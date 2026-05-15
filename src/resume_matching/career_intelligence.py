import pandas as pd 
from pathlib import Path

# -------------------------------------------
# DATA CONFIG 
# ------------------------------------------
BASE_PATH =  Path("d:/Startup/Project/ai-career-coach")

DATA_PATH = BASE_PATH / 'data' / 'processed'

BATCH_RESULT_DATA =  DATA_PATH / 'data_analyst_batch_results.csv'

OUTPUT_CAREER_INSIGHT = DATA_PATH / 'career_insight_output_df.csv'

CATEGORY_MAPPING = {
        "python": "Programming",
        "r": "Programming",
        "sql": "Database",
        "excel": "Spreadsheet",
        "power bi": "Visualization",
        "tableau": "Visualization",
        "dashboarding": "Visualization",
        "pandas": "Python Library",
        "numpy": "Python Library",
        "tensorflow": "Machine Learning",
        "pytorch": "Machine Learning",
        "nlm": "Machine Learning",
        "artificial intelligence": "Machine Learning",
        "statistics": "Statistics",
        "aws": "Cloud",
        "azure": "Cloud",
        "gcp": "Cloud",
        "snowflake": "Cloud",
        "big data": "Big Data",
        "spark": "Big Data",
        "dbt": "Data Engineering",
        "etl": "Data Engineering",
        "airflow": "Orchestration",
        "data preprocessing": "Data Engineering",
        "business analysis": "Business Analysis",
        "market research": "Business Analysis",
    }

# --------------------------------------------
# IMPORT DATA 
# --------------------------------------------
def data_import():
    try:
        match_df = pd.read_csv(BATCH_RESULT_DATA)
        return match_df

    except FileNotFoundError:
        print('File Not Found ... ')

    except Exception as e:
        print(f'File Loading Error {e}')

    return None

# --------------------------------------------------
# CANDIDATE PROFILE 
# --------------------------------------------------
def candidate_profile_extract(match_df):

    target_role = match_df.loc[0 , 'Role']
    match_score = match_df.loc[0 , 'Match Score %']
    matched_skills = match_df.loc[0 , 'Matched Skills']
    missing_skills = match_df.loc[0 , 'Missing Skills']
    matched_skills = [skill.strip() for skill in matched_skills.split(',')]
    missing_skills = [skill.strip() for skill in missing_skills.split(',')]

    candidate_profile = {

        "Role": target_role,

        "Match Score": match_score,

        "Matched Skills": matched_skills,

        "Missing Skills": missing_skills
    }

    return candidate_profile


# ----------------------------------------------------------
# MATCH SCORE INTERPRETATION
# ----------------------------------------------------------
# INTERPRET MATCH SCORE
def interpret_match_score(match_score):
   
    if match_score >= 80:

        return (

            "Your profile is strongly aligned "
            "with current market expectations "
            "for this role."
        )
    
    # MODERATELY ALIGNED
    elif match_score >= 60:

        return (

            "Your profile demonstrates "
            "moderate alignment with "
            "current market requirements."
        )

    # NEEDS UPSKILLING
    elif match_score >= 40:

        return (

            "Your profile shows partial "
            "alignment but requires "
            "additional upskilling."
        )
    
    # WEAK ALIGNMENT
    else:

        return (

            "Your current skill profile "
            "shows limited alignment "
            "with market expectations."
        )
    

# ====================================================
# IDENTIFY STRENGTH AREAS
# ====================================================

