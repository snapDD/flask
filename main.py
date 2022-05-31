from config import host, user, password, database
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    conn = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    cursor = conn.cursor()
    cursor.execute('select id, date, title, content from entries order by date')
    rowlist = cursor.fetchall()
    
    return render_template('index.html', entries=rowlist)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)