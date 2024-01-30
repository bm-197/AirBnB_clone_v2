#!/usr/bin/python3

"""Create hello route for the flask app"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run()
