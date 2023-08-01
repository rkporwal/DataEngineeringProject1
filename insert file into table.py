import pandas
import psycopg2


data=pandas.read_csv("G:\\Learning\\Data Sets\\OfficeSupplies.csv")
#print(data.columns)

data=data.drop(['OrderDate','Unit Price','Item','Units'],axis='columns')

#print(data.columns)


def create_connection():
	#create connect to the database
	try:
		conn=psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
		print("connection created succesfully")
	except psycopg2.error as e:
		print("error : connecting to the database")
		print(e)

	# set connection autocommit to true
	conn.set_session(autocommit=True)

	curr=conn.cursor()
	return curr,conn

curr,conn=create_connection()

#create a new database
try:
	curr.execute("create database mydb;")
	print("new mydb database has been created")
except psycopg2.Error as e :
	print("error in creating a new database")
	print(e)	

def change_database():
	#connect to new database
	try:
		conn=psycopg2.connect("host=127.0.0.1 dbname=mydb user=postgres password=root")
		curr=conn.cursor()
		print("connection created succesfully")
	except psycopg2.Error as e:
		print("error : connecting to the database")
		print(e)
	return conn,curr	



curr.close()
conn.close()


conn,curr=change_database()
conn.set_session(autocommit=True)

create_table_stmt=("""create table officesupplies(
				region varchar(50)
				,rep varchar(50))""")

curr.execute(create_table_stmt)


insert_table_stmt=("""
insert into officesupplies
(
region
,rep
) values (%s,%s)
	""")


for i,row in data.iterrows():
	#print(list(row))
	curr.execute(insert_table_stmt,list(row))

curr.close()
conn.close()		