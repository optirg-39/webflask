# import library
import mysql.connector

# creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

# create the cursor
mycursor = conn.cursor()

# use the database
mycursor.execute("USE test_db")

# join two tables (INNER JOIN or JOIN)
# bedore this you have to create 1 extra tables with 1 common column
sql = "SELECT student_table.name AS name, grades_table.grade AS grade FROM student_table \
    INNER JOIN grades_table ON student_table.id = grades_table.student_id"
mycursor.execute(sql)

result = mycursor.fetchall()
# print the records
for x in result:
    print(x)

# join two tables (LEFT JOIN)
# bedore this you have to create 1 extra tables with 1 common column
sql = "SELECT student_table.name AS name, grades_table.grade AS grade FROM student_table \
    LEFT JOIN grades_table ON student_table.id = grades_table.student_id"
mycursor.execute(sql)

result = mycursor.fetchall()
# print the records
for x in result:
    print(x)

# join two tables (RIGHT JOIN)
# bedore this you have to create 1 extra tables with 1 common column
sql = "SELECT student_table.name AS name, grades_table.grade AS grade FROM student_table \
    RIGHT JOIN grades_table ON student_table.id = grades_table.student_id"
mycursor.execute(sql)

result = mycursor.fetchall()
# print the records
for x in result:
    print(x)

conn.close()