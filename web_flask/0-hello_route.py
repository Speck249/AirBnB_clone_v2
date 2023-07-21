#!/usr/bin/python3
"""
Module starts web application.
"""
from flask import Flask

app = Flask(__name__)
"""
Creates new Flask app instance.
"""


@app.route('/', strict_slashes=False)
def hello():
    """ Maps root URL path '/' to hello(). """
    return ("Hello HBNB!")


if __name__ == '__main__':
    """ Starts Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
