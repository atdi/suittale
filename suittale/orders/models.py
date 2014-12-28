#!/usr/bin/env python

from suittale.core import *


class Order(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    order_id = db.Column(db.Integer, autoincrement=True, nullable=False, unique=True)
    user_id = db.Column(db.String(255), nullable=False)
    address_id = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='RON', nullable=False)
    status = db.Column(db.String(20), nullable=False)
    __tablename__ = 'orders'


class OrderProduct(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    product_id = db.Column(db.String(255), nullable=False)
    order_id = db.Column(db.String(255), db.ForeignKey('orders.id'), nullable=False)
    __tablename__ = 'order_products'


class OrderProductAttribute(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    order_product_id = db.Column(db.String(255), db.ForeignKey('order_products.id'), nullable=False)
    size_id = db.Column(db.String(255), nullable=False)
    texture_id = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    __tablename__ = 'order_product_attributes'