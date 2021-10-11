# import library
import mysql.connector as c

# create a server on local server or cloud

conn = c.connect(host="localhost", user = "root", passwd="")

# creating the cursor
mycursor = conn.cursor()

db = "hexnbittest_db"

# create database
mycursor.execute(f"Create database if not exists {db}")

# show all the databases
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)


# use the database
mycursor.execute(f"Use {db}")

# create table 
mycursor.execute("Create table if not exists student_table(id integer Primary key Auto_increment, name Text, marks Integer, group_id integer)")

# show tables
mycursor.execute("Show Tables")
print(f"tables in {db}")
for j in mycursor:
    print(j)

conn.close()