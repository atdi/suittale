#!/usr/bin/env python
from flask.app import Flask
from flask.ext.admin.base import Admin
from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()


# Import admin views after app and db instantiation
from suittale.products.admin import AdminCategoryView, AdminProductView, AdminTextureView
from suittale.users.admin import AdminUserView, AdminRoleView, AdminCountryView, \
    AdminRegionView, AdminCityView, AdminCustomerView


def add_user_admin_views(admin):
    admin.add_view(AdminUserView(db.session, category='Admin'))
    admin.add_view(AdminRoleView(db.session, category='Admin'))
    admin.add_view(AdminCountryView(db.session, category='Admin'))
    admin.add_view(AdminRegionView(db.session, category='Admin'))
    admin.add_view(AdminCityView(db.session, category='Admin'))
    admin.add_view(AdminCustomerView(db.session, category='Admin'))


def add_prod_admin_views(admin):
    admin.add_view(AdminCategoryView(db.session, category='Magazie'))
    admin.add_view(AdminProductView(db.session, category='Magazie'))
    admin.add_view(AdminTextureView(db.session, category='Magazie'))


rest_manager = APIManager(app, flask_sqlalchemy_db=db)
from .views import *
from .errors import *


def init_app(settings='suittale.config'):
    app.config.from_object(settings)
    db.init_app(app)
    admin = Admin(app)
    add_user_admin_views(admin)
    add_prod_admin_views(admin)