import pdfplumber
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from src.resume_matching.resume_parser import (extract_resume_text , 
                                               extract_with_ocr , 
                                               clean_resume_text , 
                                               text_validation)

def process_resume(path:str) -> str:

    print("\nTrying PDFPlumber extraction...")
    # trying normal extraction
    resume_text = extract_resume_text(path)

    if not text_validation(resume_text):

        print('text quality is poor..')
        print('switching to OCR extraction')
        resume_text = extract_with_ocr(path)
    
    else:
        print('pyplumber extraction successful...')

    
    # clean text
    cleaned_text = clean_resume_text(resume_text)

    print("\nEXTRACTED TEXT:\n")
    print(cleaned_text[:2000])

resume = r"d:\Startup\Project\ai-career-coach\data\resume\Pratham_resume.pdf"
process_resume(resume)


# testing on 10 resumes
for i in range(1 , 18):
    resume_paths = Path((rf"d:\Startup\Project\ai-career-coach\data\resume\resume_{i}.pdf"))
   
    print(f'\nResume Skill Extraction For Resume No. {i}\n')
    result = process_resume(resume_paths)
    result
