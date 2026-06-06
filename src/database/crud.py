from src.database.db_connection import SessionLocal
from src.database.models import User
from src.database.models import Resume
from sqlalchemy.orm import joinedload
from src.database.models import Analysis


#-------------------------------------------------------
# CREATE USER FUNCTION
#-------------------------------------------------------
def create_user(username , email , password_hash):

    session = SessionLocal()

    try:
        user = User(
            username = username , 
            email = email ,
            password_hash = password_hash
        )

        session.add(user)
        session.commit()

        return user

    finally:
        session.close()


#----------------------------------------------------------
# GET USER BY EMAIL
#----------------------------------------------------------
def get_user_by_email(email):
    session = SessionLocal()

    try:
        user = session.query(User).filter(
            User.email == email
        ).first()

        return user
    
    finally:
        session.close()

    
#-------------------------------------------------------------------
# CREATE RESUME
#-----------------------------------------------------------
def save_resume(
        user_id, 
        resume_name , 
        resume_path
):
    session = SessionLocal()

    try:
        resume = Resume(
            user_id = user_id,
            resume_name = resume_name,
            resume_path = resume_path
        )

        session.add(resume)
        session.commit()

        return resume
    
    finally:
        session.close()




#----------------------------------------------------------
# GET RESUMES BY USER ID
#----------------------------------------------------------
def get_user_resumes(user_id):

    session = SessionLocal()

    try:
        resumes = session.query(Resume).filter(
            Resume.user_id == user_id
        ).all()

        return resumes

    finally:
        session.close()



def get_user(user_id):
    session = SessionLocal()

    try:
        return (
            session.query(User)
            .options(joinedload(User.resumes))
            .filter(User.id == user_id)
            .first()
            )
    finally:
        session.close()


#------------------------------------------------
# SAVE ANALYSIS
#------------------------------------------------
def save_analysis(
    user_id,
    resume_id,
    ats_score,
    match_score,
    target_role
):
    session = SessionLocal()

    try:
        analysis = Analysis(
            user_id=user_id,
            resume_id=resume_id,
            ats_score=ats_score,
            match_score=match_score,
            target_role=target_role
        )

        session.add(analysis)
        session.commit()

        return analysis
    
    finally:
        session.close()


def get_analysis_history(user_id):
    session = SessionLocal()

    try:
        analyses = session.query(Analysis).filter(
            Analysis.user_id == user_id
        ).all()

        return analyses
    
    finally:
        session.close()