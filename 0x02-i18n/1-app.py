#!/usr/bin/env python3
"""
This module sets up a simple Flask application with
internationalization support using Flask-Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class to store language settings for Flask-Babel.
    
    Attributes:
        LANGUAGES (list): Supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """
    Render the home page template.

    Returns:
        Rendered HTML template for the home page.
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based on request.

    Returns:
        str: Best matched language for the request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run(debug=True)
