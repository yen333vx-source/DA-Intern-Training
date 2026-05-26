import pymysql

conn = pymysql.connect(
    host='localhost',
    user='nhy',
    password='Hoangyen9626!',
    database='classicmodels'
)

cursor = conn.cursor()

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

cursor.execute(sql)

rows = cursor.fetchall()

with open("customer_orders_basic.txt", "w", encoding="utf-8") as f:

    f.write("CUSTOMER ORDER INFORMATION\n")
    f.write("============================\n\n")

    for row in rows:
        f.write(str(row) + "\n")

cursor.close()
conn.close()
