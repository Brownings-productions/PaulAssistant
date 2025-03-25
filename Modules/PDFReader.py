import fitz  # PyMuPDF
import pymupdf4llm as pymu
import os
import json

def to_raw(string):
    return fr"{string}"

def pdf_path(file_name):
    root_path = os.path.abspath(os.path.join("Archives", file_name))
    # Get the absolute path of the PDF file
    return root_path

def extract_text_from_pdf():
    pdf_file = "BMW.pdf"

    pdf_file_path = pdf_path(pdf_file)

    try:
        doc=fitz.open(to_raw(pdf_file_path))

        result = []


        #for page in doc:
        #    block = page.get_text("blocks")
        #    for block in blocks:






        #Open the PDF file
    #    doc = fitz.open(to_raw(pdf_file_path))
    #    out = open("output.txt", "w", encoding="utf-8")
#
    #    for page in doc:
    #        text = page.get_text()
    #        out.write(text + "\n")
    #    out.close()
#
    #    with open("output.txt", "r", encoding="utf-8") as file:
    #        text = file.read()  
    #    return text

    except Exception as e:
        print(f"Error: {e}")
