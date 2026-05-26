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
    e.employeeNumber,
    CONCAT(e.firstName, ' ', e.lastName) AS employeeName,
    COUNT(o.orderNumber) AS totalOrdersProcessed
FROM employees e
INNER JOIN customers c
ON e.employeeNumber = c.salesRepEmployeeNumber
INNER JOIN orders o
ON c.customerNumber = o.customerNumber
GROUP BY e.employeeNumber, e.firstName, e.lastName
ORDER BY totalOrdersProcessed DESC
LIMIT 1;
"""

df = pd.read_sql(sql, conn)


df = df.rename(columns={
    'employeeNumber': 'Employee Number',
    'employeeName': 'Employee Name',
    'totalOrdersProcessed': 'Total Orders Processed'
})


with open("employee_orders.txt", "w", encoding="utf-8") as f:

    f.write("EMPLOYEE ORDER PROCESSING INFORMATION\n")
    f.write("=======================================\n\n")

    f.write(df.to_string(index=False))

conn.close()