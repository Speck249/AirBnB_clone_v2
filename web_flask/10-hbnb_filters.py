#!/usr/bin/python3
"""
Script Lists all States.
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
"""
Create new Flask app instance.
"""


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays an HTML page with filters for
    searching properties.
    """
    states= sorted(storage.all(State).values(), key=lambda state: state.name)
    cities= sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities= sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def close_storage(exception):
    """
    Remove current SQLAlchemy Session.
    """
    storage.close()


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
