from flask import Flask, render_template
import psycopg2
from config import host, database, user, password




app = Flask(__name__)

conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cur = conn.cursor()
file = open("schema.sql", "r")
alltext = file.read()
cur.execute(alltext)
conn.commit()
cur.execute('SELECT * FROM entries')
designer = cur.fetchone()
cur.close()
conn.close()