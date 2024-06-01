from flask import Flask, request, send_file, render_template, abort
import os
import io
import tempfile
from werkzeug.utils import secure_filename
import png

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def embed_file_into_png(file_content, png_path, output_path):
    reader = png.Reader(filename=png_path)
    chunks = list(reader.chunks())
    iend_index = next(i for i, chunk in enumerate(chunks) if chunk[0] == b'IEND')
    custom_chunk = (b'UIUC', file_content)
    chunks.insert(iend_index, custom_chunk)
    with open(output_path, 'wb') as output_file:
        png.write_chunks(output_file, chunks)

def extract_file_from_png(png_path):
    reader = png.Reader(filename=png_path)
    chunks = reader.chunks()
    for chunk_type, content in chunks:
        if chunk_type == b'UIUC':
            return content
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'image' not in request.files:
        return 'Missing file part', 400
    file = request.files['file']
    image = request.files['image']
    if file.filename == '' or image.filename == '':
        return 'No selected file', 400
    if file.content_type != 'application/pdf':
        return 'File must be a PDF', 400

    file_content = file.read()
    temp_image_path = os.path.join(tempfile.gettempdir(), secure_filename(image.filename))
    output_image_path = os.path.join(UPLOAD_FOLDER, 'embedded_' + secure_filename(image.filename))
    
    image.save(temp_image_path)
    embed_file_into_png(file_content, temp_image_path, output_image_path)

    return send_file(output_image_path, mimetype='image/png', as_attachment=True, download_name='embedded_image.png')

@app.route('/extract', methods=['POST'])
def extract_file():
    if 'image' not in request.files:
        return 'Missing file part', 400
    image = request.files['image']
    if image.filename == '':
        return 'No selected file', 400

    temp_image_path = os.path.join(tempfile.gettempdir(), secure_filename(image.filename))
    image.save(temp_image_path)

    file_content = extract_file_from_png(temp_image_path)
    if file_content:
        return send_file(io.BytesIO(file_content), attachment_filename='extracted_file.pdf', as_attachment=True)
    else:
        return 'No UIUC chunk found', 404

if __name__ == '__main__':
    app.run(debug=True)
