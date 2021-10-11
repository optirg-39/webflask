import mysql.connector as c
conn = c.connect(host = "localhost", user = "root", passwd = "")
mycursor = conn.cursor()
mycursor.execute("Use hexnbittest_db")
mycursor.execute("Delete From student_table Where id = 15")
mycursor.execute("SELECT * FRom student_table")
result = mycursor.fetchall()
for i in result:
    print(i)