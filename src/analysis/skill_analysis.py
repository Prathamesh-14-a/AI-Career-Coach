import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

#import data
df = pd.read_csv(r'd:\Startup\Project\ai-career-coach\data\processed\skill_frequencies.csv')
role_df = pd.read_csv(r"d:\Startup\Project\ai-career-coach\data\processed\role_skill_mapping.csv")

print('Data Preview : \n')
print(f'Skill_freq : \n {df.head()}')
print(f'Info:  {df.info()}')

print('Data Preview : \n')
print(f'Role Skill Map: \n {role_df.head()}')
print(f'Info: {role_df.info()}')

print(df.sort_values(by='Count' , ascending= False ).head(10))
#filtering general skills
exclude_skills = [
    "analysis",
    "research",
    "data analysis",
    "communication"
]
filtered_skill_df = df[~ df['Skill'] .isin(exclude_skills)].copy()

print('Preview of filtered skill df :\n')
print(filtered_skill_df.sort_values(by='Count' , ascending= False ).head(10))

#Top 20 Skills Bar Chart 

top_skills = filtered_skill_df.sort_values(by='Count' , 
                            ascending=False ).head(20)

plt.figure(figsize=(12,6))
plt.bar(x=top_skills['Skill'] ,
        height = top_skills['Count'] ,
                color = 'yellow' , 
                alpha = 0.7 , 
                edgecolor = 'black' , 
                linewidth = 1 )
plt.title('Top 20 Skills' , fontsize = 12)
plt.xlabel('Skills' , fontsize = 10)
plt.ylabel('Count' , fontsize = 10)
plt.xticks(rotation = 90)
plt.show()


# creating categories
def category_skill(skill):
    if skill in ['python' , 'sql' , 'r' , 'java' , 'scala']:
        return 'Programming'
    elif skill in ['power bi' , 'tableau' , 'excel']:
        return 'BI'
    elif skill in ['aws' , 'gcp' , 'azure']:
        return 'Cloud'
    elif skill in ['tensorflow' , 'sckit-learn' , 'pytorch' , 'machine learning']:
        return 'Machine Learning'
    elif skill in ['communication'   , 'problem solving' , 'presentation' ,'leadership' ]:
        return 'Soft Skills' 
    elif skill in ['postgresql' , 'oracle' , 'mysql' , 'mongodb' ]:
        return 'DataBase'
    elif skill in [ 'data preprocessing'  , 'pandas']:
        return 'Data Cleaning'
    elif skill in ['etl' , 'hadoop' ,'databricks' , 'dbt' ,'spark' , 'big data' ,'snowflake', 'airflow']:
        return 'Data Engineering'
    elif skill in ['nlp' , 'llm' , 'artificial intelligence']:
        return 'Artificial Intelligence'
    elif skill in ['ggplot2' , 'matplotlib' , 'data visualization' , 'seaborn' , 'dashboarding']:
        return 'Data Visualization'
    elif skill in [ "analysis", "research", "data analysis"]:
        return 'Generic Terms'
    else:
        return 'Other'
    
filtered_skill_df['category'] = filtered_skill_df['Skill'].apply(category_skill)

print('Category Preview : \n')
print(filtered_skill_df[['Skill' , 'category']])

category_counts = filtered_skill_df.groupby('category')['Count'].sum().sort_values(ascending=False)
print('Category Count Preview : \n')
print(category_counts)

#ploting bar chart for category counts
category_counts.sort_values().plot(kind='barh',
                                   color = sns.color_palette('viridis' , len(category_counts)))
plt.title("Skill Demand by Category")
plt.show()

# creating wordcloud
skill_count_dict = dict(
    zip(filtered_skill_df['Skill'] , filtered_skill_df['Count'])
)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="white"
).generate_from_frequencies(skill_count_dict)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most In-Demand Skills")
plt.show()
wordcloud.to_file(
   r'D:\Startup\Project\ai-career-coach\reports\dashboard_images\skill_wordcloud.png'
)

#Role Skill Analysis
role_df_filtered =role_df[ ~role_df['Skill'].isin(exclude_skills)].copy()
print(
    'Top SKills for Data Analyst : \n',
    role_df_filtered[role_df_filtered["Role"] == "Data Analyst"].head(10).sort_values(by = 'Count',ascending=False)
)

