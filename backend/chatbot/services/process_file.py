import fitz
import pathlib
from pathlib import Path
import os
import re
import filetype
import pytesseract
from PIL import Image
import json
import unicodedata
import chardet
from . convert_to_json import process_user_file


def detect_encoding(file_path):
    """
    Detects the file's encoding using chardet.
    """
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']


def clean_text(text):
    """
    Cleans extracted text by removing bullet points and normalizing characters.
    """
    # Normalize text to standard Unicode format
    text = unicodedata.normalize("NFKD", text)

    # Replace bullet points and special symbols
    text = re.sub(r"[\u2022•●▪]", "", text)  # Remove common bullet points

    # Optionally remove non-printable characters
    text = ''.join(c for c in text if c.isprintable())

    return text.strip()
    


def extract_file_content(file):
    """
    Extracts content from an image or PDF and saves it as text and JSON.
    """
    try:
        # Supported image extensions
        image_extension = ['jpg', 'jpeg', 'png']

        # Guess the file type using the filetype module
        file_info = filetype.guess(file)
        print(f"File info: {file_info}")

        # Initialize text as empty string
        text = ""

        # If the file is an image
        if file_info and file_info.extension in image_extension:
            print("File is an image. Using pytesseract for OCR.")
            img = Image.open(file)
            text = pytesseract.image_to_string(img)

        # If the file is not an image, assume it's a PDF
        else:
            print("File is a PDF. Using PyMuPDF for text extraction.")
            with fitz.open(file) as doc:
                text = chr(12).join([page.get_text() for page in doc])

        # Clean the extracted text
        cleaned_text = clean_text(text)

        # Save extracted text to a .txt file
        text_file_path = os.path.splitext(file)[0] + ".txt"

        # Try to save the text, use 'replace' to handle encoding issues
        try:
            # Try UTF-8 encoding first
            Path(text_file_path).write_text(cleaned_text, encoding="utf-8", errors="replace")
            print(f"Cleaned text file created: {text_file_path}")
        except UnicodeEncodeError as e:
            print(f"Error saving file with UTF-8 encoding: {e}")
            # If utf-8 fails, fall back to a different encoding (like 'latin-1')
            Path(text_file_path).write_text(cleaned_text, encoding="latin-1", errors="replace")
            print(f"Text file saved with latin-1 encoding: {text_file_path}")

        # Call function to convert the cleaned text to JSON
        return text_file_path 

    except Exception as e:
        print(f"Error in extract_file_content: {e}")
        return None


