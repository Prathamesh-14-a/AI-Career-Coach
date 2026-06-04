import pandas as pd
from src.resume_matching.resume_parser import (
    extract_resume_text ,
    extract_skills
    
)
from src.ATS.resume_parser import(
    SKILLS_DB
)
from src.ATS.ats_match import (
    get_role_skills ,
    calculated_weighted_score
)
from src.llm.resume_feedback import generate_resume_feedback




def analyze_resume(resume_file, target_role):

    resume_text = extract_resume_text(resume_file)
    resume_skills = extract_skills(resume_text, SKILLS_DB)


    da_skills = get_role_skills(target_role)

    ats_result = calculated_weighted_score(resume_skills , da_skills)
    feedback = generate_resume_feedback(ats_result, target_role)
    print(feedback)
