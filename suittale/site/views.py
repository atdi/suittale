__author__ = 'aurel'

from .models import Page
from suittale import app
from flask import json


def create_api(rest_manager):
    rest_manager.create_api(Page, url_prefix='/titles', include_columns=['slug', 'title'], methods=['GET'])


@app.route('/menuitems', methods=['GET'])
def get_menu_items():
    pages = Page.filter(published=True, parent_id=None).all()
    dict_pages = list(map(lambda page:
                          page.to_dict(include=['slug', 'title', 'children']), pages))
    return json.dumps(dict_pages)





