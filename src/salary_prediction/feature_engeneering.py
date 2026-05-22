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
# -----------------------------------------------------
def load_data():
    try:
        df = pd.read_csv(SALARY_DATA_FILE)
        print("Data Loaded Successfully")
        print(df.shape)

        return df

    except FileNotFoundError:
        print('File Not Found')

    except Exception as e:
        print(f'File Loading Eroor : {e}')

        return None
    

#-------------------------------------------------------
# EXTRACTING TOP SKILLS 
# keeping all skills make a noisy data
# ------------------------------------------------------

def extract_top_skills(df, top_n=25):

    all_skills = []

    for row in df["Skills"]:

        skills = [
            s.strip()
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

#----------------------------------------------------
# CREATING BINARY SKILL FEATURE
#----------------------------------------------------
def create_skill_features(df, top_skills):

    for skill in top_skills:

        df[skill] = df["Skills"].apply(
            lambda x:
            1 if skill in str(x).lower()
            else 0
        )

    print("\nSkill Features Created")

    return df

#--------------------------------------------------
# REDUCE LOCATION
#-------------------------------------------------
def reduce_location_categories(df, top_n=20):

    top_locations = df["Location"] \
        .value_counts() \
        .head(top_n) \
        .index

    df["Location"] = df["Location"].apply(
        lambda x:
        x if x in top_locations
        else "Other"
    )

    return df

#----------------------------------------------
# CREATE CATEGORICAL TO NUMERIC 
# ------------------------------------------------
def encoding_categorical(df):

    categorical_columns = [
        'Job_Title' , 
        'Location'
    ]

    df = pd.get_dummies(
        df , 
        columns=categorical_columns,
        drop_first= True , 
        dtype=int
    )

    print("Encoded Categorical Features")

    return df


# -------------------------------------------------
# SPLIT
# ----------------------------------------------------
def split_features_target(df):

    X = df.drop(columns =["Salary", "Skills"] )

    y = df['Salary']

    print(f'Feature matrix shape : {X.shape}')
    print(f'Target Shape: {y.shape}')

    return X , y


# -----------------------------------------------------
# SAVE FEATURE DATASET
#  ----------------------------------------------------

def save_feature_data(df):

    df.to_csv(FEATURE_DATA, index=False)

    print("\nFeature Engineered Data Saved")


# ----------------------------------------------------
# MAIN PIPELINE
# ----------------------------------------------------
def main():
    df = load_data()
    if df is None:
        return
    
    top_skills = extract_top_skills(df)

    df = create_skill_features(df, top_skills)

    df = reduce_location_categories(df)

    df = encoding_categorical(df)

    save_feature_data(df)

    X, y = split_features_target(df)


#-------------------------------------------------------
# ENTRY POINT 
#------------------------------------------------------A
if __name__ == '__main__':
    main()






