import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import dataset
df = pd.read_csv(r"d:\Startup\Project\ai-career-coach\data\processed\salary_jobs.csv")
skill_df = pd.read_csv(r"d:\Startup\Project\ai-career-coach\data\processed\jobs_with_skills.csv")

print('Salary Statistics : \n')
print(df['salary_avg'].describe().round(2))

print('Checking Nulls : \n')
print(df['salary_avg'].isnull().sum())

#plotiing salary distribution
# Salary Distribution
sns.histplot(
    df['salary_avg'], 
    kde = True,
    color='purple',
    element='step'
)
plt.title('Distribution Of Salary Average')
plt.show()

print('Salary by Experience : \n')
print(df.groupby("Experience Required")["salary_avg"].median())

#Checking for outliers 
sns.boxplot(
    df['salary_avg']
)

# Salary by Job Role
print('Salary By Job Role : \n')
salary_job_role = (df.groupby('Standardized_Job_Title')
                   ['salary_avg'].median()
                   .sort_values(ascending=False))
print(salary_job_role)

# bar plot for job_role vs salary
salary_job_role.sort_values().plot(kind='barh')
plt.xlabel('Salary LPA (1LPA = 0.1)')
plt.title('Salary by Job Role')
plt.show()


#Location Vs Salary analysis
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

salary_location = (df.groupby('Location')
                   ['salary_avg'].median()
                   .sort_values(ascending=False))
print('Salary vs Location')
print(salary_location)

# location Count to know outliers
print('Location Count :')
print(df.groupby("Location")["salary_avg"].count())

# plotting Salary by location
salary_location.head(10).plot(kind="bar")
plt.title("Top Paying Locations")
plt.show()

# getting valid locations
valid_locations = ["Remote", "Bangalore", "Delhi", "Gurgaon", "Noida"]

filtered_location_df = df[df["Location"].isin(valid_locations)]
print('filteres location vs salary')
print(
    filtered_location_df.groupby("Location")["salary_avg"]
    .median())

#comparing salary for remote jobs and onsite jobs
remote_salary = df[df["Location"] == "Remote"]["salary_avg"].median()
onsite_salary = df[df["Location"] != "Remote"]["salary_avg"].median()
print('Remote Salary :\n' , remote_salary)
print('Onsite Salary : \n' , onsite_salary)

# premium skills with salaries 
premium_skills_list = [
    'tensorflow', 'pytorch', 'nlp', 'llm', 'artificial intelligence',
    'computer vision', 'spark', 'hadoop', 'airflow', 'dbt',
    'databricks', 'snowflake', 'big data',
    'aws', 'azure', 'gcp',
    'scala', 'java'
]
premium_skills = {}

for skill in premium_skills_list:
    skill_jobs = skill_df[
        skill_df["extracted_skills"].str.contains(skill, na=False)
    ]
    
    premium_skills[skill] = skill_jobs["salary_avg"].dropna().median()

premium_skill_df = pd.DataFrame(
    premium_skills.items(),
    columns=["Skill", "Median_Salary"]
)

premium_skill_df = premium_skill_df.dropna()

print('preview of premium skill df : \n')
print(premium_skill_df)

# creating salary band
def salary_band(salary):
    if salary < 400000:
        return "Low"
    elif salary < 800000:
        return "Mid"
    else:
        return "High"

skill_df["Salary_Band"] = skill_df["salary_avg"].apply(
    lambda x: salary_band(x) if pd.notnull(x) else "Unknown"
)

df["Salary_Band"] = df["salary_avg"].apply(
    lambda x: salary_band(x) if pd.notnull(x) else "Unknown"
)

skill_df = skill_df.dropna()
print(skill_df.shape)

# Saving df into csv
df.to_csv(
    r"d:\Startup\Project\ai-career-coach\data\processed\salary_enhanced.csv",
    index=False
)

premium_skill_df.to_csv(
     r"d:\Startup\Project\ai-career-coach\data\processed\premiun_skill_salary.csv",
    index=False
)

filtered_location_df.to_csv(
    r"d:\Startup\Project\ai-career-coach\data\processed\filtered_location_df.csv",
    index=False
)

print('DataFrames Saved into CSV sucessfully !!!')

