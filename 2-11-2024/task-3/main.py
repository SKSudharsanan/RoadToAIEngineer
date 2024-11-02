import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

df = pd.read_csv('AmesHousing.csv')

#1. Handling Missing Values

numerical_features = df.select_dtypes(include=['float64','int64']).columns
df[numerical_features] = df[numerical_features].apply(lambda x:x.fillna(x.median()))

categorial_features = df.select_dtypes(include=['object']).columns
df[categorial_features] = df[categorial_features].apply(lambda x: x.fillna(x.mode()[0]))

#alternative_method
#df[categorial_features] = df[categorial_features].fillna("unknown")

#2. Feature Engineering

#2a. calculate Total square 

df['Total_SF'] = (
    df['Total Bsmt SF'].fillna(0) +
    df['1st Flr SF'].fillna(0) +
    df['2nd Flr SF'].fillna(0) +
    df['Low Qual Fin SF'].fillna(0) +
    df['Wood Deck SF'].fillna(0) + 
    df['Open Porch SF'].fillna(0) +
    df['Enclosed Porch'].fillna(0) +
    df['3Ssn Porch'].fillna(0) +
    df['Screen Porch'].fillna(0)
)

#2b. calculate house age

df['age'] = df['Yr Sold'] - df['Year Built']

#3. Genarating Binary Indicators for Features

df['Has Pool'] = df['Pool Area'].apply(lambda x:1 if x > 0 else 0)
df['Has Garage'] = df['Garage Area'].apply(lambda x:1 if x > 0 else 0)
df['Has Fireplace'] = df['Fireplaces'].apply(lambda x:1 if x > 0 else 0)

#4. One hot encoding for categorical Features with multiple categories
df = pd.get_dummies(df, columns=['Neighborhood', 'House Style'], drop_first=True)

## label encoding for ordinal features
if 'Overall Qual' in df.columns:
    le = LabelEncoder()
    df['Overall Qual Encoder'] = le.fit_transform(df['Overall Qual'])
    df.drop(columns=['Overall Qual'], inplace=True)

#5. Log Transformation for skewed Numerical Features
df['Log SalePrice'] = np.log1p(df['SalePrice'])
df['Log TotalSF'] = np.log1p(df['Total_SF'])

#6.Scaling Numerical Features
# option1 using minmax scaling
numerical_features = df.select_dtypes(include=['float64', 'int64']).columns
min_max_scaler = MinMaxScaler()
df[numerical_features] = min_max_scaler.fit_transform(df[numerical_features])

#option2 using standard scalar
#standard_scalar = StandardScaler()
#df[numerical_features] = standard_scalar.fit_transform(df[numerical_features])

#7. Final check on data
print("First few rows of preprocessed data")
print(df.head())

#8.save preprocessed dataset
df.to_csv('preposed_housing_data.csv',index=False)