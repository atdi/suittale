#!/usr/bin/env python

from suittale.admin_core import AdminBaseView
from suittale.products.models import Category, Product, Texture


class AdminCategoryView(AdminBaseView):
    # Override displayed fields
    column_list = ('name', 'creation_date')

    form_excluded_columns = ['version', 'creation_date', 'updated_by', 'parent_id']

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCategoryView, self).__init__(Category, session, **kwargs)


class AdminTextureView(AdminBaseView):
    # Override displayed fields
    column_list = ('code', 'composition')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminTextureView, self).__init__(Texture, session, **kwargs)


class AdminProductView(AdminBaseView):
    # Override displayed fields
    column_list = ('name', 'code')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminProductView, self).__init__(Product, session, **kwargs)


