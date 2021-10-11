# import library
import mysql.connector

# creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

# create the cursor
mycursor = conn.cursor()

# use the database
mycursor.execute("USE test_db")

# update a record
sql = "UPDATE student_table SET marks = 80 WHERE name = 'jatin'"

mycursor.execute(sql)
# commit
conn.commit()

sql = "SELECT * FROM student_table"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

conn.close()
