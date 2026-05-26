import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='nhy',
    password='Hoangyen9626!',
    database='classicmodels'
)

sql = """
SELECT
    c.customerNumber,
    c.customerName,
    o.orderNumber,
    o.orderDate,
    o.status
FROM customers c
INNER JOIN orders o
ON c.customerNumber = o.customerNumber
LIMIT 5;
"""

df = pd.read_sql(sql, conn)

with open("customer_orders.txt", "w", encoding="utf-8") as f:

    f.write("CUSTOMER ORDER INFORMATION\n")
    f.write("============================\n\n")

    f.write(df.to_string(index=False))

conn.close()