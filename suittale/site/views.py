__author__ = 'aurel'

from .models import Page


def create_api(rest_manager):
    rest_manager.create_api(Page, url_prefix='/titles', include_columns=['slug', 'title'], methods=['GET'])


def get_menu_items():
    Page.filter(published=True, parent_id=None).all()