def identify_strength_areas( matched_skills):

    # EXTRACT CATEGORIES
    strength_categories = []

    for skill in matched_skills:
        normalized_skill = skill.lower().strip()
        category = CATEGORY_MAPPING.get(normalized_skill)
        if category:
            strength_categories.append(category)


    # REMOVE DUPLICATES
    strength_categories = sorted(set(strength_categories))

    # GENERATE DETAILED INSIGHTS

    # All three core competencies
    if (
        "Programming" in strength_categories
        and "Database" in strength_categories
        and "Visualization" in strength_categories
    ):
        return (
            "Exceptional well-rounded analytics profile with strong programming, "
            "database querying, and dashboard visualization capabilities. "
            "Positioned as a full-stack data professional ready for senior-level roles."
        )

    # Programming + Database + Cloud
    elif (
        "Programming" in strength_categories
        and "Database" in strength_categories
        and "Cloud" in strength_categories
    ):
        return (
            "Strong data engineering foundation with cloud expertise. "
            "Skilled in building scalable analytics solutions and modern data pipelines. "
            "Well-positioned for cloud data engineering roles."
        )

    # Programming + Database + Machine Learning
    elif (
        "Programming" in strength_categories
        and "Database" in strength_categories
        and "Machine Learning" in strength_categories
    ):
        return (
            "Advanced analytical skillset combining programming, database work, and ML. "
            "Capable of building predictive models and sophisticated analytics solutions. "
            "Ready for data science and advanced analytics roles."
        )

    # Programming + Database (core pair)
    elif (
        "Programming" in strength_categories
        and "Database" in strength_categories
    ):
        return (
            "Strong analytical and querying foundation. "
            "Excellent programmer with solid data management skills. "
            "Well-positioned for data analyst and junior data engineer roles."
        )

    # Programming + Visualization
    elif (
        "Programming" in strength_categories
        and "Visualization" in strength_categories
    ):
        return (
            "Strong technical foundation combining programming with visualization expertise. "
            "Capable of building automated analytics and interactive reporting solutions. "
            "Well-suited for analytics engineer and BI developer roles."
        )

    # Database + Visualization
    elif (
        "Database" in strength_categories
        and "Visualization" in strength_categories
    ):
        return (
            "Strong data querying and visualization capabilities. "
            "Excellent at transforming raw data into compelling dashboards and reports. "
            "Well-positioned for business intelligence and reporting roles."
        )

    # Programming + Cloud
    elif (
        "Programming" in strength_categories
        and "Cloud" in strength_categories
    ):
        return (
            "Strong programming skills combined with cloud platform expertise. "
            "Capable of deploying scalable analytics solutions on modern cloud infrastructure. "
            "Ready for cloud-based analytics development roles."
        )

    # Programming + Machine Learning
    elif (
        "Programming" in strength_categories
        and "Machine Learning" in strength_categories
    ):
        return (
            "Strong predictive modeling foundation anchored in solid programming. "
            "Capable of developing and deploying machine learning solutions. "
            "Well-positioned for data science and ML engineering roles."
        )

    # Just Programming
    elif "Programming" in strength_categories:
        return (
            "Strong programming skills provide excellent foundation for data roles. "
            "Ready to build specialized expertise in databases, analytics, or data science. "
            "Well-suited for entry to intermediate data engineering positions."
        )

    # Just Database
    elif "Database" in strength_categories:
        return (
            "Strong SQL and database querying skills. "
            "Excellent foundation for data analyst and BI roles. "
            "Consider adding Python or visualization skills for broader career options."
        )

    # Visualization + Cloud
    elif (
        "Visualization" in strength_categories
        and "Cloud" in strength_categories
    ):
        return (
            "Strong visualization and cloud platform expertise. "
            "Capable of building cloud-based BI solutions and dashboards. "
            "Well-positioned for cloud BI and analytics roles."
        )

    # Visualization + Machine Learning
    elif (
        "Visualization" in strength_categories
        and "Machine Learning" in strength_categories
    ):
        return (
            "Unique combination of visualization and ML skills. "
            "Excellent for communicating complex model results and building interpretable solutions. "
            "Well-positioned for ML explainability and analytics roles."
        )

    # Just Visualization
    elif "Visualization" in strength_categories:
        return (
            "Good visualization and dashboard design capabilities. "
            "Excellent at turning data into compelling stories and insights. "
            "Well-suited for BI developer and reporting analyst roles."
        )

    # Spreadsheet + Programming
    elif (
        "Spreadsheet" in strength_categories
        and "Programming" in strength_categories
    ):
        return (
            "Strong analytical skills spanning spreadsheet work and programming. "
            "Capable of automating analytics and scaling analysis workflows. "
            "Well-positioned for analytics and data engineering roles."
        )

    # Just Spreadsheet
    elif "Spreadsheet" in strength_categories:
        return (
            "Strong spreadsheet and data handling skills. "
            "Excellent foundation for tactical analysis and reporting. "
            "Consider adding SQL or Python to expand into broader data roles."
        )

    # Python Libraries with Programming
    elif (
        "Python Library" in strength_categories
        and "Programming" in strength_categories
    ):
        return (
            "Strong Python data tooling expertise for analysis and modeling. "
            "Capable of advanced data manipulation and statistical analysis. "
            "Well-positioned for data analyst and data science roles."
        )

    # Just Python Libraries
    elif "Python Library" in strength_categories:
        return (
            "Solid Python data tools foundation using pandas, numpy, and related libraries. "
            "Great for data processing and exploratory analysis. "
            "Consider adding SQL and visualization to build comprehensive analytics skills."
        )

    # Cloud expertise
    elif "Cloud" in strength_categories:
        return (
            "Familiar with cloud platforms for scalable analytics. "
            "Capable of working with modern cloud data infrastructure. "
            "Well-positioned for cloud analytics and data engineering roles."
        )

    # Big Data expertise
    elif "Big Data" in strength_categories:
        return (
            "Experience with large-scale data ecosystems and distributed computing. "
            "Capable of processing and analyzing massive datasets. "
            "Well-positioned for big data engineering and analytics roles."
        )

    # Machine Learning expertise
    elif "Machine Learning" in strength_categories:
        return (
            "Strong machine learning and AI capabilities. "
            "Experienced in building predictive models and intelligent systems. "
            "Well-positioned for data science and ML specialist roles."
        )

    # Statistics expertise
    elif "Statistics" in strength_categories:
        return (
            "Solid statistical foundations for rigorous data analysis and modeling. "
            "Excellent for hypothesis testing, forecasting, and statistical rigor. "
            "Well-positioned for analytics and data science roles."
        )

    # Data Engineering expertise
    elif "Data Engineering" in strength_categories:
        return (
            "Strong data engineering capabilities for building robust data systems. "
            "Capable of designing and implementing ETL pipelines. "
            "Well-positioned for data engineering and pipeline development roles."
        )

    # Orchestration expertise
    elif "Orchestration" in strength_categories:
        return (
            "Capable of managing complex data workflows and automation. "
            "Skilled in scheduling and orchestrating production data processes. "
            "Well-positioned for data engineering and workflow management roles."
        )

    # Business Analysis expertise
    elif "Business Analysis" in strength_categories:
        return (
            "Strong business acumen combined with data skills. "
            "Excellent at translating business needs into analytical solutions. "
            "Well-positioned for business analyst and analytics consultant roles."
        )

    # Default fallback
    else:
        return (
            "Demonstrates relevant technical foundations and "
            "is positioned to build further expertise in data analytics."
        )
    

