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

    def __str__(self):
        return self.name


class Texture(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    code = db.Column(db.String(50), unique=True, nullable=False)
    composition = db.Column(db.String(100))
    image = db.Column(db.String(255), nullable=False)
    __tablename__ = 'textures'

    def __str__(self):
        return self.code


class Product(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), default='RON', nullable=False)
    category_id = db.Column(db.String(255), db.ForeignKey('categories.id'), nullable=False)
    texture_id = db.Column(db.String(255), db.ForeignKey('textures.id'), nullable=False)
    texture = db.relationship(Texture)
    attributes = db.relationship("ProductAttribute", backref="product")
    images = db.relationship("ProductImage", backref="product")
    sizes = db.relationship("ProductSize", backref="product")
    __tablename__ = 'products'

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    default = db.Column(db.Boolean, default=False, nullable=False)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    __tablename__ = 'product_images'

    def __str__(self):
        return self.name


class Attribute(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.String(255), nullable=False)
    __tablename__ = 'attributes'

    def __str__(self):
        return '%s %s' % (self.name, self.value)


class ProductAttribute(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    attribute_id = db.Column(db.String(255), db.ForeignKey('attributes.id'), nullable=False)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    attribute = db.relationship("Attribute")
    __table_args__ = (db.UniqueConstraint('product_id', 'attribute_id', name='_product_measure_uc'),)
    __tablename__ = 'product_attributes'


class Size(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    size = db.Column(db.String(5), nullable=False)
    __tablename__ = 'sizes'

    def __str__(self):
        return self.size


class ProductSize(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    product_id = db.Column(db.String(255), db.ForeignKey('products.id'), nullable=False)
    size_id = db.Column(db.String(255), db.ForeignKey('sizes.id'), nullable=False)
    size = db.relationship("Size")
    number = db.Column(db.Integer, nullable=False, default=0)
    __table_args__ = (db.UniqueConstraint('product_id', 'size_id', name='_product_size_uc'),)
    __tablename__ = 'product_sizes'


"""
Event listeners
"""


# Register after_delete handler which will delete image file after model gets deleted
@event.listens_for(ProductImage, 'after_delete')
def _handle_prod_image_delete(mapper, conn, target):
    try:
        if target.path:
            os.remove(op.join(base_path, target.path))
            os.remove(op.join(base_path, thumbgen_filename(target.path)))
    except OSError:
            # Don't care if was not deleted because it does not exist
            pass


@event.listens_for(Texture, 'after_delete')
def _handle_texture_image_delete(mapper, conn, target):
    try:
        if target.image:
            os.remove(op.join(base_path, target.image))
            os.remove(op.join(base_path, thumbgen_filename(target.image)))
    except OSError:
            # Don't care if was not deleted because it does not exist
            pass