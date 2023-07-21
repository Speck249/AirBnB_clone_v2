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
    """ Return string. """
    return ("HBNB!")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Return string. """
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Return string. """
    text = text.replace("_", " ")
    return ("Python {}".format(text))


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)