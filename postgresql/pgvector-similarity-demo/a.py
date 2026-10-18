from psycopg2 import connect
conn = connect(database="pgv_db", user="pgv", password="pgv", port=5432, host="localhost")
cursor = conn.cursor()

