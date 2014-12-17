#!/usr/bin/env python
from flask.app import Flask
from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

rest_manager = APIManager(app, flask_sqlalchemy_db=db)
from .views import *
from .errors import *


def init_app(settings='suittale.config'):
    app.config.from_object(settings)
    db.init_app(app)