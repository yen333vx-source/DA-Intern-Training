import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Hoangyen9626!',  
    database='classicmodels'
)
cursor = conn.cursor()

sql = "UPDATE customers SET creditLimit = 50000.00 WHERE customerNumber = 1000"

cursor.execute(sql)
conn.commit()  
print("Đã cập nhật dữ liệu thành công")

cursor.close()
conn.close()
