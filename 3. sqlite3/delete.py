# import library
import sqlite3

# create connection with local database file
con = sqlite3.connect("hexnbit.db")
print("Database opened successfully")

# create curson object
cursor = con.cursor()

# execute query - delete row
cursor.execute('DELETE FROM employees where id = 1')

# commit
con.commit()

# close the connection
con.close()
