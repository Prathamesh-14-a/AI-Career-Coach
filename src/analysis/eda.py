import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"d:/Startup/Project/ai-career-coach/data/processed/jobs_with_skills.csv")

# Exlore the dataset
print(f'Dataset Preview:\n{df.head()}')
print(f'Number of Rows and Columns: {df.shape}')
print(f'\nDataset Info:\n{df.info()}')
print(f'\nDataset Description:\n{df.describe()}')
print(f'\nMissing Values:\n{df.isnull().sum()}')


#Job Role Analysis
role_count = df['Standardized_Job_Title'].value_counts()
print(f'Job Role Distribution:\n{role_count}')

#pltting bar plot for job role distribution
print('Job Role Distribution (Bar Plot) :')
plt.figure(figsize=(12,6))
role_count.plot(kind= 'bar' 
                , color= sns.color_palette('viridis', len(role_count)) ,
                edgecolor= 'black' , linewidth= 1.2)
plt.xlabel('Job Role' , fontsize= 12)
plt.ylabel('Count' , fontsize= 12)
plt.title('Top Job Role' , fontsize= 16)
plt.xticks(rotation=45)
plt.show()


#Location Analysis
location_count = df['Location'].value_counts()
print(f'Location Distribution:\n{location_count}')

#bar plot for location distribution
print('Location Distribution (Bar Plot) :')
location_count.head(10).plot(kind= 'bar'
                            , color= 'green',
                            alpha= 0.7
                            , edgecolor= 'black'
                            , linewidth= 1.2)
plt.xlabel('Location' , fontsize= 12)
plt.ylabel('Count' , fontsize= 12)
plt.title('Top Hiring Locations' , fontsize= 16)
plt.xticks(rotation=45)
plt.show()


# Experience Year Analysis
exp_counts = df['Experience_Years'].value_counts().sort_values()
print(f'Experience Year Distribution:\n{exp_counts}')

#bar plot for experience level distribution
print('Experience Year CountPlot : ')
exp_counts.plot(kind= 'barh'
                , color= 'orange',
                alpha= 0.7
                , edgecolor= 'black'
                , linewidth= 1.2)
plt.xlabel('Count' , fontsize= 12)
plt.ylabel('Experience Years' , fontsize= 12)
plt.title('Experience Required' , fontsize= 16)
plt.show()


#Salary Analysis
print(f'Salary Statistics:\n{df["salary_avg"].describe()}')

# Salary Distribution Plot
#Histogram with KDE for salary distribution
print('Salary Distribution (HistPlot) : ')
sns.histplot(df['salary_avg'].dropna(), bins=30, kde=True, color='blue')
plt.xlabel('Average Salary', fontsize=12)
plt.title('Distribution of Average Salaries', fontsize=16)
plt.show()

# Box Plot for Salary
print('Salary Box Plot: ')
df["salary_avg"].plot(kind="box")
plt.show()

#Salary by Job Role
print(f'Salary by Job Role:\n{df.groupby("Standardized_Job_Title")["salary_avg"].median()}')


# Remote vs On-site Analysis
remote_count = df[df['Location'] == 'Remote'].shape[0]
onsite_count = df[df['Location'] != 'Remote'].shape[0]
print('Count of Remote Jobs : ', remote_count)
print('Count of Onsite Jobs : ' , onsite_count)

# Distribution of Remote vs On-site jobs in percentage
print('Distribution of Remote vs On-site jobs in percentage')
labels = ['Remote', 'On-site']
sizes = [remote_count, onsite_count]
colors = ['lightblue', 'lightcoral']
plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Remote vs On-site Job Distribution', fontsize=16)
plt.show()


# Company Analysis
print('Company Distribution :')
company_count = df["Company Name"].value_counts().head(10)
print(company_count)


# Days Since Posted 
print('Days since Posted Statistics:\n ' , df["days_sinced_posted"].describe())


# Saving CSV of role_count and location_count for future use purpose
role_count.to_csv(r"d:/startup/project/ai-career-coach/data/processed/role_distribution.csv")
location_count.to_csv(r"d:/startup/project/ai-career-coach/data/processed/location_distribution.csv")
print('Datasets Saved Sucessfully !!!!')

