#!/usr/bin/python3

"""Create hello route for the flask app"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBnB'


if __name__ == '__main__':
    app.run()
