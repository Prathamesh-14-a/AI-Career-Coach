from src.salary_prediction.salary_predictor import master_salary_prediction_pipeline
from src.database.crud import save_salary_prediction , get_prediction_history

user_id = 1
role = 'Data Engineer'
experience = 5
location = 'Ahmedabad'
skills = "python, machine learning, sql, pandas"
predicted_salary = master_salary_prediction_pipeline(role , experience , location , skills)

prediction = save_salary_prediction(
    user_id , 
    role,
    experience,
    location,
    skills,
    predicted_salary
)
print('Prediction Data Saved Succesfully')

prediction_data = get_prediction_history(user_id)

for data in prediction_data:
    print(
        data.user_id,
        data.role,
        data.experience,
        data.location,
        data.skills,
        data.predicted_salary
    )