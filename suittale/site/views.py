__author__ = 'aurel'

from .models import Page
from suittale import app
from flask import render_template


def get_images(images):
    imgs = [{'url': x.path, 'active': images.index(x) == 0} for x in images]
    return imgs


@app.route('/', methods=['GET'])
def index():
    page = Page.query.filter_by(slug='home').first()
    images = get_images(page.images)
    return render_template('index.html', title=page.title, images=images)





