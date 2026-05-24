import pymysql
from dbutils.pooled_db import PooledDB

pool = PooledDB(
    creator=pymysql,
    maxconnections=5,       
    host='localhost',
    user='root',
    password='Hoangyen9626!',   
    database='classicmodels'
)

conn = pool.connection()
cursor = conn.cursor()

sql = "UPDATE customers SET creditLimit = 50000.00 WHERE customerNumber = 1000"

cursor.execute(sql)
conn.commit()  
print("Đã cập nhật dữ liệu thành công")

cursor.close()
conn.close()