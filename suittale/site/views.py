__author__ = 'aurel'

from .models import Page
from suittale import app
from flask import json


@app.route('/menuitems', methods=['GET'])
def get_menu_items():
    pages = Page.query.filter_by(published=True, parent_id=None).all()
    dict_pages = list(map(lambda page:
                          page.to_dict(include=['slug', 'title', 'children']), pages))
    return json.dumps(dict_pages)