# ====================================================
# IDENTIFY WEAKNESS AREAS
# ====================================================

def identify_weakness_areas( missing_skills):
    # CATEGORY INSIGHTS
    weakness_mapping  = {

    "Programming":
    "Your programming foundation appears limited or inconsistent, "
    "which reduces your ability to build scalable analytical workflows independently. "
    "This weakness often leads to dependency on low-code tools and restricts problem-solving depth during technical tasks. "
    "Strong programming ability is considered a baseline expectation for modern data roles, especially in automation, backend analytics, and machine learning pipelines.",

    "Statistics":
    "Your profile shows insufficient statistical depth, "
    "which weakens your ability to interpret patterns, validate models,"
    " and make data-driven decisions confidently. Without statistical reasoning, "
    "analytical outputs risk becoming descriptive rather than scientifically reliable. "
    "This gap becomes especially critical in machine learning, experimentation, forecasting, and"
    " business decision support.",

    "Machine Learning":
    "Your machine learning exposure appears underdeveloped, "
    "limiting your ability to transition from reporting-focused "
    "roles into predictive and intelligent systems development. "
    "This weakness suggests limited familiarity with model training, "
    "evaluation, feature engineering, and deployment workflows that are "
    "increasingly expected in competitive data science environments.",

    "Data Engineering":
    "Your profile indicates weak data engineering capabilities, "
    "which may affect your ability to handle real-world production "
    "data systems. Modern organizations expect professionals to work with ETL pipelines, large-scale datasets, and data infrastructure. Limited exposure here can create bottlenecks when moving from academic projects to enterprise-level analytics environments.",

    "Database":
    "Your database skills appear insufficient for efficient data extraction, "
    "transformation, and querying tasks. Weak database proficiency often leads "
    "to slower analytical workflows and limited capability in handling structured "
    "enterprise data systems. Since SQL and database concepts are core industry requirements, "
    "this gap can significantly reduce employability in analytics-related roles.",

    "Visualization":
    "Your visualization capabilities appear limited, "
    "which may reduce the clarity and business impact of your analytical findings. "
    "Data storytelling is a critical skill in decision-making environments, "
    "and weak visualization practices often prevent insights from being effectively communicated "
    "to stakeholders and leadership teams.",

    "Business Analysis":
    "Your profile suggests limited business analysis exposure,"
    "which may affect your ability to connect technical outputs with business objectives. "
    "Organizations increasingly value professionals who can translate data into actionable "
    "business decisions rather than producing isolated technical analysis without strategic context.",

    "Cloud":
    "Your cloud technology exposure appears minimal, "
    "which may limit your readiness for modern scalable data ecosystems. "
    "Many organizations now operate analytics and machine learning workflows on"
    "cloud platforms, and insufficient cloud familiarity can reduce adaptability "
    "in production-grade environments.",

    "Big Data":
    "Your profile indicates limited experience with big data technologies and "
    "distributed processing systems. This weakness may restrict your ability to "
    "work with high-volume, high-velocity datasets commonly found in enterprise environments. "
    "As organizations scale their data infrastructure, familiarity with big data ecosystems "
    "becomes increasingly valuable.",

    "Orchestration":
    "Your orchestration and workflow automation capabilities appear underdeveloped, "
    "which may affect your ability to manage scalable and reliable data pipelines. "
    "Modern data systems rely heavily on scheduling, monitoring, and dependency management tools, "
    "and lacking these skills can limit operational efficiency in production environments.",

    "Spreadsheet":
    "Your spreadsheet-related analytical skills appear limited, "
    "which may impact efficiency in quick business analysis and reporting workflows. "
    "While advanced technical tools are important, spreadsheets remain heavily used "
    "across organizations for operational analytics, ad-hoc analysis, and stakeholder collaboration.",

    "Python Library":
    "Your exposure to essential Python libraries appears insufficient for advanced analytical "
    "and machine learning workflows. Limited familiarity with industry-standard libraries may "
    "reduce productivity, code efficiency, and the ability to implement scalable analytical solutions"
    " effectively."

}

    # EXTRACT CATEGORIES
    weakness_categories = []

    # Handle both string and list inputs
    if isinstance(missing_skills, str):
        missing_skills = [skill.strip() for skill in missing_skills.split(',')]

    for skill in missing_skills:

        category = CATEGORY_MAPPING.get(skill.lower().strip())

        if category:

            weakness_categories.append(category)

    # REMOVE DUPLICATES

    weakness_categories = list(
        set(weakness_categories)
    )

    # GENERATE INSIGHTS

    weakness_insights = []

    for category in weakness_categories:

        insight = weakness_mapping.get(
            category
        )

        if insight:

            weakness_insights.append(
                insight
            )

    # FINAL OUTPUT

    if weakness_insights:

        return " ".join(weakness_insights)

    return (

        "The profile shows some missing "
        "technical capabilities that may "
        "affect market alignment."
    )


