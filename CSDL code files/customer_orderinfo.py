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

for row in rows:
    print(row)

cursor.close()
conn.close()