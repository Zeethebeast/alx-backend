#!/usr/bin/env python3
"""
Flask app with Babel for multilingual support.

This module configures a Flask app with Babel to provide language selection
based on user preference or accepted languages from the request.
"""

from flask import g, Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask application.

    Sets supported languages, default locale, and default timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Select the best match for supported languages.

    Returns the user's locale if available; otherwise, uses the best match
    from accepted languages in the request.

    Returns:
        str: Locale string for the best language match.
    """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale  # Ensure `user.locale` is set elsewhere
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
    Render the home page template.

    Returns:
        str: Rendered HTML content for the home page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
