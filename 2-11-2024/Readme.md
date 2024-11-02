I was down for a week because of a viral fever and couldn't do anything. I am still not 100% recovered but have started learning again.

One thing I really loved about Andrew Ng's basic Python course is the use of ChatGPT as an assistant. Inspired by this, I decided to create my own GPT called Sam to assist me in this journey.

The purpose of Sam is to streamline my tasks and guide me step-by-step from scratch to becoming an AI engineer. Once I gain complete confidence, I will be open-sourcing Sam so that it can become everyone's tutor in becoming an AI engineer.

So, now here is the first task given to me by Sam:

**Task: Data Cleaning and Preparation for Customer Analysis**

**Scenario**

You are an AI engineer tasked with preparing customer data for analysis. The dataset contains issues like missing values, duplicates, inconsistent entries, and outliers. Your goal is to clean the data so it's ready for deeper analysis and visualization.

**Steps**

1. **Load and Inspect the Data**
   - Load the data into a Pandas DataFrame.
   - Inspect it to understand the structure and identify any issues.

2. **Identify Missing Values**
   - Check for missing values in each column.
   - Decide how to handle these missing values, particularly for critical columns like `annual_income`.

3. **Remove Duplicates**
   - Identify and remove any duplicate entries.

4. **Standardize the Gender Column**
   - Ensure the `gender` column has consistent values ('M' for male and 'F' for female).

5. **Handle Outliers**
   - For `purchase_amount`, consider limiting values to within three standard deviations of the mean to remove outliers.

6. **Output the Cleaned Data**
   - After cleaning, print a summary of the cleaned data to verify each issue has been addressed.

**Sample Data (customers_with_issues.csv)**

Copy this data into a CSV file named `customers_with_issues.csv` for your task:

```
customer_id,name,date_of_birth,gender,annual_income,purchase_amount
1,John Doe,1985-05-15,M,75000,200
2,Jane Smith,1990-08-22,F,82000,350
3,Bob Johnson,1978-12-01,M,54000,120
4,Emily Davis,1992-03-11,F,68000,500
5,Michael Brown,,95000,450
6,Sarah Wilson,1985-04-25,Female,78000,300
7,David Lee,1995-01-10,M,61000,
8,Amy Garcia,1989-07-30,F,92000,400
9,Chris Martinez,1976-10-20,Male,88000,600
10,Jessica White,1993-06-15,F,67000,240
11,Jessica White,1993-06-15,F,67000,240  # Duplicate row
12,Alex Green,1985-05-25,Male,,1000      # Missing income and unusually high purchase amount
```

