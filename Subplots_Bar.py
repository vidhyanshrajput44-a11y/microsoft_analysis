import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

# first graph we will plot between the revenue vs product

print(df.columns)
fig,axes=plt.subplots(2,2,figsize=(16,10))
plt.suptitle(" Microsoft Sales Data Analysis Dashboard", fontsize=18, fontweight="bold")
# now the title of the graph is



product_revenue=df.groupby('Product')['Revenue'].sum().sort_values(ascending = False)
axes[0,0].bar(product_revenue.index,product_revenue.values,color='Yellow')
axes[0,0].set_xlabel('Product')
axes[0,0].set_ylabel('Revenue')
axes[0,0].set_title('ANALYSING MICRSOFT SALES DATASET')
axes[0,0].legend()
plt.tight_layout()


# now the second graph will be profit vs product

profit_product=df.groupby('Product')['Profit'].sum().sort_values(ascending=False)
axes[0,1].bar(profit_product.index,profit_product.values,color='Red')
axes[0,1].set_xlabel('Product')
axes[0,1].set_ylabel('Profit')
axes[0,1].set_title('analysing micrsoft profit dataset')
axes[0,1].legend()
plt.tight_layout()



# now we will plot there the graph between the revenue vs country
revenue_country=df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

axes[1,1].bar(revenue_country.index,revenue_country.values,color='Violet')
axes[1,1].set_xlabel('Country')
axes[1,1].set_ylabel('Revenue')
axes[1,1].set_title('ANALYSING MICRSOFT COUNTRY WISE DATA')
plt.tight_layout()



# now we will plot there the graph between the profit vs country

profit_country=df.groupby('Country')['Profit'].sum().sort_values(ascending=False)
axes[1,0].bar(profit_country.index,profit_country.values,color='Green')
axes[1,0].set_xlabel('Country')
axes[1,0].set_ylabel('Profit')
axes[1,0].set_title('ANALYSING MICRSOFT COUNTRY DATA ON THE BASIS OF PROFIT')
plt.tight_layout()
plt.show()

plt.savefig("microsoft_sales_dashboard.png", dpi=300, bbox_inches="tight")
plt.show()
