# there the section 1 is (date overview)

#firslty we will check the total number of rows and columns present in the data set

import pandas as pd
df=pd.read_excel('cleaned.xlsx')
print(df)

# now for rows and columns we will use the shape function

print(f"total number of rows and columns : {df.shape}")
print(df.columns)


# now we will count the total numbers of orders or total number of revenue in data sets

# firstly we will check the total number of orders 


print(f'total number of orders : {df["Order_ID"].nunique()}')

# here we will check how many product we have

print('total products =',df['Product'].nunique())

# if we wants to know how many sales man we have in our company then we will use

print('total sales man =',df['Salesperson'].nunique())


# section 2 (REVENUE ANALYSIS)

# so now we will talk about the revenue analysis so firstly we will check the total revenue of the company

print('-----------------REVENUE ANALYSIS--------------------')
print('Total Revenue =',df['Revenue'].sum())
print('Average Revenue =',df['Revenue'].mean())
print('Maximum Revenue =',df['Revenue'].max())
print('Minimum Revenue =',df['Revenue'].min())

# section 3 (profit analysis)

# so now we will analysis the profit by abovesame 4 statemnt data

print('-----------------PROFIT ANALYSIS---------------------')
print('Total profit =',df['Profit'].sum())
print('Average profit =',df['Profit'].mean())
print('Maximum profit=',df['Profit'].max())
print('Minimum profit = ',df['Profit'].min())
# if we wants to calculate the profit percentage then we need to the

profit_percent=df['Profit'].sum()/df['Revenue'].sum()*100
print('profit percentage =',profit_percent,'%')


# section 4 product analysis

#1 here firstly we will claculate the revenue vs product
print('-----------------PRODUCT ANALYSIS--------------------')
revenue_product=df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)
print('Revenue Vs Product')
print(revenue_product)
print('Highest Revenue Product')
print(revenue_product.idxmax())
print('Lowest Revenue Product')
print(revenue_product.idxmin())
print('--------------------------------')

# now we will calculate the profit by product 

profit_product=df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
print('profit Vs product')

print(profit_product)

print('Highhest profit product')
print(profit_product.idxmax())
print('Lowest profit product')
print(profit_product.idxmin())

print('--------------------------------')


# now we will calculate the units sold by product

unit_sold=df.groupby('Product')['Units_Sold'].sum().sort_values(ascending=False)
print('Units sold vs product')
print(unit_sold)

print('Maximum 5  product that sailed most')
print(unit_sold.head())

print('Minimum 5 product that sailed least')
print(unit_sold.tail())

print('--------------------------------')


print('------------------Category Analysis--------------------')


revenue_category=df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print('Revenue Vs Category')
print(revenue_category)
print('Highest Revenue Category')
print(revenue_category.idxmax())
print('Lowest Revenue Category')
print(revenue_category.idxmin())
print('--------------------------------')

# now we will calculate the profit by product 

profit_Category=df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print('profit Vs Category')

print(profit_Category)

print('Highhest profit Category')
print(profit_Category.idxmax())
print('Lowest profit Category')
print(profit_Category.idxmin())

print('--------------------------------')


# now we will calculate the units sold by product

unit_sold=df.groupby('Category')['Units_Sold'].sum().sort_values(ascending=False)
print('Units sold vs category')
print(unit_sold)

print('Maximum 5  category that sailed most')
print(unit_sold.head())

print('Minimum 5 category that sailed least')
print(unit_sold.tail())

print('--------------------------------')


# section 6 (Country Analysis)

print('------------------Country Analysis--------------------'  )


country_revenue = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False)

print(country_revenue)

print("\nHighest Revenue Country")

print(country_revenue.idxmax())

print("\nLowest Revenue Country")

print(country_revenue.idxmin())

print('--------------------------------')
country_profit = df.groupby("Country")["Profit"].sum().sort_values(ascending=False)

print(country_profit)

print('---------------------------------')
country_units = df.groupby("Country")["Units_Sold"].sum().sort_values(ascending=False)

print(country_units)


average_country_revenue =df.groupby("Country")["Revenue"].mean()

print("\nAverage Revenue Per Country")

print(average_country_revenue)

print('---------------------Time Analysis--------------------')

df['Month']=df['Order_Date'].dt.month_name()

monthly_revenue=df.groupby('Month')['Revenue'].sum().sort_values(ascending=False)
print('Monthly Revenue')
print(monthly_revenue)

print('--------------------------------')
monthly_profit=df.groupby('Month')['Profit'].sum().sort_values(ascending=False)
print('Monthly Profit')
print(monthly_profit)
print('--------------------------------')

monthly_units=df.groupby('Month')['Units_Sold'].sum().sort_values(ascending=False)
print('Monthly Units Sold')
print(monthly_units)
print('--------------------------------')

print('Best Month')
print(monthly_revenue.idxmax())

print('Worst Month')
print(monthly_revenue.idxmin())

