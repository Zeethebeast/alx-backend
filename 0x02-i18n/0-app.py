#!/usr/bin/env python3
""" flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
	""" home or root route """
	return render_template('0-index.html')


if __name__ == '__main__':
	app.run(debug=True)
