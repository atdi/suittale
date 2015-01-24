__author__ = 'aurel'

import os
from sqlalchemy import create_engine
from flask import json
from flask.ext.testing import TestCase
from suittale.site.tests.config import basedir
from suittale.site.views import *
from suittale.site.models import *


def init_app(settings='suittale.site.tests.config'):
    app.config.from_object(settings)
    db.init_app(app)


def create_database(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    BaseModel.metadata.create_all(bind=engine)


def add_static_page():
    static_page = Page(title='Acasa',
                             slug='home',
                             content='Aceasta este o pagina de test',
                             keywords='costume,stofa,botosani')
    static_page.save()
    return static_page


class SiteViewsTestCase(TestCase):
    def create_app(self):
        init_app()
        return app

    def setUp(self):
        create_database(self.app)
        static_page = add_static_page()

    def tearDown(self):
        os.remove(os.path.join(basedir, 'site.db'))

    def test_get_menu(self):
        pass

