import mysql.connector as c

conn = c.connect(host = "localhost", user = "root", passwd = "")

mycursor = conn.cursor()

mycursor.execute("Use hexnbittest_db")

# select all
# selq = "Select * from student_table"

# select particular columnskey
# selq = "Select id,name from student_table"

# WHERE condition 
# selq = "Select id,name from student_table WHERE name = 'akash'"

# WHERE condition with AND operator
# selq = "Select * from student_table WHERE name = 'vipul' and id = 15"

# WHERE condition with or operator
# selq = "Select * from student_table WHERE name = 'akash' or group_id = 560"
# mycursor.execute(selq)

# WHERE condition with IN operator
# selq = "Select * from student_table WHERE marks IN (56, 60)"
# mycursor.execute(selq)

# WHERE condition with NOT IN operator
# selq = "Select * from student_table WHERE marks Not IN (56, 60)"
# mycursor.execute(selq)


# ORDER BY in SELECT query
# selq = "Select * from student_table ORDER by name"

# limit
# selq = "Select * from student_table LIMIT 2, 1"


# like
selq = "Select * from student_table WHERE name like 'gupta'"
mycursor.execute(selq)
result = mycursor.fetchall()
print(result)
for i in result:
    print(i)

# conn.close()