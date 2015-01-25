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


def add_static_page(title, slug):
    static_page = Page(title=title,
                             slug=slug,
                             content='Aceasta este o pagina de test',
                             keywords='costume,stofa,botosani')
    static_page.save()
    return static_page


def add_carousel_image(name, path, page_id):
    carousel_img = CarouselImages(name=name, path=path, page_id=page_id)
    carousel_img.save()


class SiteMethodsTestCase(TestCase):
    def create_app(self):
        init_app()
        return app

    def setUp(self):
        create_database(self.app)
        home_page = add_static_page('Acasa', 'home')
        add_static_page('Despre', 'despre')
        add_carousel_image('img1', 'path1', home_page.id)
        add_carousel_image('img2', 'path2', home_page.id)

    def tearDown(self):
        os.remove(os.path.join(basedir, 'site.db'))

    def test_get_index(self):
        result = self.client.get('/')
        self.assert200(result)

    def test_get_images(self):
        page = Page.query.filter_by(slug='home').first()
        images = get_images(page.images)
        self.assertTrue(images[0]['active'])
        self.assertFalse(images[1]['active'])



