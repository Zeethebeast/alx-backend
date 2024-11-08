#!/usr/bin/env/ python3
""" flask app"""
from flask import Flask, render_templates


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
	pass
