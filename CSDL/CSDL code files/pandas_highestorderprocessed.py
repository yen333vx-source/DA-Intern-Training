import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='nhy',
    password='Hoangyen9626!',
    database='classicmodels'
)

employees = pd.read_sql("""
    SELECT employeeNumber, firstName, lastName
    FROM employees
""", conn)

customers = pd.read_sql("""
    SELECT customerNumber, salesRepEmployeeNumber
    FROM customers
""", conn)

orders = pd.read_sql("""
    SELECT orderNumber, customerNumber
    FROM orders
""", conn)

emp_cust = pd.merge(
    employees,
    customers,
    left_on="employeeNumber",
    right_on="salesRepEmployeeNumber",
    how="inner"
)

df = pd.merge(
    emp_cust,
    orders,
    on="customerNumber",
    how="inner"
)

df["employeeName"] = df["firstName"] + " " + df["lastName"]

df = df.groupby(
    ["employeeNumber", "employeeName"],
    as_index=False
)["orderNumber"].count()

df = df.rename(columns={
    "employeeNumber": "Employee Number",
    "orderNumber": "Total Orders Processed"
})

df = df[[
    "Employee Number",
    "employeeName",
    "Total Orders Processed"
]]

df = df.sort_values(
    by="Total Orders Processed",
    ascending=False
).head(1)

df.to_csv(
    "pandas_highestorderprocessed.txt",
    sep="\t",
    index=False
)

conn.close()
