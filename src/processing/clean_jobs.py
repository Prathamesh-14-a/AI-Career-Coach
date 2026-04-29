import pandas as pd 
import re
import numpy as np

df = pd.read_csv(r'd:\Startup\Project\ai-career-coach\data\processed\jobs_filtered.csv')

print("Data Inspection Before Cleaning:")
print("First few rows before cleaning:")
print(df.head())
print("Data types and missing values:")
print(df.info())
print("Number of Columns Before Cleaning:", df.shape[1])
print("Number of Rows  Before Cleaning:", df.shape[0])

#Checking for duplicates 
print("Number of duplicate rows:", df.duplicated().sum())

#Checking for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# filling missing values in location and experience required with "Not Specified" 
df["Location"].fillna("Not Specified", inplace=True)
df["Experience Required"].fillna("Not Specified", inplace=True)

#Standardize Job Titles
def standardize_job_title(title):
    title = title.lower()

    if "data analyst" in title:
        return "Data Analyst"
    elif "data scientist" in title:
        return "Data Scientist"
    elif "business analyst" in title:
        return "Business Analyst"
    elif "machine learning" in title:
        return "Machine Learning Engineer"
    elif "data engineer" in title:
        return "Data Engineer"
    elif "product analyst" in title :
        return "Product Analyst"
    elif "analytics" in title:
        return "Analytics"
    else:
        return "Other"
    
df["Standardized_Job_Title"] = df["Job Title"].apply(standardize_job_title)

print("unique job roles :")
print(df["Standardized_Job_Title"].value_counts())

# Normalize Posting Dates
def normalize_posting_date(date_str):
    date_str =  str(date_str).lower()

    if 'few' in date_str or 'hour' in date_str or 'today' in date_str:
        return 0 
    elif 'day' in date_str:
        num = re.search(r'\d+' , date_str)
        return int(num.group()) if num else 1 
    elif 'week' in date_str:
        num = re.search(r'\d+' , date_str)
        return int(num.group())*7 if num else 7
    elif 'month' in date_str:
        num = re.search(r'\d+' , date_str)
        return int(num.group())*30 if num else 30
    elif "30+" in date_str:
        return 30
    else:
        None

df["days_sinced_posted"] = df["Posted Date"].apply(normalize_posting_date)

print("Days Since Posted:")
print(df["days_sinced_posted"].value_counts())

# Salary Cleaning

# Function to process salary
def clean_salary(salary_text):
    salary_text = str(salary_text).strip()

    if "competitive" in salary_text.lower() or salary_text == "nan":
        return pd.Series([np.nan, np.nan, np.nan])

    cleaned = salary_text.replace("₹", "").replace(",", "").strip()

    if "-" in cleaned:
        parts = cleaned.split("-")

        try:
            salary_min = int(parts[0].strip())
            salary_max = int(parts[1].strip())
            salary_avg = (salary_min + salary_max) / 2

            return pd.Series([salary_min, salary_max, salary_avg])

        except:
            return pd.Series([np.nan, np.nan, np.nan])
    else:
        try:
            salary_value = int(cleaned.strip())

            return pd.Series([salary_value, salary_value, salary_value])

        except:
            return pd.Series([np.nan, np.nan, np.nan])


# Apply function
df[["salary_min", "salary_max", "salary_avg"]] = df["Salary"].apply(clean_salary)

# Optional: Fill missing values
df["salary_min"] = df["salary_min"].fillna(np.nan)
df["salary_max"] = df["salary_max"].fillna(np.nan)
df["salary_avg"] = df["salary_avg"].fillna(np.nan)

print("Salary cleaning completed successfully!")
print(df[["Salary", "salary_min", "salary_max", "salary_avg"]].head(10))


# Create salary subset (only rows with valid salary) It will help in Salary Analysis and Salary Prediction Model
salary_df = df[df["salary_avg"].notnull()].copy()

salary_df.reset_index(drop=True, inplace=True)

salary_df.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\salary_jobs.csv", index=False)

print("Salary subset created successfully!")
print("Salary dataset shape:", salary_df.shape)
print(salary_df[["Job Title", "salary_min", "salary_max", "salary_avg"]].head())


#Location Standardization
print("Location Value Counts:")
print(df["Location"].value_counts())

location_mapping = {
    "Work from home": "Remote",
    "Nanakramguda": "Hyderabad",
    "Yalahanka": "Bangalore",
    "Gurgaon": "Gurgaon",
    "Noida": "Noida",
    "Maharashtra": "Maharashtra",
    "Telangana": "Telangana"
}
df["Location"] = df["Location"].replace(location_mapping)

# Experience Required Standardization
print("Experience Required Value Counts:")
print(df["Experience Required"].value_counts())

def extract_experience_years(exp_text):
    exp_text = exp_text.lower()

    if "no experience required" in exp_text:
        return 0
    else:
        match = re.search(r'\d+', str(exp_text))
        return int(match.group()) if match else np.nan
    
df["Experience_Years"] = df["Experience Required"].apply(extract_experience_years)

print("================= Data cleaning completed successfully! ==================")
print("Data Inspection After Cleaning:")
print("First few rows after cleaning:")
print(df.head())
print("Data types and missing values:")
print(df.info())
print("Number of Columns After Cleaning:", df.shape[1])
print("Number of Rows  After Cleaning:", df.shape[0])

# Save cleaned data to new CSV
df.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\jobs_cleaned.csv", index=False)
print("Cleaned data saved to CSV file successfully!")
