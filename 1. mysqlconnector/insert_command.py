# import library
import mysql.connector

# creating connection with credentials
conn = mysql.connector.connect(host="localhost", user="root", passwd="password")

# create the cursor
mycursor = conn.cursor()

# use the database
mycursor.execute("USE test_db")

# insert query
sql = "INSERT INTO student_table (id, name, marks, group_id) VALUES (%s, %s, %s, %s)"
val = (1, "ravi", 68, 101)
mycursor.execute(sql, val)

# commit after every updation
conn.commit()

# insert multiple rows
sql = "INSERT INTO student_table (id, name, marks, group_id) VALUES (%s, %s, %s, %s)"
val = [
  ('2', 'akash', 55, 101),
  ('3', 'jatin', 75, 102),
  ('4', 'prateek', 68, 103),
  ('5', 'sandeep', 99, 103)
    
]
mycursor.executemany(sql, val)

# commit
conn.commit()

# select query
mycursor.execute("SELECT * FROM student_table")

# to fetch all records/rows
result = mycursor.fetchall()
for i in result:
    print(i)

# to fetch only 1 record
result2 = mycursor.fetchone()
print(result2) 

conn.close()