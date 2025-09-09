import sqlite3

##connect to database
connection=sqlite3.connect("student.db")

##creata a cursor object to insert records, create table, retrieve-table
cursor=connection.cursor()

##create table
table_info="""
create table student(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);"""

cursor.execute(table_info)



# Queries to INSERT records. 
cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C')''') 
  
# Display data inserted 
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
  
# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()
