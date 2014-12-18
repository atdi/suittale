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


class Product(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category_id = db.Column(db.String(255), db.ForeignKey('categories.id'))
    __tablename__ = 'products'


#class ProductAttribute(BaseModel):