from flask import Flask, request, jsonify
from flask_cors import CORS
from psycopg2 import connect
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
	conn = connect(
            dbname="example_db",
            user="example",
            password="example",
            host="db",
            port=5432,
        )
	cursor = conn.cursor(cursor_factory=RealDictCursor)
	cursor.execute("SELECT * FROM abc limit 1;")
	rv = cursor.fetchone()
	conn.close()
	return jsonify(rv), 200
