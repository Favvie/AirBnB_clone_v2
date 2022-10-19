#!/usr/bin/python3
"""
flask application that display html page from storage apparently
a really long moduel doc is required
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_state():
    """Prints html document with a list of states"""
    all_states = storage.all(State)
    return render_template("7-states_list.html", all_states=all_states)


@app.teardown_appcontext
def close_db(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
