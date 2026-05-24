import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Hoangyen9626!',  
    database='classicmodels'
)
cursor = conn.cursor()

sql = "DELETE FROM customers WHERE customerNumber = 1000"

cursor.execute(sql)
conn.commit()  
print("Đã xóa dữ liệu thành công")

cursor.close()
conn.close()