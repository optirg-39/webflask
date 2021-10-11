# import library
import mysql.connector

# creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

# create the cursor
mycursor = conn.cursor()

# use the database
mycursor.execute("USE test_db")

# select particular columnskey
mycursor.execute("SELECT id, name FROM student_table")

result = mycursor.fetchall()
for i in result:
    print(i)

# WHERE condition in SELECT query
sql = "SELECT * FROM student_table WHERE name ='ravi'"
mycursor.execute(sql)

result = mycursor.fetchall()
for i in result:
    print(i)

# WHERE condition with AND operator
sql = "SELECT * FROM student_table WHERE name = 'akash' AND group_id = 101"

mycursor.execute(sql)

result = mycursor.fetchall()
for i in result:
    print(i)

## WHERE condition with OR operator
# sql1= "SELECT * FROM student_table WHERE name = 'akash' OR 'marks' = 60"

## WHERE condition with IN operator
# sql2 = "SELECT * FROM student_table WHERE group_id IN (101, 102)"

## WHERE condition with NOT IN operator
# sql3 = "SELECT * FROM student_table WHERE group_id NOT IN (101)"

# ORDER BY in SELECT query
sql = "SELECT * FROM student_table ORDER BY name"
mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)

conn.close()
