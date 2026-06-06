from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime , ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Float


class Base(DeclarativeBase):
    pass


# User Table
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    resumes = relationship(
        "Resume",
        back_populates="user",
        lazy="joined")
    
    analyses = relationship(
        "Analysis",
        back_populates="user"
    )


# Resume Table
class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    resume_name = Column(String(255))
    resume_path = Column(String(500))

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="resumes"
    )

    analyses = relationship(
    "Analysis",
    back_populates="resume"
    )

# Analysis Table
class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False
    )

    ats_score = Column(Float)

    match_score = Column(Float)

    target_role = Column(String(255))

    analysis_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="analyses"
    )

    resume = relationship(
        'Resume',
        back_populates="analyses"
    )




