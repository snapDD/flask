from email.policy import default
from config import host, user, password, database
from flask import Flask
import psycopg2 

app = Flask(__name__)

@app.route("/")
def dump_entries():
    conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
    cursor = conn.cursor()
    cursor.execute('select id, date, title, content from entries order by date')
    rows = cursor.fetchall()
    output = ""
    for r in rows:
        for el in r:
            output += str(el) + " " + "\t"
        output += "\n"
    return "<pre>" + output + "</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)