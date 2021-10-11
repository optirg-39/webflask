# import library
import sqlite3

# create connection with local database file
con = sqlite3.connect("hexnbit.db")
print("Database opened successfully")

# create curson object
cursor = con.cursor()

# execute query - insert row
cursor.execute("INSERT INTO employees VALUES(1, 'Shilpa', 30000, 'HR')")

# commit
con.commit()

# close the connection
con.close()
