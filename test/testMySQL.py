import mysql.connector
conn = mysql.connector.connect(user='root', password='hsp', database='db01')
cursor = conn.cursor()
sql = "select * from dept"
cursor.execute(sql)
resultSet = cursor.fetchall()
print(resultSet)
conn.commit()
cursor.close()
cursor.close()

conn.close()