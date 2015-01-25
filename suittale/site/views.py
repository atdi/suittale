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
    return render_template('index.html', title=page.title,
                           content_title=page.content_title,
                           content=page.content,
                           second_content_title=page.second_content_title,
                           second_content=page.second_content,
                           images=images)


@app.route('/about', methods=['GET'])
def about():
    page = Page.query.filter_by(slug='about').first()
    return render_template('about.html', title=page.title,
                           content_title=page.content_title,
                           content=page.content,
                           second_content_title=page.second_content_title,
                           second_content=page.second_content)





