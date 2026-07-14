import os
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# ==========================================
# 1. EXTRACT (TAB-SEPARATED COMPILATION)
# ==========================================
print("Reading raw CSV database source...")
df = pd.read_csv("sales.csv", sep="\t")

print("\nOriginal source columns detected:")
for i, col in enumerate(df.columns):
    print(i, repr(col))

# ==========================================
# 2. STANDARDIZE COLUMN SCHEMAS
# ==========================================
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("\nStandardized engine columns:")
print(list(df.columns))

# ==========================================
# 3. DATA CLEANING & SANITIZATION
# ==========================================
print("\nExecuting data cleaning procedures...")

# Purge duplicate entries
df = df.drop_duplicates()

# Standardize date types and drop records with corrupted timeline variables
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")
df = df.dropna(subset=["order_date", "ship_date"])

# ==========================================
# 4. TRANSFORMATION & CALCULATED FIELDS
# ==========================================
print("\nProcessing analytical transformations...")

# Compute processing intervals and aggregate profit ratios
df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days
df["profit_margin"] = (df["total_profit"] / df["total_revenue"]) * 100

# ==========================================
# 5. LOAD INTO TARGET ASSETS
# ==========================================
print("\nLoading parsed entries into physical storage layers...")

# Transaction 1: Commit data to relational SQLite database
conn = sqlite3.connect("global_sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()

# Transaction 2: Export flattened CSV schema matrix optimized for Power BI Desktop
df.to_csv("cleaned_global_sales.csv", index=False)

# ==========================================
# 6. PIPELINE DIAGNOSTIC VERIFICATION
# ==========================================
print("\nPipeline execution sequence completed successfully!")
print(df.head())
print("\nTotal Records Documented:", df.shape[0])
print("Total Features Evaluated:", df.shape[1])

# ==========================================
# 7. METRIC QUERYING & LOCAL VISUALIZATION
# ==========================================
print("\nExecuting relational diagnostic queries...")
conn = sqlite3.connect("global_sales.db")
query = """
SELECT region, SUM(total_profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC;
"""
df_metrics = pd.read_sql(query, conn)
print(df_metrics)
conn.close()

# Generate local validation plot configuration
df_metrics.plot(kind="bar", x="region", y="total_profit", legend=False)
plt.title("Total Profit by Region")
plt.tight_layout()
plt.show()
