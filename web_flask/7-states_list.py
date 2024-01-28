#!/usr/bin/python3
"""
This is the number_template module
"""


from flask import Flask, render_template
from models import storage
from models.state import State


states = storage.all(State)
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """ Return the list of states """
    states_A_Z = sorted(list(states.values()), key=lambda att: att.name)
    return render_template("7-states_list.html", states=states_A_Z)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Closes the storage """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
