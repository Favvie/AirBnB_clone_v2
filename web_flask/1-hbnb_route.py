#!/usr/bin/python3
"""
set up two routes
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
