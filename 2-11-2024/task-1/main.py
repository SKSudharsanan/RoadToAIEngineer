# importing pandas libary
import pandas as pd

#1. loading data.csv to data frame
df = pd.read_csv('data.csv')

print("Initial Data:\n", df)

print("Missing values in Data:\n", df.isnull().sum())

#2. droping values where both dob and gender is not available 
df.dropna(subset=['date_of_birth', 'gender'], inplace=True)

#3. Drop Duplicates
df = df.drop_duplicates(subset=['name','gender','date_of_birth'])

print("Data after duplicates removal:\n", df)

#3. Standarise 'gender'
df['gender'] = df['gender'].replace({'Female':'F', 'Male':'M'})

# 4. Convert 'annual_income' to numeric, forcing errors to NaN
df['annual_income'] = pd.to_numeric(df['annual_income'], errors='coerce')

# Now fill missing values in 'annual_income' with the median
median_income = df['annual_income'].median()
df['annual_income'] = df['annual_income'].fillna(median_income)

print("Data after filling annual income:\n", df)

#5. Convert 'purchase amount' to numeric, forcing errors to NaN
df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')

# Remove outliers if needed
mean_purchase = df['purchase_amount'].mean()
std_dev_purchase = df['purchase_amount'].std()
df = df[(df['purchase_amount'] < mean_purchase + 3 * std_dev_purchase) &
        (df['purchase_amount'] > mean_purchase - 3 * std_dev_purchase)]

print("Data after removing outliers:\n", df)
