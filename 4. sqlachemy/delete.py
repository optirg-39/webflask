from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, delete
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

conn = engine.connect()

# delete query
stmt = students.delete().where(students.c.id == 1)
conn.execute(stmt)

s = students.select()
conn.execute(s).fetchall()
