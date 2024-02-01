#!/usr/bin/python3
"""Flask Script to fetch all states from database"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    all_states = storage.all(State)
    all_states = dict(sorted(all_states.items(), key=lambda x: x[1]['name']))
    return render_template('7-states_list.html', states_list=all_states)


if __name__ == "__main__":
    app.run(debug=True)
