#!/usr/bin/python3

"""Create hello route for the flask app"""


from flask import Flask, abort, render_template

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


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def numbers(n):
    return f"{n} is a number" if isinstance(n, int) else abort(404)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html',
                           num=n) if isinstance(n, int) else abort(404)


if __name__ == '__main__':
    app.run(debug=True)
