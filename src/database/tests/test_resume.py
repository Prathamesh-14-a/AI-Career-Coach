
from src.database.crud import save_resume
from src.database.crud import get_user_resumes
from src.database.crud import get_user


resume = save_resume(
    user_id =1,
    resume_name="data_analyst_resume.pdf",
    resume_path="uploads/data_analyst_resume.pdf"
)

resume = save_resume(
    user_id =1,
    resume_name="ml_resume.pdf",
    resume_path="uploads/ml_resume.pdf"
)

print('Resume Saved')

resumes = get_user_resumes(1)

for resume in resumes:
    print(
        resume.id,
        resume.resume_name,
        resume.resume_path
    )

user = get_user(1)

for resume in user.resumes:
    print(resume.resume_name)