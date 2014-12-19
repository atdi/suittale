#!/usr/bin/env python

from flask.ext.admin.contrib.sqla import ModelView
from suittale.products.models import Category, Product


class CategoryView(ModelView):
    # Override displayed fields
    column_list = 'name'

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(CategoryView, self).__init__(Category, session, **kwargs)


class ProductView(ModelView):
    # Override displayed fields
    column_list = ('name', 'code')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(ProductView, self).__init__(Product, session, **kwargs)