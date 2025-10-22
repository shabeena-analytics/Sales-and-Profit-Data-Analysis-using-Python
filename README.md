# 📊 Sales and Profit Data Analysis using Python

## 🧾 Project Overview
This project performs a simple yet powerful data analysis on sales and profit data across different regions using Python.  
It demonstrates how to process data, perform aggregations, and create visualizations using popular Python libraries such as Pandas, Matplotlib, and Seaborn.

## 🧰 Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## 📈 Features
- Import data from Excel using Pandas
- Group data by region to calculate:
  - Total and Average Sales
  - Total and Average Profit
- Generate the following visualizations:
  - **Bar Chart:** Total Sales and Profit by Region
  - **Line Chart:** Average Sales and Profit trends
  - **Pie Chart:** Sales Proportion by Region
  - **Histogram:** Distribution of Sales and Profit

## 🗂️ Dataset
Ensure your Excel file (`p.xlsx`) contains the following columns:

| Region | Sales | Profit |
|---------|--------|--------|
| East | 25000 | 3000 |
| West | 15000 | 2000 |
| South | 12000 | 1800 |
| North | 20000 | 2500 |

Save it as `p.xlsx` and place it in your `D:` drive or update the file path in the code:
```python
df = pd.read_excel(r'D:\p.xlsx')
