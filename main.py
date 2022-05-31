from flask import Flask, render_template
from datetime import datetime

### Make the flask app
app = Flask(__name__)

### Routes
@app.route("/")
def index():
    timestring = datetime.now()
    return render_template("time.html", timestring=timestring)

### Start flask
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)