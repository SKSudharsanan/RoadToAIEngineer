# New Use Case: Patient Health Analysis

## Scenario
Imagine you’re working with a healthcare provider to analyze patient data. The goal is to explore demographics, health metrics, and lifestyle factors to identify trends and potential risk factors.

## Dataset Description
Here’s a synthetic dataset of patients that you can use for this task. Each row represents a patient with various attributes:

- **patient_id**: Unique identifier for each patient.
- **name**: Patient's name.
- **date_of_birth**: Patient’s date of birth.
- **gender**: Patient’s gender.
- **bmi**: Body Mass Index.
- **smoker_status**: Whether the patient is a smoker.
- **avg_monthly_exercise_hours**: Average hours of exercise per month.
- **annual_checkup_expense**: Annual expense on healthcare checkups.

## Sample Data (`patients.csv`)

```csv
patient_id,name,date_of_birth,gender,bmi,smoker_status,avg_monthly_exercise_hours,annual_checkup_expense
1,John Doe,1985-05-15,M,27.5,Yes,12,1500
2,Jane Smith,1990-08-22,F,22.1,No,20,1200
3,Bob Johnson,1978-12-01,M,30.2,Yes,8,1800
4,Emily Davis,1992-03-11,F,24.0,No,15,1100
5,Michael Brown,1987-09-07,M,26.5,Yes,10,1600
6,Sarah Wilson,1985-04-25,F,23.5,No,25,1300
7,David Lee,1995-01-10,M,28.0,Yes,5,1700
8,Amy Garcia,1989-07-30,F,21.0,No,30,1000
9,Chris Martinez,1976-10-20,M,29.0,Yes,7,1900
10,Jessica White,1993-06-15,F,22.8,No,18,1150
```

## Task: Exploratory Data Analysis (EDA) and Visualization on Patient Data

### Goals

#### 1. Analyze Health Metrics
- Calculate the average and median BMI of patients.
- Compare BMI between smokers and non-smokers.

#### 2. Visualization of Key Health Trends
- Visualize the distribution of BMI.
- Compare exercise hours between smokers and non-smokers.
- Analyze healthcare expenses by gender.

#### 3. Patient Segmentation
- Segment patients by age group (e.g., under 30, 30-50, over 50) and analyze their BMI and exercise habits.