#creating pivot 
plt.figure(figsize=(12,6))
sns.heatmap(
role_df_filtered.pivot_table(
    index = 'Role' , 
    columns= 'Skill' ,
    values= 'Count', 
    fill_value= 0
) , cmap='coolwarm' , 
    linewidths=0.1,
    linecolor= 'white' )


## Creating enhanced_skill.csv

# creating Demand Level
def demand_level(count):
    if (count >= 40) :
        return 'High'
    elif (count < 40 ) and (count >= 15) :
        return 'Medium'
    else: 
        return 'Low'
    
filtered_skill_df['demand_level']= filtered_skill_df['Count'].apply(demand_level)

# Percentage of jobs
filtered_skill_df['percentage_of_jobs'] = (
    filtered_skill_df['Count'] / len(role_df_filtered) * 100
)

# Rank for jobs
filtered_skill_df["Rank"] = filtered_skill_df["Count"].rank(
    ascending=False,
    method="dense"
)

# Premium skills 
premium_skills = [
    'tensorflow', 'pytorch', 'nlp', 'llm', 'artificial intelligence',
    'computer vision', 'spark', 'hadoop', 'airflow', 'dbt',
    'databricks', 'snowflake', 'big data',
    'aws', 'azure', 'gcp',
    'scala', 'java'
]

filtered_skill_df['premium_skill'] = (filtered_skill_df['Skill']
                     .apply(lambda skill: 'Yes' if skill in premium_skills
                                           else 'No'))


#Standardizing Skills
skill_standardization_map = {
    # Programming Languages
    'python': 'Python',
    'r': 'R',
    'sql': 'SQL',
    'java': 'Java',
    'scala': 'Scala',

    # Data Analysis / Visualization
    'excel': 'Excel',
    'power bi': 'Power BI',
    'tableau': 'Tableau',
    'data visualization': 'Data Visualization',
    'dashboarding': 'Dashboarding',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'ggplot2': 'GGPlot2',
    'kpi': 'KPI Analysis',

    # Databases
    'mysql': 'MySQL',
    'postgresql': 'PostgreSQL',
    'mongodb': 'MongoDB',
    'oracle': 'Oracle Database',
    'snowflake': 'Snowflake',

    # Data Engineering / Big Data
    'etl': 'ETL',
    'big data': 'Big Data',
    'spark': 'Apache Spark',
    'hadoop': 'Hadoop',
    'airflow': 'Apache Airflow',
    'dbt': 'dbt',
    'databricks': 'Databricks',

    # Cloud Platforms
    'aws': 'Amazon Web Services (AWS)',
    'azure': 'Microsoft Azure',
    'gcp': 'Google Cloud Platform (GCP)',

    # Machine Learning / AI
    'tensorflow': 'TensorFlow',
    'pytorch': 'PyTorch',
    'nlp': 'Natural Language Processing (NLP)',
    'llm': 'Large Language Models (LLMs)',
    'artificial intelligence': 'Artificial Intelligence (AI)',
    'computer vision': 'Computer Vision',

    # Statistics / Data Science
    'statistics': 'Statistics',
    'pandas': 'Pandas',
    'numpy': 'NumPy',
    'data preprocessing': 'Data Preprocessing',

    # Business / Soft Skills
    'business analysis': 'Business Analysis',
    'market research': 'Market Research',
    'stakeholder management': 'Stakeholder Management',
    'leadership': 'Leadership',
    'presentation': 'Presentation Skills'
}
filtered_skill_df['standardized_skills'] = filtered_skill_df['Skill'].map(skill_standardization_map)


print('Enhanced Skill df : \n')
print(filtered_skill_df.head(10))


# Saving Enhanced skills Data as Csv
filtered_skill_df.to_csv(r'd:\Startup\Project\ai-career-coach\data\processed\Enhanced_skills_dataset.csv' ,
                         index = False)

#Saving Role Filtered Dataset
role_df_filtered.to_csv(r'd:\Startup\Project\ai-career-coach\data\processed\role_df_filtered.csv' ,
                        index = False)

print("Datasets Saved Sucessfully !!!")

