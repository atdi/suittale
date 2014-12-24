#!/usr/bin/env python
from suittale.core import db, generate_uuid, BaseModel


class Page(BaseModel):
    id = db.Column(db.String(255), primary_key=True, default=generate_uuid)
    slug = db.Column(db.String(100))
    title = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20))
    parent_id = db.Column(db.String(255), db.ForeignKey('pages.id'), nullable=True)
    __tablename__ = 'pages'

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'page'
    }

    def __str__(self):
        return '%s' % (self.title)


class StaticPage(Page):
    __tablename__ = 'static_pages'
    id = db.Column(db.String(255), db.ForeignKey('pages.id'), primary_key=True)
    keywords = db.Column(db.String(255))
    content= db.Column(db.Text)
    __mapper_args__ = {
        'polymorphic_identity': 'static_page'
    }


class LinkPage(Page):
    __tablename__ = 'link_pages'
    id = db.Column(db.String(255), db.ForeignKey('pages.id'), primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'link_page'
    }
