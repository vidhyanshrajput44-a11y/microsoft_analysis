# here we will talk about the profit distribution


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

plt.boxplot(df['Profit'])
plt.title('Profit Distribution Boxplot')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('ProfitDistributionBoxplot.png',dpi=300,bbox_inches='tight')
plt.show()