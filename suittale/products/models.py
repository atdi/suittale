#!/usr/bin/env python
from suittale import db
from suittale.core import BaseModel, generate_uuid


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
    __table_args__ = (db.UniqueConstraint('product_id', 'measure_id', 'status', name='_product_measure_uc'),)
    __tablename__ = 'product_measures'
