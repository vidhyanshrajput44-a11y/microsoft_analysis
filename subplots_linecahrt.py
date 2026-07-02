import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('cleaned.xlsx')
print(df)

# first graph we will plot between the revenue vs product

print(df.columns)
fig,axes=plt.subplots(1,2,figsize=(16,10))
plt.suptitle('Microsoft sales data analysis dashborad of profit Vs revenue ')
monthly_revenue=df.groupby(df['Order_Date'].dt.month_name())['Revenue'].sum().reindex(['January','February','March','April','May','June','July','August','September','October','November','December'])
axes[0].plot(monthly_revenue.index, monthly_revenue.values, color='Red', marker='o', linestyle='--', label='Monthly Revenue')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Revenue')
axes[0].set_title('ANALYSING MICRSOFT SALES DATASET')
axes[0].legend()
axes[0].grid()
plt.tight_layout()



# now we will work on the profit generated in a month

profit_month=df.groupby(df['Order_Date'].dt.month_name())['Profit'].sum().reindex(['January','February','March','April','May','June','July','August','September','October','November','December'])
axes[1].plot(profit_month.index, profit_month.values, color='Blue', marker='s', linestyle='-.', label='Monthly Profit')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Profit')
axes[1].set_title('ANALYSING MICRSOFT SALES DATASET')
axes[1].legend()
axes[1].grid()
plt.tight_layout()
plt.savefig('MonthlyRevenue_Profit.png',dpi=300,bbox_inches='tight')
plt.show()