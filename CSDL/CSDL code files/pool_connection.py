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

try:
    conn = pool.connection()
    
    print("Khởi tạo Connection Pool thành công! Sẵn sàng cấp phát kết nối.")
    
    conn.close()

except Exception as e:
    print(f"Kết nối đến Connection Pool thất bại! Lỗi: {e}")
