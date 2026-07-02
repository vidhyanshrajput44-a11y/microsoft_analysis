# which product solds the highest unit of items
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

product_sales=df.groupby('Product')['Units_Sold'].sum().sort_values(ascending=False)
plt.bar(product_sales.index,product_sales.values,color='Orange',label='2026 MICROSOFT PRODUCT SALES')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.title('Top Selling Products')
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.savefig('TopSellingProducts.png',dpi=300,bbox_inches='tight')
plt.show()
