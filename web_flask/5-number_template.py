#!/usr/bin/python3
"""
add default text to url
"""
from flask import Flask, render_template
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


@app.route("/number_template/<int:n>", strict_slashes=False)
def hello_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="127.0.01", port=5000)
