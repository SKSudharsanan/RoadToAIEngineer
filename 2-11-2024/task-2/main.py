import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

#read csv and load data to data frame
df = pd.read_csv('data.csv')

#set data tp datetime format
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')

#1. calculate age of the people
df['age'] = df['date_of_birth'].apply(
    lambda dob: int((datetime.now().timestamp() - dob.timestamp()) / (365.25 * 24 * 60 * 60))
)

print("dataframe after adding age \n",df)

#2. basic statistics

#mean age
print("mean age is " , df['age'].mean(), "\n")

#average bmi
print("mean bmi is " , df['bmi'].mean(), "\n")

#median bmi
print("median bmi is " , df['bmi'].median(), "\n")

#bmi of smokers 
print("mean bmi of smokers is", df[df['smoker_status'] == 'Yes']['bmi'].mean(), "\n")

#bmi of non smokers 
print("mean bmi of non smokers is", df[df['smoker_status'] == 'No']['bmi'].mean(), "\n")

#average exercise time of smokers
print("average exercise time of smokers is  " , df[df['smoker_status'] == 'Yes']['avg_monthly_exercise_hours'].mean(), "\n")

#average exercise time of non-smokers
print("average exercise time of Non - smokers is " , df[df['smoker_status'] == 'No']['avg_monthly_exercise_hours'].mean(), "\n")

#average annual checkup expense of smokers
print("average exercise time of smokers is  " , df[df['smoker_status'] == 'Yes']['annual_checkup_expense'].mean(), "\n")

#average annual checkup expense of non-smokers
print("average exercise time of Non - smokers is " , df[df['smoker_status'] == 'No']['annual_checkup_expense'].mean(), "\n")


#3 Visualisations 
plt.figure(figsize=(8,6))
sns.histplot(df['bmi'], bins=10, kde=True)
plt.title('BMI Distribution of Patients')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()

#4 Exercise Hours by smoker status
plt.figure(figsize=(8,6))
sns.boxplot(x='smoker_status', y='avg_monthly_exercise_hours', data = df)
plt.title('Exercise Hours by Smoker Status')
plt.xlabel('Smoker Status')
plt.ylabel('Average Monthly Exercise Hours')
plt.show()

#5. Annual checkup expense by Gender
plt.figure(figsize=(8,6))
sns.barplot(x='gender', y='annual_checkup_expense', data = df)
plt.title('Total Annual Expense by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Checkup Expense')
plt.show()

#6.  Patient Segmentation by Age Groups
# Define age groups
bins = [0, 30, 50, 100]
labels = ['Under 30', '30-50', 'Over 50']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)


plt.figure(figsize=(8,6))
sns.barplot(x='age_group', y='bmi', data = df)
plt.title('Average BMI by Age group')
plt.xlabel('Age Group')
plt.ylabel('Average BMI')
plt.show()

