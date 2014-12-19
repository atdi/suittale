#!/usr/bin/env python
from flask.app import Flask
from flask.ext.admin.base import Admin
from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()

from suittale.products.admin import AdminCategoryView, AdminProductView, AdminTextureView

admin = Admin(app)


def add_prod_admin_views():
    admin.add_view(AdminCategoryView(db.session))
    admin.add_view(AdminProductView(db.session))
    admin.add_view(AdminTextureView(db.session))


add_prod_admin_views()

rest_manager = APIManager(app, flask_sqlalchemy_db=db)
from .views import *
from .errors import *


def init_app(settings='suittale.config'):
    app.config.from_object(settings)
    db.init_app(app)