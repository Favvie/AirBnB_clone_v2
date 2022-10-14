#!/usr/bin/python3
"""
display n if only it is a number
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return 'Hello HBNB'


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_text(text):
    return "C %s" % text.replace("_", " ")


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>')
def hello_default(text):
    return "Python %s" % text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def hello_int(n):
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="127.0.01", port=5000)