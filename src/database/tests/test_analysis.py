from src.database.crud import save_analysis
from src.database.crud import get_analysis_history

analysis = save_analysis(
    user_id=1,
    resume_id=1,
    ats_score=85.0,
    match_score=90.0,
    target_role="Data Analyst"
)

analyses = get_analysis_history(user_id=1)

for analysis in analyses:
    print(
        analysis.id,
        analysis.resume_id,
        analysis.ats_score,
        analysis.match_score,
        analysis.target_role,
        analysis.analysis_date
    )