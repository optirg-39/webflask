## import library
import mysql.connector

## first crete a mysql server on your system or in cloud
## creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

## create the cursor
mycursor = conn.cursor()

## creating the database
mycursor.execute("CREATE DATABASE IF NOT EXISTS test_db")

## show the list of databases
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)

## drop the database
# mycursor.execute("DROP TABLE table_name")

## use the database
mycursor.execute("USE test_db")

## create table if not exists
mycursor.execute('CREATE TABLE IF NOT EXISTS student_table(id INTEGER PRIMARY KEY AUTO_INCREMENT,\
                name TEXT, marks INTEGER, group_id INTEGER)')

## DROP TABLE
#sql = "DROP TABLE table_name"

# show tables
mycursor.execute("SHOW TABLES")

# print the result
for x in mycursor:
    print(x)

# close the connection
conn.close()

