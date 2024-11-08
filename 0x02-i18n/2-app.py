#!/usr/bin/env python3
from flask import g, Flask, render_template, request
from flask_babel import Babel

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale  # Ensure `user.locale` is set elsewhere
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def home():
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)
