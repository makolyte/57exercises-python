from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/time/JSON")
def time():
    now = str(datetime.now())
    return jsonify({"currentTime":now})

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)
