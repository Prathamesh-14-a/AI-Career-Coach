import pdfplumber
import re
from pathlib import Path
import logging

# -------------------------------
# TECHNICAL SKILL LISTS
# -------------------------------
technical_skills = [
    
    'python', 'r', 'sql', 
    'excel' 'microsoft excel',
    'power bi', 'tableau',

    'etl', 'spark', 'hadoop',
    'airflow', 'dbt',

    'machine learning',
    'tensorflow', 'pytorch', 'scikit-learn',

    'aws', 'azure', 'gcp', 

    'pandas', 'numpy', 'matplotlib',
    'seaborn', 'plotly', 'ggplot2',

    ]


# ---------------------------------------
# RESUME TEXT CLEAN
# ---------------------------------------
def clean_resume_text(text:str) -> str:

    # lower case
    text =  text.lower()
    # extra spaces
    text = re.sub(r'\s+', ' ', text)
    # character symbols
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ' , text)
    # extra characters
    text = re.sub(r'[\r\n\xa0]+' , ' ' , text)
    # irrelavent numbers
    text = re.sub(r'\b\d+\b', '', text)
    # design symbols
    text = re.sub(r"[•★►▪]", " ", text)
    #extra spaces
    text = re.sub(r'\s+' ,' ' , text)

    return text.strip()


# ------------------------------------------
# EXTRACT TEXT THROUGH RESUME PDF 
# ------------------------------------------
def extract_resume_text(path:str) ->str:

    pages_text = []

    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text :
                    pages_text.append(page_text)
                
        full_text = " ".join(pages_text)

        return clean_resume_text(full_text)

    except Exception as e:
        logging.error(f'Error Reading Resume : {e}')
        return ""
    

# ----------------------------------------------
# EXTRACT SKILL FROM RESUME
# ----------------------------------------------
def extract_skills(resume_text: str, skills_list: list) -> list:

    skill_set = set()
    for skill in skills_list:
        escape_skill = re.escape(skill)

        pattern = rf'\b{escape_skill}\b'

        if re.search(pattern , resume_text):
            skill_set.add(skill)

    return sorted(skill_set)

# -------------------------------------------------
# RESUME PROCESS
# -------------------------------------------------
def process_resume(path:str) -> dict:

    resume_text = extract_resume_text(path)

    # validation
    if not resume_text:
        return {
            'status' : 'failed' ,
            'skills' : [] , 
            'resume_text' : ''
        }
    
    skills = extract_skills(resume_text , technical_skills)

    return {
        'status' : 'successful' , 
        'skills' : skills , 
        'resume_text' : resume_text[0:100] + '.......'
    }


# ------------------------------------------------
# TESTING
# ------------------------------------------------

if __name__ == "__main__":

    path = Path(r"d:\Startup\Project\ai-career-coach\data\resume\Pratham_resume.pdf")
    result = process_resume(path)
    print(result)

    # testing on 10 resumes
    for i in range(1 , 18):
        resume_paths = Path((rf"d:\Startup\Project\ai-career-coach\data\resume\resume_{i}.pdf"))
        result = process_resume(resume_paths)
        print(f'Resume Skill Extraction For Resume No. {i}')
        print(result)
