#!/usr/bin/env python

from suittale.products.models import Product, SuitSizeGuide, Texture


def create_api(rest_manager):
    rest_manager.create_api(Product, methods=['GET'])
    rest_manager.create_api(SuitSizeGuide, methods=['GET'])
    rest_manager.create_api(Texture, methods=['GET'])