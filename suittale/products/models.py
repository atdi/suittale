#!/usr/bin/env python
from flask.ext.admin.form.upload import thumbgen_filename
from suittale import db
from suittale.core import BaseModel, generate_uuid
import os
import os.path as op
from sqlalchemy import event
from suittale.admin_core import base_path


class Category(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), unique=True, nullable=False)
    template = db.Column(db.Text, nullable=True)
    parent_id = db.Column(db.String(255), nullable=True)
    products = db.relationship("Product", backref="category")
    __tablename__ = 'categories'


class Texture(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    code = db.Column(db.String(50), unique=True, nullable=False)
    composition = db.Column(db.String(100))
    image = db.Column(db.String(255), nullable=False)
    __tablename__ = 'textures'


class Product(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    thumbnail = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='RON', nullable=False)
    category_id = db.Column(db.String(255), db.ForeignKey('categories.id'), nullable=False)
    texture_id = db.Column(db.String(255), db.ForeignKey('textures.id'), nullable=False)
    texture = db.relationship(Texture)
    attributes = db.relationship("ProductAttribute", backref="product")
    images = db.relationship("ProductImage", backref="product")
    __tablename__ = 'products'


class ProductImage(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    __tablename__ = 'product_images'


class ProductAttribute(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    __tablename__ = 'product_attributes'


class Measure(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    size = db.Column(db.Integer, nullable=False)
    __tablename__ = 'measures'


class ProductMeasure(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    measure_id = db.Column(db.String(255), db.ForeignKey('measures.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    __table_args__ = (db.UniqueConstraint('product_id', 'measure_id', name='_product_measure_uc'),)
    __tablename__ = 'product_measures'


"""
Event listeners
"""


# Register after_delete handler which will delete image file after model gets deleted
@event.listens_for(ProductImage, 'after_delete')
def _handle_prod_image_delete(mapper, conn, target):
    if target.path:
        os.remove(op.join(base_path, target.path))


@event.listens_for(Product, 'after_delete')
def _handle_prod_thumbnail_delete(mapper, conn, target):
    if target.thumbnail:
        os.remove(op.join(base_path, target.thumbnail))


@event.listens_for(Texture, 'after_delete')
def _handle_texture_image_delete(mapper, conn, target):
    if target.image:
        os.remove(op.join(base_path, target.image))
        os.remove(op.join(base_path, thumbgen_filename(target.image)))