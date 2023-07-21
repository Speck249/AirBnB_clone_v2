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
    """ Maps root URL path '/' to hello(). """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Maps URL path '/hbnb' to hbnb(). """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Maps URL path '/c/<text>' to c_text(). """
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python/', defaults={'text': 'is cool'},
           strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Maps URL path '/python/<text>' to python_text(). """
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Maps URL path '/number/<n>' to number(). """
    return ("{} is a number".format(n))


if __name__ == '__main__':
    """ Start Flask dev server. """
    app.run(host='0.0.0.0', port=5000)
