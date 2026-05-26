import pandas as pd
from pathlib import Path
from collections import Counter

#------------------------------------------------------
# PATH
#-----------------------------------------------------

BASE_PATH = Path("d:/Startup/Project/ai-career-coach")

DATA_PATH = BASE_PATH / 'data' / 'Salary Prediction Data'

SALARY_DATA_FILE = DATA_PATH / 'salary_preprocessed_data.csv'

FEATURE_DATA = DATA_PATH / "salary_feature_data.csv"


#------------------------------------------------------
# LOAD DATA
#------------------------------------------------------
def load_data():
    try:
        df = pd.read_csv(SALARY_DATA_FILE)
        print("Data Loaded Successfully")
        print(df.shape)

        return df

    except FileNotFoundError:
        print('File Not Found')

    except Exception as e:
        print(f'File Loading Error : {e}')

    return None


#------------------------------------------------------
# EXTRACT TOP SKILLS
#------------------------------------------------------
def extract_top_skills(df, top_n=25):

    all_skills = []

    for row in df["Skills"]:

        skills = [
            s.strip().lower()
            for s in str(row).split(",")
            if s.strip()
        ]

        all_skills.extend(skills)

    skill_counts = Counter(all_skills)

    top_skills = [
        skill
        for skill, count
        in skill_counts.most_common(top_n)
    ]

    print("\nTop Skills:")
    print(top_skills)

    return top_skills


#------------------------------------------------------
# CREATE BINARY SKILL FEATURES
#------------------------------------------------------
def create_skill_features(df, top_skills):

    for skill in top_skills:

        df[skill] = df["Skills"].apply(
            lambda x: 1 if skill in str(x).lower() else 0
        )

    print("\nSkill Features Created")

    return df


#------------------------------------------------------
# REDUCE LOCATION
#------------------------------------------------------
def reduce_location_categories(df, top_n=20):

    top_locations = df["Location"].value_counts().head(top_n).index

    df["Location"] = df["Location"].apply(
        lambda x: x if x in top_locations else "Other"
    )

    return df


#------------------------------------------------------
# EXTRA FEATURES
#------------------------------------------------------
def create_skill_count_feature(df):

    df["Skill_Count"] = df["Skills"].apply(
        lambda x: len([
            s for s in str(x).split(",")
            if s.strip()
        ])
    )

    print("\nSkill Count Feature Created")

    return df

#------------------------------------------------------
# PREMIUM SKILL COUNT
#------------------------------------------------------
def create_premium_skill_count(df):

    premium_skills = [
        "aws",
        "spark",
        "hadoop",
        "deep learning",
        "machine learning",
        "natural language processing"
    ]

    available_skills = [
        skill for skill in premium_skills
        if skill in df.columns
    ]

    df["Premium_Skill_Count"] = df[available_skills].sum(axis=1)

    print("\nPremium Skill Count Created")

    return df

#------------------------------------------------------
# EXPERIENCE × SKILL INTERACTION
#------------------------------------------------------
def create_experience_skill_interaction(df):

    df["Exp_X_SkillCount"] = (
        df["Experience"] * df["Skill_Count"]
    )

    print("\nExperience-Skill Interaction Created")

    return df

#------------------------------------------------------
# REMOTE × EXPERIENCE INTERACTION
#------------------------------------------------------
def create_remote_experience_feature(df):

    df["Remote_Experience"] = (
        df["remote_status"] * df["Experience"]
    )

    print("\nRemote Experience Feature Created")

    return df



def bucket_experience(exp):
    if exp <= 2:
        return "Entry"
    elif exp <= 5:
        return "Mid"
    elif exp <= 8:
        return "Senior"
    else:
        return "Lead"




def apply_experience_bucket(df):

    df["Experience_Level"] = df["Experience"].apply(bucket_experience)

    print("\nExperience Bucketed")

    return df




#------------------------------------------------------
# ENCODE CATEGORICAL FEATURES
#------------------------------------------------------
def encoding_categorical(df):

    categorical_columns = [
        'Job_Title',
        'Location',
        'Experience_Level'
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_columns,
        drop_first=True,
        dtype=int
    )

    print("\nEncoded Categorical Features")

    return df


#------------------------------------------------------
# SPLIT FEATURES + TARGET
#------------------------------------------------------
def split_features_target(df):

    X = df.drop(columns=["Salary", "Skills"])
    y = df["Salary"]

    print(f'\nFeature matrix shape : {X.shape}')
    print(f'Target Shape: {y.shape}')

    return X, y


#------------------------------------------------------
# SAVE FEATURE DATASET
#------------------------------------------------------
def save_feature_data(df):

    df.to_csv(FEATURE_DATA, index=False)

    print("\nFeature Engineered Data Saved")


#------------------------------------------------------
# MAIN PIPELINE
#------------------------------------------------------
def main():

    df = load_data()

    if df is None:
        return

    top_skills = extract_top_skills(df)

    df = create_skill_features(df, top_skills)

    df = reduce_location_categories(df)

    df = create_skill_count_feature(df)

    df = create_premium_skill_count(df)

    df = create_experience_skill_interaction(df)

    df = create_remote_experience_feature(df)

    df = apply_experience_bucket(df)

    print(df["Experience_Level"].value_counts())

    df = encoding_categorical(df)

    save_feature_data(df)

    X, y = split_features_target(df)

    print(df.columns)


#------------------------------------------------------
# ENTRY POINT
#------------------------------------------------------
if __name__ == '__main__':
    main()