# --------------------------------------------------
# LEARNING INSIGHTS
# --------------------------------------------------
def learning_direction(missing_skills):

    learning_insight_mapping = {

        "Programming": (
            'Your learning journey should focus on building strong programming fundamentals such as functions, loops, object-oriented programming, and logical problem-solving. '
            'Consistent coding practice through projects, debugging exercises, and algorithm-based challenges will improve your analytical development capabilities. '
            'Strong programming skills are essential for automation, scalable workflows, and advanced data science applications.'
        ),

        "Statistics": (
            'You should focus on understanding core statistical concepts including probability, distributions, hypothesis testing, correlation, and statistical inference. '
            'Applying these concepts on real-world datasets will strengthen your analytical reasoning and decision-making ability. '
            'A strong statistical foundation is critical for machine learning, forecasting, experimentation, and business analytics.'
        ),

        "Machine Learning": (
            'Your learning should emphasize supervised and unsupervised learning, feature engineering, model evaluation, and optimization techniques. '
            'Building practical machine learning projects using real datasets will help you understand how models behave in real scenarios rather than only learning theory. '
            'Hands-on implementation is essential for developing strong predictive analytics capabilities.'
        ),

        "Data Engineering": (
            'Focus on learning ETL pipelines, data warehousing, distributed systems, and scalable data processing workflows. '
            'Working on projects involving automated data movement and transformation will improve your understanding of production-level data systems. '
            'Data engineering knowledge is becoming increasingly important in modern analytics and AI environments.'
        ),

        "Database": (
            'You should strengthen your database knowledge by practicing SQL queries, joins, aggregations, indexing, and query optimization techniques. '
            'Understanding how structured data is stored, managed, and retrieved efficiently is critical for analytics workflows. '
            'Strong database skills significantly improve your ability to work with enterprise-level data systems.'
        ),

        "Visualization": (
            'Your learning should focus on improving data storytelling, dashboard design, and visualization best practices. '
            'Understanding how to present insights clearly using charts, KPIs, and business-focused reporting techniques will improve communication effectiveness. '
            'Strong visualization skills help transform raw analysis into actionable business insights.'
        ),

        "Business Analysis": (
            'You should develop a stronger understanding of business problems, KPIs, decision-making frameworks, and stakeholder requirements. '
            'Learning how to align analytical findings with business objectives will improve the practical value of your analysis. '
            'Business analysis skills help bridge the gap between technical outputs and organizational impact.'
        ),

        "Cloud": (
            'Focus on learning cloud platforms such as AWS, Azure, or Google Cloud along with core concepts like storage, computing, and deployment services. '
            'Understanding cloud-based workflows will improve your readiness for scalable analytics and machine learning systems. '
            'Cloud skills are increasingly becoming standard requirements in data-focused careers.'
        ),

        "Big Data": (
            'You should explore big data technologies such as Hadoop, Spark, and distributed computing concepts to understand large-scale data processing. '
            'Working with high-volume datasets will help you learn scalability, performance optimization, and distributed system behavior. '
            'Big data expertise is valuable for enterprise-level analytics environments.'
        ),

        "Orchestration": (
            'Focus on learning workflow orchestration tools such as Airflow or Prefect to understand pipeline scheduling, monitoring, and dependency management. '
            'Building automated workflows will improve your understanding of production-grade data operations. '
            'Orchestration skills are essential for maintaining scalable and reliable data systems.'
        ),

        "Spreadsheet": (
            'Your learning should include advanced spreadsheet concepts such as pivot tables, lookup functions, data cleaning, and business reporting techniques. '
            'Spreadsheets remain heavily used across organizations for operational analysis and quick decision-making tasks. '
            'Strong spreadsheet proficiency improves both analytical efficiency and business collaboration.'
        ),

        "Python Library": (
            'Focus on mastering essential Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn through project-based learning. '
            'Understanding how these libraries interact within analytical workflows will improve your productivity and implementation quality. '
            'Strong library knowledge is critical for efficient real-world data science development.'
        ),

    }

    # EXTRACT CATEGORIES
    learning_categories = []

    # Handle both string and list inputs
    if isinstance(missing_skills, str):
        missing_skills = [skill.strip() for skill in missing_skills.split(',')]

    for skill in missing_skills:

        category = CATEGORY_MAPPING.get(skill.lower().strip())

        if category:

            learning_categories.append(category)


     # REMOVE DUPLICATES

    learning_categories = list(
        set(learning_categories)
    )

    # GENERATE INSIGHTS

    learning_insights = []

    for category in learning_categories:

        insight = learning_insight_mapping.get(
            category
        )

        if insight:

            learning_insights.append(
                insight
            )

    # FINAL OUTPUT

    if learning_insights:

        return " ".join(learning_insights)

    return (

        """Your profile shows skill gaps in areas that are important 
        for building a well-rounded analytical and technical foundation. 
        Expanding your exposure to industry-relevant tools, technologies, 
        and problem-solving practices will improve your adaptability across 
        different data roles. Continuous learning and hands-on project experience are 
        essential for strengthening overall career readiness in evolving technology environments."""
    )

