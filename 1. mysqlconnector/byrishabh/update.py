import mysql.connector as c
conn = c.connect(host = "localhost", user = "root", passwd = "")

mycursor = conn.cursor()
mycursor.execute("Use hexnbittest_db")

# update a record 
sql = "UPDATE student_table SET marks = 99 WHERE name = 'akash'"

mycursor.execute(sql)
conn.commit()
mycursor.execute("SELECT * from student_table")

result = mycursor.fetchall()
for i in result:
    print(i)