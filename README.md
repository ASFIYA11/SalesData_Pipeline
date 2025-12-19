# 📊 Sales Data Pipeline (ETL Project)

 Project Overview
This project implements an end-to-end **ETL (Extract, Transform, Load) data pipeline** using Python, Pandas, and SQLite.  
The pipeline processes raw global sales data, cleans and transforms it, and stores the processed data in a SQL database for analysis.

---

Tech Stack
- Python
- Pandas
- SQLite
- SQL
- Matplotlib

---

Dataset
- Source: Global Sales Dataset (tab-separated CSV)
- Records processed: 357
- Columns: 16

---

 Pipeline Architecture
**Extract**
- Read raw tab-separated sales data using Pandas

**Transform**
- Standardized column names
- Removed duplicates
- Converted date columns
- Engineered features:
  - Delivery days
  - Profit margin

**Load**
- Loaded cleaned data into a SQLite database (`global_sales.db`)

---

 Key Features
- Handles non-standard tab-separated CSV files
- Real-world schema cleaning and validation
- SQL-based analysis via Python
- Data visualization using Matplotlib

---

 How to Run the Project

 Run the ETL Pipeline
```bash
python pipeline.py
Run SQL Queries & Visualization
python query_sales.py

Sample SQL Query
SELECT region, SUM(total_profit)
FROM sales
GROUP BY region
ORDER BY 2 DESC;

Insights Generated:

Regional profitability comparison

Sales performance by sales channel

Product profitability analysis

 Future Improvements:

Automate pipeline using scheduling tools

Add logging and exception handling

Integrate BI tools for dashboards



