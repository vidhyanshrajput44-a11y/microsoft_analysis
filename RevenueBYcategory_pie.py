#revenue contribution by category 

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

revenue_category=df.groupby('Category')['Revenue'].sum()

plt.pie(revenue_category.values,labels=revenue_category.index,autopct='%1.1f%%')
plt.title('Revenue Contribution by Category')
plt.show()

plt.savefig('RevenueBYcategory_pie.png',dpi=300,bbox_inches='tight')