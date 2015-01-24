__author__ = 'aurel'

import os
import datetime
from sqlalchemy import create_engine
from flask import json
from flask.ext.testing import TestCase
from suittale.core import BaseModel
from suittale import db
from suittale.site.tests.config import basedir
from suittale.site.views import *


def init_app(settings='suittale.site.tests.config'):
    app.config.from_object(settings)
    db.init_app(app)


def create_database(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    BaseModel.metadata.create_all(bind=engine)


def add_pages():
    pass

class SiteViewsTestCase(TestCase):
    def create_app(self):
        init_app()
        return app

    def setUp(self):
        create_database(self.app)

    def tearDown(self):
        os.remove(os.path.join(basedir, 'site.db'))