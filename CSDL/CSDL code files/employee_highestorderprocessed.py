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
INNER JOIN customers c 
ON e.employeeNumber = c.salesRepEmployeeNumber
INNER JOIN orders o 
ON c.customerNumber = o.customerNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
ORDER BY totalOrdersProcessed DESC
LIMIT 1;
"""

cursor.execute(sql)

rows = cursor.fetchall()

with open("employee_orders_basic.txt", "w", encoding="utf-8") as f:

    f.write("EMPLOYEE ORDER PROCESSING INFORMATION\n")
    f.write("=======================================\n\n")

    for row in rows:
        f.write(str(row) + "\n")

cursor.close()
conn.close()
