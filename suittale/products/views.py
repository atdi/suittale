#!/usr/bin/env python

from suittale.products.models import Product


def create_api(rest_manager):
    rest_manager.create_api(Product, methods=['GET'])