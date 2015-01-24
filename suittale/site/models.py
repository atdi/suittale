#!/usr/bin/env python
from suittale.core import db, generate_uuid, BaseModel


class Page(BaseModel):
    __tablename__ = 'pages'
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100))
    content_title = db.Column(db.String(100))
    content = db.Column(db.Text)
    second_content_title = db.Column(db.String(100))
    second_content = db.Column(db.Text)
    keywords = db.Column(db.String(255))
    images = db.relationship("CarouselImages", backref="page")

    def __str__(self):
        return '%s' % self.title


class CarouselImages(BaseModel):
    __tablename__ = 'carousel_images'
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(50), unique=True)
    path = db.Column(db.String(255), nullable=False)
    page_id = db.Column(db.String(255), db.ForeignKey('pages.id'), nullable=False)

    def __str__(self):
        return '%s' % self.name

