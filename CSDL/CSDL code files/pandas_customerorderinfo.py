import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='nhy',
    password='Hoangyen9626!',
    database='classicmodels'
)

customers = pd.read_sql("SELECT * FROM customers", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)

df = pd.merge(
    customers,
    orders,
    on="customerNumber",
    how="inner"
)

df = df[[
    "customerNumber",
    "customerName",
    "orderNumber",
    "orderDate",
    "status"
]]

df = df.sort_values(by="orderNumber")
df = df.head(5)

df.to_csv(
    "pandas_customer_orders.txt",
    sep="\t",
    index=False
)

conn.close()
