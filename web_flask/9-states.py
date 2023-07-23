#!/usr/bin/python3
"""
Script Lists all States.
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
"""
Create new Flask app instance.
"""

@app.route('/states', strict_slashes=False)
def states():
    """
    Display an HTML page with all State objects.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities():
    """
    Display an HTML page with City objects of a State.
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', state=None, cities=None)


@app.teardown_appcontext
def close_storage(exception):
    """
    Remove current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
