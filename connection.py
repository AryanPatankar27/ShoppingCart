import mysql.connector

conn=mysql.connector.connect(host='localhost',username='root',password='Test@123')
my_cursor=conn.cursor()

conn.commit()
conn.close()

print("Connection successfully")
