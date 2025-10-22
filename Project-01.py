import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# step 1:- import data into a dataframe

df= pd.read_excel('D:\.xlsx')

# step 2 :- Group data by region and calculate reqired metries

region_starts=df.groupby('Region').agg({'sales':['sum','mean'],'Profit':['sum','mean']}),reset_index()
region_starts.colums=['Region','total sales','Average sales','Total Profit']

# Step 3:- Plotting
#Bar chart for total sales and Profit

plt.figure(figsize=(10,5))
sns.barplot(x='Region','y=Total sales',dta=region_starts,colour="blue",label="Total sales")
sns.barplot(x='Region','y=Total profit',data=region_starts,colour="orange",label="Total Profit")
plt.title("Total sales and profit by Region")
plt.legend()
plt.show()


# step 4:-Line chart for average sales and profit

plt.figaspect(figsize(10,5))
plt.plot(region_starts['Region'],region_starts['Average sales'],marker='0',label="Average sales")
plt.plot(region_starts,['Region'],region_starts['Average Profit'],marker='0',label="Average Profit")
plt.title("Average sales and profit by Region")
plt.legend()
plt.grid()
plt.show()
# step 5:-pie char for total sales by region

plt.figure(figsize=(8,8))
plt.pie(region_starts['Total sales'],label=region_starts['Region']
plt.title(" Total sales by Region")
plt.show()

# step 6:-Histogram of sales and Profit

plt.figaspect(figure=(10,5))
sns.Histogram(df['Sales']),kde=True,bins=30,colour='Orange',Label='sales'
sns.Histogram(df['Profit'],ked=True,bins=30,colour='orange',label=('Profit')

plt.show()