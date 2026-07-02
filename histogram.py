# now we will revenue contribution using histogram by businesss

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

plt.hist(df['Revenue'],bins=20,color='Violet')
plt.title('Revenue Distribution Histogram')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('RevenueDistributionHistogram.png',dpi=300,bbox_inches='tight')
plt.show()