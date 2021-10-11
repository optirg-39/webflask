# import library
import mysql.connector

# creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

# create the cursor
mycursor = conn.cursor()

# use the database
mycursor.execute("USE test_db")

# delete a record
sql = "DELETE FROM grades_table WHERE student_id = 1"

mycursor.execute(sql)

# commit
conn.commit()

# SELECT query
sql = "SELECT * FROM grades_table"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
conn.close()
