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
    e.employeeNumber,
    CONCAT(e.firstName, ' ', e.lastName) AS employeeName,
    COUNT(o.orderNumber) AS totalordersprocessed
FROM employees e
INNER JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
INNER JOIN orders o ON c.customerNumber = o.customerNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
ORDER BY totalOrdersProcessed DESC
LIMIT 1;
"""

cursor.execute(sql)

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()