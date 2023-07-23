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

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display an HTML page with all State and City objects.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.py', states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    """
    Remove current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
