import psycopg2 as p
db_url = "postgres://abc:xyz@foobar.net:5432/mydb"

connection = p.connect(db_url)
cursor = connection.cursor()

cursor.execute("select * from mytable")
rows = cursor.fetchall()
print("query output: ",rows)

