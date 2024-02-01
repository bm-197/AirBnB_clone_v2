#!/usr/bin/python3

"""
starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
states = dict(sorted(storage.all(State).items(), key=lambda x: x[1]['name']))
cities = dict(sorted(storage.all(City).items(), key=lambda x: x[1]['name']))


@app.teardown_appcontext
def teardown_db(exception):
    """Close database connection after the request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Fetch all states """
    return render_template('7-states_list.html', states_list=states)


@app.route("/cities_by_states", strict_slashes=False)
def citiesByStates():
    """Fetch all cities by their states"""
    return render_template('8-cities_by_states.html', states_list=states,
                           cities_list=cities)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
