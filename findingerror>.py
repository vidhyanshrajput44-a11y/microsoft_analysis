import pandas as pd 
df=pd.read_excel('Microsoft_sales_Dataset_Realistic.xlsx')
print(df)
# checking for null values how many null values are present in it
f=df.isnull().sum()
print(f)

# now we have to check for the duplicate values we have already find out how many null values does we have

print(df.duplicated().sum())

# it provides there are 150 duplicate data values in the excel sheet 

print(df['Country'].unique())

# also we can use it with the product value

print(df['Product'].unique())

