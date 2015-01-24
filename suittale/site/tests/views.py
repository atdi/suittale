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
    static_page = StaticPage(title='Acasa',
                             slug='home',
                             published=True,
                             content='Aceasta este o pagina de test',
                             keywords='costume,stofa,botosani')
    static_page.save()
    return static_page


def add_link_page():
    link_page = LinkPage(title='Costume',
                             slug='costume',
                             published=True,
                             url='/costume')
    link_page.save()
    return link_page


def add_child_page(parent_id):
    static_page = StaticPage(title='About',
                             slug='about',
                             published=True,
                             content='Aceasta este o pagina de test',
                             keywords='costume,stofa,botosani',
                             parent_id=parent_id)
    static_page.save()
    return static_page


class SiteViewsTestCase(TestCase):
    def create_app(self):
        init_app()
        return app

    def setUp(self):
        create_database(self.app)
        static_page = add_static_page()
        add_link_page()
        add_child_page(static_page.id)

    def tearDown(self):
        os.remove(os.path.join(basedir, 'site.db'))

    def test_get_menu(self):
        response = self.client.get('/menuitems')
        self.assert200(response)
        data = json.loads(response.data)
        self.assertEqual(2, len(data))


