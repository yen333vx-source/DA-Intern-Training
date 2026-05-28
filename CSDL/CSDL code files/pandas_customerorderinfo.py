import pymysql
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="nhy",
    password="Hoangyen9626!",
    database="classicmodels"
)

customers = pd.read_sql("SELECT customerNumber, customerName FROM customers", conn)

orders = pd.read_sql(
    "SELECT orderNumber, customerNumber, orderDate, status FROM orders", conn)

df = pd.merge(
    customers,
    orders,
    on="customerNumber",
    how="inner"
)

df = df.sort_values(by="orderNumber").head(5)

df.to_csv(
    "pandas_customer_orders.txt",
    sep="\t",
    index=False
)

conn.close()
