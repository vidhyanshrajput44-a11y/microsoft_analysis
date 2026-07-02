import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

# first graph we will plot between the revenue vs product

print(df.columns)

product_revenue=df.groupby('Product')['Revenue'].sum().sort_values(ascending = False)
plt.bar(product_revenue.index,product_revenue.values,color='Yellow')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.title('ANALYSING MICRSOFT SALES DATASET')
plt.tight_layout()
plt.legend()
plt.savefig("microsoft_product_revenue.png", dpi=300, bbox_inches="tight")


# now we will plot there the graph between the profit vs product

profit_product=df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
plt.bar(profit_product.index,profit_product.values,color='Red')
plt.xlabel('Product')
plt.ylabel('Profit')
plt.title('ANALYSING MICRSOFT PROFIT DATASET')
plt.tight_layout()
plt.legend()
plt.savefig("microsoft_product_profit.png", dpi=300, bbox_inches="tight")


#now we will plot there the graph between the revenue vs country   

profit_country=df.groupby('Country')['Profit'].sum().sort_values(ascending=False)
plt.bar(profit_country.index,profit_country.values,color='Green')
plt.xlabel('Country')
plt.ylabel('Profit')
plt.title('ANALYSING MICRSOFT COUNTRY DATA ON THE BASIS OF PROFIT')
plt.tight_layout()
plt.savefig("microsoft_country_profit.png", dpi=300, bbox_inches="tight")
plt.show()

#now we will plot there the graph between the revenue vs country   

revenue_country=df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
plt.bar(revenue_country.index,revenue_country.values,color='Violet')
plt.xlabel('Country')
plt.ylabel('Revenue')
plt.title('ANALYSING MICRSOFT COUNTRY WISE DATA')   
plt.tight_layout()
plt.savefig("microsoft_country_revenue.png", dpi=300, bbox_inches="tight")
plt.show()