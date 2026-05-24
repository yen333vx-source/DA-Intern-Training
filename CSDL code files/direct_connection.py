import pymysql

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Hoangyen9626!', 
    'database': 'classicmodels'
}

try:
    connection = pymysql.connect(**config)
    
    print("Kết nối đến MySQL thành công bằng phương thức TRUYỀN THỐNG (Direct)!")
    
    connection.close()

except Exception as e:
    print(f"Kết nối thất bại! Lỗi: {e}")
