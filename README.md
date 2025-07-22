# Data_Analysis_Project-1
📊 Sales Data Analysis Project
Welcome to the Sales Data Analysis repository! This project dives into a fictional retail sales dataset to uncover actionable insights by performing data cleaning, transformation, statistical analysis, and visualization using Python and popular libraries like Pandas, NumPy, and Matplotlib.

🔍 Project Overview
This project simulates real-world retail data analysis. It includes:

Data loading and preprocessing

Simulated generation of missing values (e.g., Unit_Price)

Group-wise aggregation (store, product, region)

Monthly sales trend analysis

Clear and informative visualizations

Whether you're a data science beginner or enthusiast, this project gives a hands-on experience with data exploration and business intelligence techniques.

🛠️ Tools and Libraries
Python 3

Pandas

NumPy

Matplotlib

Seaborn (optional, extendable)

📂 Dataset
The dataset used is sales_data_100.csv which includes fields such as:

Date

Product

Region

Units_Sold

Additional simulated columns include:

Unit_Price

Store

Total_Sales

Month

📈 Key Analysis Performed
✅ Conversion of date column to proper datetime format

✅ Random generation of missing Unit_Price values

✅ Addition of Store information to simulate a multi-branch setup

✅ Calculation of Total_Sales for each record

✅ Aggregated total sales by:

Store

Product

Region

Month

✅ Visualizations:

Bar chart for sales by store

Bar chart for sales by product

Pie chart for sales by region

📊 Sample Visualizations
📌 Total Sales by Store
Displays a bar chart comparing sales across Store_A, Store_B, and Store_C.

📌 Total Sales by Product
A red-colored bar chart showcasing which products generate the most revenue.

📌 Total Sales by Region
Pie chart representing regional contributions to overall sales.

🚀 How to Run
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/sales-data-analysis.git
cd sales-data-analysis
Ensure you have Python and required libraries installed:

bash
Copy
Edit
pip install pandas numpy matplotlib
Run the script:

bash
Copy
Edit
python sales_analysis.py
📁 Ensure sales_data_100.csv is in the same directory as the script.

📌 Future Enhancements
Add Seaborn for more aesthetic plots

Integrate with real-time sales dashboards (e.g., Streamlit or Power BI)

Export summary reports to Excel/PDF

💡 Learning Outcomes
Data preprocessing techniques

Handling missing/simulated data

Real-world style data aggregation

Visual storytelling through plots

📬 Feel free to fork, clone, and explore this project further! Contributions and feedback are welcome.
