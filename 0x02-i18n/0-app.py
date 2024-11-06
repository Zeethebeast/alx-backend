#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)
message = "Hello World"
title = "Welcome to Holberton"

@app.route('/')
def home():
    return render_template('index.html', message=message, title=title)

if __name__ == '__main__':
    app.run(debug=True)
