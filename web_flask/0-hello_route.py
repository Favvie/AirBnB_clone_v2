#!/usr/bin/python3
"""
a flask module tht serves on /
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
