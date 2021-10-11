# import library
import sqlite3

# create connection with local database file
con = sqlite3.connect("hexnbit2.db")
print("Database opened successfully")

# creating cursor object
cursor = con.cursor()

# execute query - create table
# con.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text)")
print("Table created successfully")

# list tables
cursor.execute('SELECT name from sqlite_master where type= "table"')

# # drop table
# cursor.execute('DROP table if exists employees')

# # execute query - create table if not exist
# cursor.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

# close the connection
con.close()
