import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

df = pd.read_csv(r"d:\Startup\Project\ai-career-coach\data\processed\jobs_cleaned.csv")

# Creating combined text feature 
df["combined_text"] = (
    df["Standardized_Job_Title"].fillna("") + " " +
    df["Job Description"].fillna("") + " " +
    df["Skills Required"].fillna("")
)

# sample text before cleaning
print(f'Sample Text Before Cleaning : {df["combined_text"].iloc[0]}')

#removed punctuation and converted to lowercase
df["combined_text"] = (df["combined_text"].str.lower()
                       .apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', ' ', x)))

# removing \r\n\xa0 these extra characters
df["combined_text"] = (df['combined_text']
                       .apply(lambda x : re.sub(r'[\r\n\xa0]+' , ' ' , x)).str.strip())

# removing extra spaces
df["combined_text"] = (df['combined_text']
                       .apply(lambda x: re.sub(r'\s+', ' ', x).strip()))

# removing irrelevant numbers
df['combined_text'] = (df["combined_text"]
                        .apply(lambda x: re.sub(r'\b\d+\b', '', x)))

#sample text after cleaning
print(f'Sample Text After Cleaning : {df["combined_text"].iloc[0]}')


#Tokenization
nltk.download("punkt_tab")
df['tokens'] = df["combined_text"].apply(word_tokenize)
print("Preview of tokens : ")
print(df['tokens'].iloc[0])


# Stopword Removal
nltk.download("stopwords")

def stopwords_removal(tokens):
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

df['filtered_tokens'] = df['tokens'].apply(stopwords_removal)
print("Preview of filtered tokens : ")
print(df['filtered_tokens'].iloc[0])


#Lemmatization
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()

df["lemmatized_tokens"] = (df["filtered_tokens"]
                    .apply(lambda tokens: [lemmatizer
                                           .lemmatize(token , pos = "v") for token in tokens]))

print("Preview of lemmatized tokens : ")
print(df["lemmatized_tokens"].iloc[0])


# creating processed text by joining lemmatized tokens
df["processed_text"] = df["lemmatized_tokens"].apply(lambda x: " ".join(x))
print("Preview of processed text : ")   
print(df["processed_text"].iloc[0])

# skill extraction 
skills_list = ['python' ,'r','sql','java','scala','c++' ,
               'excel','power bi','tableau' ,'statistics',
               'data visualization','reporting','dashboarding' , 
               'mysql','postgresql','mongodb','snowflake','oracle' ,
               'etl','data warehousing','spark','hadoop','airflow','dbt',
               'machine learning','deep learning','nlp','tensorflow',
               'pytorch','scikit-learn','computer vision','llm' ,
               'aws','azure','gcp','databricks' ,'business analysis',
               'stakeholder management','kpi','forecasting','market research' ,
               'communication','problem solving','leadership','presentation',
               'pandas','numpy','matplotlib','seaborn','plotly','ggplot2',
               'artificial intelligence','big data',
               'data mining','data cleaning', 'data preprocessing',
               'data modeling','data analysis',
               'data storytelling', 'research','analysis','reporting','dashboard' ,
                'structured query language',
               'visualization','google sheets' , 'microsoft excel']

print(f'Number of skills : {len(skills_list)}')

# function to extract skills from processed text
def skill_extracter(text):
    extracted_skills = []

    for skill in skills_list:
        
        if re.search(r'\b' + re.escape(skill) + r'\b', text):
            extracted_skills.append(skill)

    return list(set(extracted_skills))


df["extracted_skills"] = df["processed_text"].apply(skill_extracter)
df["skill_count"] = df["extracted_skills"].apply(len)

print("Preview of extracted skills : ") 
print(df[["Standardized_Job_Title", "extracted_skills", "skill_count"]].head())


# skill normalization
normalization_dict = {
    "microsoft excel": "excel",
    "structured query language": "sql",
    "visualization": "data visualization",
    "dashboard": "dashboarding"
}
df['extracted_skills'] = (df['extracted_skills']
        .apply(lambda skills: [normalization_dict.get(skill, skill) for skill in skills]))

#extracting technical skills
technical_skills = [
    # Programming
    'python', 'r', 'sql', 'java', 'scala', 'c++',

    # Data tools
    'excel', 'google sheets', 'microsoft excel',
    'power bi', 'tableau',

    # Statistics & analytics
    'statistics',

    # Databases
    'mysql', 'postgresql', 'mongodb', 'snowflake', 'oracle',

    # Data engineering
    'etl', 'data warehousing', 'spark', 'hadoop',
    'airflow', 'dbt',

    # Machine learning / AI
    'machine learning', 'deep learning', 'nlp',
    'tensorflow', 'pytorch', 'scikit-learn',
    'computer vision', 'llm', 'artificial intelligence',

    # Cloud / infrastructure
    'aws', 'azure', 'gcp', 'databricks',

    # Python libraries
    'pandas', 'numpy', 'matplotlib',
    'seaborn', 'plotly', 'ggplot2',

    # Data-specific processes
    'big data', 'data mining', 'data cleaning',
    'data preprocessing', 'data modeling',
    'data analysis', 'structured query language'
]


# separating technical skills 
df["technical_skills"]= (df["extracted_skills"]
                .apply(lambda skills: [skill for skill in skills if skill in technical_skills]))   


#extracting soft skills
soft_skills = [
    'communication',
    'problem solving',
    'leadership',
    'presentation',
    'stakeholder management',
    'research'
]

df["soft_skills"] = (df["extracted_skills"]
                .apply(lambda skills:[skill for skill in skills if skill in soft_skills]))


# extracting business skills
business_terms = [
    'business analysis',
    'kpi',
    'forecasting',
    'market research',
    'data visualization',
    'visualization',
    'reporting',
    'dashboarding',
    'dashboard',
    'data storytelling',
    'analysis'
]

df['business_skills'] = (df['extracted_skills']
                     .apply(lambda skills: [skill for skill in skills if skill in business_terms]))


# saving the dataframe with extracted skills
df.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\jobs_with_skills.csv", index=False)
print("Dataframe with extracted skills saved successfully.")


# skill count frequency
all_skills = [
    skill 
    for skill_list in df['extracted_skills'] 
    for skill in skill_list
]

skill_counts = Counter(all_skills)
print("Top 20 Most Common Skills : ")
print(skill_counts.most_common(20))

# creating a dataframe for skill frequency
skill_freq_df = pd.DataFrame(
    skill_counts.items(),
    columns=["Skill", "Count"]
).sort_values(by="Count", ascending=False)

print("Skill Frequency DataFrame : ")
print(skill_freq_df.head())

# saving skill frequency dataframe
skill_freq_df.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\skill_frequencies.csv", index=False)
print("Skill frequency dataframe saved successfully.")

# creating a mapping of role to skills
role_skill_map = df.groupby("Standardized_Job_Title")["extracted_skills"].sum()
print("Role to Skill Mapping : ")
print(role_skill_map.head())


# creating a dataframe for role skill mapping
role_skill_data = []

for role in df["Standardized_Job_Title"].unique():
    
    role_df = df[df["Standardized_Job_Title"] == role]
    
    role_skill = [
        skill
        for skills_list in role_df["extracted_skills"]
        for skill in skills_list
    ]

    role_skill_count = Counter(role_skill)

    for skill , count in role_skill_count.items():
        role_skill_data.append({
            "Role": role,
            "Skill": skill,
            "Count": count
        })

# creating a dataframe for role skill mapping
role_skill_df = pd.DataFrame(role_skill_data)
print("Role Skill DataFrame : ")
print(role_skill_df.head())

#Saving role skill mapping dataframe
role_skill_df.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\role_skill_mapping.csv", index=False)
print("Role skill mapping dataframe saved successfully.")


# role skill matrix
role_skill_matrix = role_skill_df.pivot_table(
    index = 'Role' , 
    columns = 'Skill' ,
    values = 'Count' , 
    fill_value = 0
)
print("Role Skill Matrix : ")
print(role_skill_matrix.head())

# saving role skill matrix
role_skill_matrix.to_csv(r"d:\Startup\Project\ai-career-coach\data\processed\role_skill_matrix.csv")
print("Role skill matrix saved successfully.")


















