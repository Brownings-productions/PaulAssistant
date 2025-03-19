import fitz  # PyMuPDF
import pymupdf4llm as pymu
import os

def to_raw(string):
    return fr"{string}"

def pdf_path(file_name):
    root_path = os.path.abspath(os.path.join("Archives", file_name))
    # Get the absolute path of the PDF file
    return root_path

pdf_file = "BMW.pdf"

pdf_file_path = pdf_path(pdf_file)
output_file = "output.txt"

try:
    # Open the PDF file
    doc = fitz.open(to_raw(pdf_file_path))
    
    with open(output_file, "w", encoding="utf-8") as out:
        for page in doc:
            text = page.get_text()
            out.write(text + "\n")  # Ensure line breaks

    print(f"Text extracted successfully to {output_file}")

except Exception as e:
    print(f"Error: {e}")
