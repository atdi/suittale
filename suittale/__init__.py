#!/usr/bin/env python
from flask import Flask, url_for
from flask.ext.admin.base import Admin
from flask.ext.restless.manager import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


# Import admin views after app and db instantiation
from suittale.products.admin import AdminCategoryView, AdminProductView, AdminTextureView, AdminProductImagesView, \
    AdminAttributeView, AdminSizeView
from suittale.users.admin import AdminUserView, AdminRoleView, AdminCountryView, \
    AdminRegionView, AdminCityView, AdminCustomerView


from suittale.admin import SuittaleAdminIndexView, AuthenticatedMenuLink
from flask.ext.security.datastore import SQLAlchemyUserDatastore
from suittale.users.models import User, Role
from flask.ext.security.core import Security


# Setup Flask-Security
# Initialize flask-login
def init_login(app):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    return Security(app, user_datastore)


def add_user_admin_views(admin):
    admin.add_view(AdminUserView(db.session, category='Admin'))
    admin.add_view(AdminRoleView(db.session, category='Admin'))
    admin.add_view(AdminCountryView(db.session, category='Admin'))
    admin.add_view(AdminRegionView(db.session, category='Admin'))
    admin.add_view(AdminCityView(db.session, category='Admin'))
    admin.add_view(AdminCustomerView(db.session, category='Admin'))


def add_prod_admin_views(admin):
    admin.add_view(AdminCategoryView(db.session, category='Produse'))
    admin.add_view(AdminAttributeView(db.session, category='Produse'))
    admin.add_view(AdminSizeView(db.session, category='Produse'))
    admin.add_view(AdminProductView(db.session, category='Produse'))
    admin.add_view(AdminProductImagesView(db.session, category='Produse'))
    admin.add_view(AdminTextureView(db.session, category='Produse'))


rest_manager = APIManager(app, flask_sqlalchemy_db=db)
from .views import *
from .errors import *
from suittale.products.views import *


def init_app(settings='suittale.config'):
    app.config.from_object(settings)
    db.init_app(app)
    admin = Admin(app, index_view=SuittaleAdminIndexView(), template_mode='bootstrap2')
    # Add logout link by endpoint
    admin.add_link(AuthenticatedMenuLink(name='Logout',
                                         url='/admin/logout'))
    add_user_admin_views(admin)
    add_prod_admin_views(admin)
    init_login(app)