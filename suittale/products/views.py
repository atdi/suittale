#!/usr/bin/env python

from suittale import rest_manager
from suittale.products.models import Product


rest_manager.create_api(Product, methods=['GET'])