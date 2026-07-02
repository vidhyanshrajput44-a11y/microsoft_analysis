import pandas as pd 
df=pd.read_excel('Microsoft_sales_Dataset_Realistic.xlsx')
print(df)
print(df.head())
print(df.tail())
# firstly we will check their how many data sets are present there
print(df.info())

# for the discriptive data we will use there the descirbe function

print('Descriptive Data')
print(df.describe())
print(df.columns)


