import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from src.salary_prediction.train_salary_model import preprocess_data
from src.salary_prediction.train_salary_model import feature_engineering
from src.salary_prediction.train_salary_model import function_transform


# Load saved model

BASE_PATH = Path("d:/Startup/Project/ai-career-coach") 
DATA_PATH = BASE_PATH / 'data' / 'Salary Prediction Data' 
SALARY_DATA_FILE = DATA_PATH / 'salary_feature_data.csv'

model = joblib.load(BASE_PATH /"src" / "models" / "best_salary_model.pkl")
print("Model loaded successfully")
data = pd.read_csv(SALARY_DATA_FILE)
sample_data = data.sample(1)
sample_data = feature_engineering(sample_data)

X,y = preprocess_data(sample_data)
y_trans = np.log1p(y)

# Predict
prediction_log = model.predict(X)

# Convert back if trained using log1p
prediction_salary = np.expm1(prediction_log)

print("Predicted Salary:", prediction_salary)
print("Actual Salary:", y)





