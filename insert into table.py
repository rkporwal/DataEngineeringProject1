#import library
import psycopg2

# #Create connection to the database
# try:
# 	conn=psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
# except psycopg2.Error as e:
# 	print("coould not make connection to the postgres database")
# 	print(e)	

# #Use the connection to get the cursor that can be used to execute quiries
# try:
# 	cur=conn.cursor()
# except psycopg2.Error as e:
# 	print("could not get cursor to the Database")
# 	print(e)

# # set autocommit to be true so that each action is commi conn.commit() after each command
# conn.set_session(autocommit=True)

# #Create a database to do the work in 
# try:
# 	cur.execute("create database myfirstdb")
# except psycopg2.Error as e:
# 	print("could not create databases")
# 	print (e)

# #Add database name in the connect statement, Lets close database,reconnect and get a new cursor
# try:
# 	conn.close()
# except psycopg2.Error as e:
# 	print(e)

try:
	conn=psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password=root")
except psycopg2.Error as e:
	print("coould not make connection to the postgres database")
	print(e)	

try:
	cur=conn.cursor()
except psycopg2.Error as e:
	print("could not get cursor to the Database")
	print(e)

conn.set_session(autocommit=True)		

# create a table for student which includes below columns
	# student_id
	# name
	# age
	# gender
	# subject
	# marks
try:
	cur.execute("CREATE TABLE IF NOT EXISTS students(student_id int,name varchar,\
		age int,gender varchar,subject varchar,marks int);")
except psycopg2.Error as e:
	print("Error : Issue creating table")
	print(e)

#Insert the following two rows in the table
	# First row : 1, "Alex",25,male,physics,92
	# Second row : 2. "Sara",18,female,english,85
try:
	cur.execute("INSERT INTO students(student_id,name,age,gender,subject,marks)\
		values(%s,%s,%s,%s,%s,%s)",\
		(1,"Alex",25,"male","physics",92))
except psycopg2.Error as e:
	print("Error : inserting rows")
	print(e)

try:
	cur.execute("INSERT INTO students(student_id,name,age,gender,subject,marks)\
		values(%s,%s,%s,%s,%s,%s)",\
		(1,"Sara",18,"female","english",85))
except psycopg2.Error as e:
	print("Error : inserting rows")
	print(e)


#Validate your data was inserted in the table
try:
	cur.execute("SELECT * FROM 	students;")
except psycopg2.Error as e:
	print("Error : select *")
	print(e)

row=cur.fetchone()
while row:
	print(row)
	row=cur.fetchone()

# And finally close your connection
cur.close()
conn.close()
