
# Embed and Extract PDF from PNG

This is a Flask application that allows users to embed a PDF file into a PNG image and later extract the PDF from the PNG image. This can be useful for steganography or simple file hiding.

## Features

- Upload a PDF and PNG image to embed the PDF into the PNG image.
- Upload a PNG image to extract an embedded PDF file.
- Simple and clean web interface.

## Requirements

- Python 3.x
- Flask
- PyPNG

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nskath/PDFtoPNG.git
cd PDFtoPNG
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Use the web interface to upload PDF and PNG files for embedding and extracting PDFs from PNG files.

## Project Structure

```plaintext

├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

- `static/`: Contains the CSS file for styling the web interface.
- `templates/`: Contains the HTML template for the web interface.
- `app.py`: The main Flask application.
- `requirements.txt`: Lists the Python packages required for the project.
- `README.md`: Project documentation.


