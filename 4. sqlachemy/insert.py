from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

# create table
students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)
# create connection
conn = engine.connect()

# insert query
stmt = students.insert().values(name = 'Ravi', lastname = 'Kapoor')

# execute query
result = conn.execute(stmt)
