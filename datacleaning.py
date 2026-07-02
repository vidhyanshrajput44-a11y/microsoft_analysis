import pandas as pd 
df=pd.read_excel('Microsoft_sales_Dataset_Realistic.xlsx')
print(df)
# firstly create a copy of the dataset
clean_df=df.copy()

# now we will check one more time the missing values
print(clean_df.isnull().sum())

# check duplicates values also 

print(df.duplicated().sum())

# now we have to remove the duplicate values so

clean_df=clean_df.drop_duplicates()
print(clean_df)
# for verifying uses 

print(clean_df.duplicated().sum())

# now we need to convert the date in the date fromat

clean_df['Order_Date']=pd.to_datetime(clean_df['Order_Date'],errors='coerce')
print(clean_df['Order_Date'])

# now we will check the null values again becuase we have correct the order of date

print(clean_df.isnull().sum())

# standardize the text columns

clean_df["Country"] = clean_df["Country"].str.strip()
clean_df["Region"] = clean_df["Region"].str.strip()
clean_df["Product"] = clean_df["Product"].str.strip()
clean_df["Category"] = clean_df["Category"].str.strip()
clean_df["Salesperson"] = clean_df["Salesperson"].str.strip()

# now i have to work to standarize the country names also

clean_df["Country"] = clean_df["Country"].replace({
    "usa": "USA",
    "UsA": "USA"
})

print(clean_df['Country'].unique())

# now we will work to handle the missing values 

print(clean_df.isnull().sum())

# now we need to clean the data
# firstly we will fill the values in units price

clean_df["Unit_Price"] = clean_df["Unit_Price"].fillna(
    clean_df["Unit_Price"].mean()
)

# now we will deal with the product values 

clean_df = clean_df.dropna(subset=["Product"])

# now we will deal with the category data 

category_map = {
    "Surface Laptop": "Hardware",
    "Microsoft 365": "Software",
    "Windows 11 Pro": "Software",
    "Azure Subscription": "Cloud",
    "Xbox Series X": "Gaming"
}

clean_df["Category"] = clean_df["Category"].fillna(
    clean_df["Product"].map(category_map)
)

# now we have to dill with the data as we can't predict the date so we will drop it

clean_df=clean_df.dropna(subset=['Order_Date'])

#now we will work on the missing values of sales man data basically its data is very large and contain very high value so 
# there we can't delete that missing values so we will fill there unknowns

clean_df["Salesperson"]=clean_df["Salesperson"].fillna('Unknown')

print(clean_df.isnull().sum())

clean_df.to_excel("Microsoft_Sales_Cleaned.xlsx", index=False)
