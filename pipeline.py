import pandas as pd
import sqlite3

# =========================
# 1. EXTRACT (TAB-SEPARATED FIX)
# =========================
print("Reading CSV file...")
df = pd.read_csv("sales.csv", sep="\t")

print("\nOriginal columns:")
for i, col in enumerate(df.columns):
    print(i, repr(col))


# =========================
# 2. CLEAN COLUMN NAMES
# =========================
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("\nCleaned columns:")
print(list(df.columns))


# =========================
# 3. DATA CLEANING
# =========================
print("\nCleaning data...")

df = df.drop_duplicates()

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["ship_date"] = pd.to_datetime(df["ship_date"], errors="coerce")

df = df.dropna(subset=["order_date", "ship_date"])


# =========================
# 4. TRANSFORMATION
# =========================
print("\nTransforming data...")

df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days
df["profit_margin"] = (df["total_profit"] / df["total_revenue"]) * 100


# =========================
# 5. LOAD INTO SQL DATABASE
# =========================
print("\nLoading data into SQLite database...")

conn = sqlite3.connect("global_sales.db")
df.to_sql("sales", conn, if_exists="replace", index=False)
conn.close()


# =========================
# 6. FINAL CHECK
# =========================
print("\nPipeline completed successfully!")
print(df.head())
print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])
