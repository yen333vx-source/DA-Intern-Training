import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='nhy',
    password='Hoangyen9626!',
    database='classicmodels'
)

customers = pd.read_sql("SELECT customerNumber, customerName FROM customers", conn)
payments = pd.read_sql("SELECT customerNumber, amount FROM payments", conn)

df = pd.merge(
    customers,
    payments,
    on="customerNumber",
    how="left"
)

df = df.groupby(
    ["customerNumber", "customerName"],
    as_index=False
)["amount"].sum()

df = df.rename(columns={
    "amount": "Total Payment",
    "customerNumber": "Customer Number",
    "customerName": "Customer Name"
})

df["Total Payment"] = df["Total Payment"].fillna(0)

df = df.sort_values(by="Total Payment", ascending=False).head(7)

df["Total Payment"] = df["Total Payment"].round(2)

df.to_csv(
    "pandas_total_payments.txt",
    sep="\t",
    index=False
)

conn.close()
