import sqlite3
connect = sqlite3.connect("test.db") #获取test.db的连接，若无该文件，则创建一个
cursor = connect.cursor()
# '''  xxx  ''' 既是多行输入（用于变量赋值语句时），又是多行注释
sql = "select * from movieinfo where id =?"
cursor.execute(sql, '1')
resultset = cursor.fetchall()
print(resultset)
connect.commit()
cursor.close()
connect.close()