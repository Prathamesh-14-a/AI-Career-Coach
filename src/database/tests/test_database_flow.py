from src.database.crud import (
    create_user,
    save_resume,
    save_analysis,
    save_salary_prediction,
    get_user_resumes,
    get_analysis_history,
    get_prediction_history
)

print("=" * 50)
print("STARTING DATABASE FLOW TEST")
print("=" * 50)

# 1. Create User
user = create_user(
    username="TestUser",
    email="jethalal@gmail.com",
    password_hash="dummy_hash"
)

print(f"User Created -> ID: {user.id}")

# 2. Save Resume
resume = save_resume(
    user_id=user.id,
    resume_name="resume.pdf",
    resume_path="uploads/resume.pdf"
)

print(f"Resume Saved -> ID: {resume.id}")

# 3. Save Analysis
analysis = save_analysis(
    user_id=user.id,
    resume_id=resume.id,
    ats_score=87,
    match_score=81,
    target_role="Data Analyst"
)

print(f"Analysis Saved -> ID: {analysis.id}")

# 4. Save Salary Prediction
prediction = save_salary_prediction(
    user_id=user.id,
    role="Data Analyst",
    experience=2,
    location="Mumbai",
    skills="Python, SQL, Power BI",
    predicted_salary=750000
)

print(f"Salary Prediction Saved -> ID: {prediction.id}")

# 5. Retrieve Resume History
resumes = get_user_resumes(user.id)

print("\nResume History")
for r in resumes:
    print(
        r.id,
        r.resume_name
    )

# 6. Retrieve Analysis History
analyses = get_analysis_history(user.id)

print("\nAnalysis History")
for a in analyses:
    print(
        a.id,
        a.ats_score,
        a.target_role
    )

# 7. Retrieve Salary Prediction History
predictions = get_prediction_history(user.id)

print("\nSalary Prediction History")
for p in predictions:
    print(
        p.id,
        p.role,
        p.predicted_salary
    )

print("\nALL TESTS PASSED")