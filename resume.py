#importing the required libraries
import pdfplumber
import docx

def extract_text_from_pdf(file) -> str: #return in text
    text = "" #empty string to store all the extracted text
    with pdfplumber.open(file) as pdf: #opens the uploaded pdf file
        for page in pdf.pages:#loops each page in the pdf
            page_text = page.extract_text() #it extracts text from the current page
            if page_text:
                text += page_text + "\n"  #only adds the text if something was found
    return text

def extract_text_from_docx(file) -> str:
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def get_text(file) -> str:
    name = file.name.lower()
    if name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif name.endswith(".docx"):
        return extract_text_from_docx(file)
    elif name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        raise ValueError("Unsupported file type")

            



