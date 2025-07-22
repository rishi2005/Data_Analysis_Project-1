import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#step 1 load the dataset
df = pd.read_csv('sales_data_100.csv')
print(df.head())
print("original data set: ")
print(df.head())

#step 2 convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'])


#Need to add Random Unit Price (missing value)
#col -- simulated
np.random.seed(42)
df['Unit_Price'] = np.random.randint(10000, 60000,size=len(df))

#add random store col into the dataset
stores = ['Store_A', 'Store_B', 'Store_C']
df['Store'] = np.random.choice(stores, size=len(df))

#create a 'Total_sales' column
df['Total_Sales'] = df['Units_Sold'] * df['Unit_Price']

#data info
print("\n Data info: ")
print(df.info())

#Data summary
print('\n Summary Statistics:')
print(df.describe())

#Total Sales by Store
sales_by_store = df.groupby('Store')['Total_Sales'].sum().sort_values(ascending=False)
print('\n Total Sales by Store:')
print(sales_by_store)

#total sales by product
sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
print(sales_by_product)

#total sales by region
sales_by_region = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print(sales_by_region)

#Monthly sales 
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Total_Sales'].sum().sort_values(ascending=False)
print('\n Monthly Sales:')
print(monthly_sales)

#Sales by store
plt.figure(figsize=(8,9))
sales_by_store.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Store')
plt.xlabel('Store')
plt.ylabel(' Sales(in $)')
plt.grid(True)
plt.tight_layout()
plt.show()


#2nd plot
plt.figure(figsize=(8,5))
sales_by_product.plot(kind='bar', color='red')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales(in $)')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8,9))
sales_by_region.plot(kind='pie', autopct='%1.1f%%')
plt.title('Total Sales by Region')
plt.tight_layout()
plt.show()


