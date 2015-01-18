#!/usr/bin/env python
from suittale.core import db, generate_uuid, BaseModel


class Page(BaseModel):
    __tablename__ = 'pages'
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    title = db.Column(db.String(100), nullable=False)
    keywords = db.Column(db.String(255))
    slug = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))

    def __str__(self):
        return '%s' % self.title

    __mapper_args__ = {
        'polymorphic_identity': 'page',
        'polymorphic_on': type
    }


class StaticPage(Page):
    __tablename__ = 'static_pages'
    main_content = db.Column(db.Text)
    secondary_content = db.Column(db.Text)

    __mapper_args__ = {
        'polymorphic_identity':'static_page',
    }


class CarouselImages(BaseModel):
    __tablename__ = 'carousel_images'
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(50), unique=True)
    path = db.Column(db.String(255), nullable=False)
    page_id = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return '%s' % self.name


class LinkPage(Page):
    __tablename__ = 'link_pages'
    url = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'link_page'
    }