# --------------------------------------------------
# GENERATE CAREER INSIGHTS
# ---------------------------------------------------
def generate_career_insights(score_interpretation , strenght_insight , 
                             weakness_insight , learning_direction):
    final_insight = (

        f"{score_interpretation}\n\n"

        f"{strenght_insight}\n\n"

        f"{weakness_insight}\n\n"

        f"{learning_direction}"
    )

    return final_insight


# -------------------------------------------------------
# SAVE CAREER INSIGHT 
# -------------------------------------------------------

def save_career_insights(candidate_profile,
                         career_insight,):
    
    career_insight_output_df = pd.DataFrame([
        {
            "Role": candidate_profile["Role"],
            "Match Score": candidate_profile["Match Score"],
            "Matched Skills": ", ".join(
                candidate_profile["Matched Skills"]
            ),
            "Missing Skills": ", ".join(
                candidate_profile["Missing Skills"]
            ),
            "Career Insight": career_insight,
        }
    ])

    career_insight_output_df.to_csv(OUTPUT_CAREER_INSIGHT,
                                    index=False)
    
    print("\n Career Insight CSV Saved Sucessfully ....")


# ----------------------------------------------------------
# MAIN PIPELINE
# ----------------------------------------------------------
def main():
    #Load DataSet
    match_df  = data_import()

    # Extract Profile
    candidate_profile = candidate_profile_extract(match_df)

    # Score Interpretation
    score_interpretation = interpret_match_score(
        candidate_profile['Match Score']
    )

    # Strenght Insight 
    strenght_insight = identify_strength_areas(
        candidate_profile['Matched Skills']
    )

    # Weakness Insight
    Weakness_insight = identify_weakness_areas(
        candidate_profile['Missing Skills']
    )

    # Learning Direction
    learning_direction_ = learning_direction(
        candidate_profile['Missing Skills']
    )

    # Career Insight
    career_insight = (
        generate_career_insights(
            score_interpretation , 
            strenght_insight , 
            Weakness_insight , 
            learning_direction_
        )
    ) 
    print('Career Insight')
    print(career_insight)

    # Save Output
    save_career_insights(candidate_profile,
                         career_insight)


# -------------------------------------------------
# RUN PIPELINE
# ------------------------------------------------
if __name__ == "__main__":
    main()
    
