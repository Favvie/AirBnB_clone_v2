#!/usr/bin/python3
"""
route with variable text
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    return "C %s" % text.replace("_"," ")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
