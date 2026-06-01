import pdfplumber
import re
from pathlib import Path
import pytesseract
from pdf2image import convert_from_path
from src.resume_matching.resume_parser import (extract_resume_text , 
                                               extract_with_ocr , 
                                               clean_resume_text , 
                                               text_validation , 
                                               extract_skills , 
                                               TECHNICAL_SKILLS)

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
    
    return resume_text

    
def cleaned_resume_text(resume_text:str) -> str:
    # clean text
    cleaned_text = clean_resume_text(resume_text)
    return cleaned_text

    

resume = r"d:\Startup\Project\ai-career-coach\data\resume\Pratham_Resume_Updated.pdf"



class SectionParser:

    SECTION_PATTERNS = {
        "summary": r"(professional summary|summary|profile)",
        "skills": r"(technical skills|skills|core competencies)",
        "projects": r"(projects|project experience)",
        "education": r"(education|academic background)",
        "experience": r"(experience|work experience|professional experience)",
        "certifications": r"(certifications|licenses)"
    }

    def extract_sections(self, text):
        """
        Extract structured resume sections
        """

        sections = {}

        lower_text = text.lower()

        matches = []

        for section, pattern in self.SECTION_PATTERNS.items():
            match = re.search(pattern, lower_text)

            if match:
                matches.append((match.start(), section))

        matches.sort()

        for i in range(len(matches)):
            start_pos, section_name = matches[i]

            if i + 1 < len(matches):
                end_pos = matches[i + 1][0]
            else:
                end_pos = len(text)

            sections[section_name] = text[start_pos:end_pos].strip()

        return sections

result_text = process_resume(resume)
cleaned_text = cleaned_resume_text(result_text)
section_parser = SectionParser()

sections = section_parser.extract_sections(cleaned_text)

# for section, content in sections.items():
#     print(f"\n{'='*60}")
#     print(f"{section.upper()}")
#     print(f"{'='*60}")
#     print(content[:700])

skill_section = sections.get("skills" , "")
project_section = sections.get("projects" , "")

skills_from_skills = extract_skills(skill_section , TECHNICAL_SKILLS)
skills_from_projects = extract_skills(project_section , TECHNICAL_SKILLS)

print("\nSkills Section Matches:")
print(skills_from_skills)

print("\nProjects Section Matches:")
print(skills_from_projects)

print("\nCombined Unique Skills:")
print(sorted(set(skills_from_skills + skills_from_projects)))



# testing on 10 resumes
# for i in range(1 , 18):
    # resume = Path((rf"d:\Startup\Project\ai-career-coach\data\resume\resume_{i}.pdf"))
   
    # print(f'\nResume Skill Extraction For Resume No. {i}\n')
    # result_text = process_resume(resume)
    # cleaned_text = cleaned_resume_text(result_text)
    # section_parser = SectionParser()

    # sections = section_parser.extract_sections(cleaned_text)

    # for section, content in sections.items():
    #     print(f"\n{'='*60}")
    #     print(f"{section.upper()}")
    #     print(f"{'='*60}")
    #     print(content[:700])
