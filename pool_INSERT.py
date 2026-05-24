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

sql = "INSERT INTO customers (customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) VALUES (1000,'XYZ Company','Nguyen','Hoang Yen','0987654321','30A', 'Staniforth St','Birmingham','West Midlands','B4 7DR','UK',1370,22000.00)"

cursor.execute(sql)
conn.commit()  
print("Đã thêm dữ liệu thành công")

cursor.close()
conn.close()