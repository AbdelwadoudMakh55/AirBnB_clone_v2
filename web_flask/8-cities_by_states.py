#!/usr/bin/python3
"""
This is the cities_by_state_template module
"""


from flask import Flask, render_template
from models import storage
from models.state import State


states = storage.all(State)
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def states_list():
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(error=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
