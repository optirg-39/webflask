# import library
import mysql.connector as c

# create connection with credentials
conn = c.connect(host = "localhost", user = "root", passwd ="")

# create the cursor
mycursor = conn.cursor()

# check show databases
# mycursor.execute("Show DATABASES")
# for i in mycursor:
#     print(i)

mycursor.execute("Use hexnbittest_db")

# mycursor.execute("Show tables")
# for i in mycursor:
#     print(i)

# mycursor.execute("DESC student_table")
# for i in mycursor:
#     print(i)

# sql = "Insert Into student_table (name, marks, group_id) Values (%s, %s, %s)"

# val = ("Aayushi gupta", 777, 66)

# mycursor.execute(sql, val)

# insert multiple rows
# sqlm = "Insert Into student_table (name, marks, group_id) Values (%s, %s, %s)"

# valm = [
#     ('akash', 56, 560),
#     ('akash goel', 57, 561),
#     ('akash ji goel', 58, 562),
#     ('akash is goel', 59, 563),
#     ('akash gupta', 60, 600)
# ]

# mycursor.executemany(sqlm, valm)

sqlm = "Insert Into student_table (name, marks, group_id) Values(%s, %s, %s)"

valm = [
    ('tarun', 56, 560),
    ('tarun goel', 57, 561),
    ('tarun ji goel', 58, 562),
    ('tarun is goel', 59, 563),
    ('tarun gupta', 60, 600)
]

mycursor.executemany(sqlm, valm)
# commit after every updation
conn.commit()

# select query
mycursor.execute("SELECT * FROM student_table")

# to fetch all records/rows
result = mycursor.fetchall()
for i in result:
    print(i)

# to fetch only 1 record
# result2 = mycursor.fetchone()
# print(result2) 

conn.close()