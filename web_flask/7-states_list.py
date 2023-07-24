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


@app.route('/states_list', strict_slashes=False)
def state_list():
    """
    Display an HTML page with all State objects.
    """
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """
    Remove current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
