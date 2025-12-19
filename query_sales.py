import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("global_sales.db")
query = """
SELECT region, SUM(total_profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_profit DESC;
"""

df = pd.read_sql(query, conn)
print(df)
conn.close()
import matplotlib.pyplot as plt

df.plot(kind="bar", x="region", y="total_profit", legend=False)
plt.title("Total Profit by Region")
plt.show()
