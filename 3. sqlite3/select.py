# import library
import sqlite3

# create connection with local database file
con = sqlite3.connect('mydatabase.db')

# create curson object
cursor = con.cursor()

# execute query - view/ select records
cursor.execute('SELECT * FROM employees')

# fetchall records
rows = cursor.fetchall()

# print records/ row
for row in rows:
  print(row)

# close the connection
con.close()
