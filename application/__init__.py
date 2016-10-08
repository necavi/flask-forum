from flask import Flask, render_template
from flask_assets import Bundle, Environment
from flask.ext.markdown import Markdown
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


# Assets
assets = Environment(app)
assets.url = '/static'
assets.directory = app.config['ASSETS_DEST']

less = Bundle('less/style.less', filters='less', output='gen/style.css')
assets.register('all-css', less)


# Database
db = SQLAlchemy(app)
from . import models


# Admin
from . import admin


# Markdown
Markdown(app, safe_mode='escape')


# Debug toolbar
if app.config['DEBUG']:
    from flask.ext.debugtoolbar import DebugToolbarExtension as DTE
    toolbar = DTE(app)


# Security
datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, datastore)


# Endpoints
@app.route('/')
def index():
    return render_template('index.html', User=models.User)


import application.forum.views as forum
app.register_blueprint(forum.bp, url_prefix='/forum')
