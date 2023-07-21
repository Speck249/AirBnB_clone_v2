#!/usr/bin/python3
"""
Module starts web application.
"""
from flask import Flask

app = Flask(__name__)
"""
Create new Flask app instance.
"""


@app.route('/', strict_slashes=False)
def hello():
    """ Return string. """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Maps URL path '/hbnb' to hbnb(). """
    return ("HBNB")


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
