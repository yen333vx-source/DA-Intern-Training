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
    SUM(p.amount) AS totalpayment
FROM customers c
LEFT JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY totalpayment DESC
LIMIT 7;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
