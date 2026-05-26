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
    SUM(p.amount) AS totalpayment
FROM customers c
LEFT JOIN payments p
ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY totalpayment DESC
LIMIT 7;
"""

df = pd.read_sql(sql, conn)

df['totalpayment'] = df['totalpayment'].fillna(0)

df = df.rename(columns={
    'customerNumber': 'Customer Number',
    'customerName': 'Customer Name',
    'totalpayment': 'Total Payment'
})

df['Total Payment'] = df['Total Payment'].round(2)

with open("customer_payments.txt", "w", encoding="utf-8") as f:

    f.write("CUSTOMER PAYMENT INFORMATION\n")
    f.write("================================\n\n")

    f.write(df.to_string(index=False))

conn.close()