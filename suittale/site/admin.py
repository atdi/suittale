#!/usr/bin/env python
from flask.ext.admin.form.upload import ImageUploadField, thumbgen_filename
from flask.helpers import url_for
from flask import request
from markupsafe import Markup
from suittale.admin_core import AdminBaseView, base_path
from suittale.site.models import StaticPage, LinkPage, CarouselImages, ComplexStaticPage
import os.path as op

CAROUSEL_IMG_PATH = 'uploads/carousel'

class AdminStaticPageView(AdminBaseView):

    column_list = ('title', 'slug')

    def __init__(self, session, **kwargs):
        self.form_excluded_columns.append("type")
        super(AdminStaticPageView, self).__init__(StaticPage, session, **kwargs)


class AdminComplexStaticPageView(AdminBaseView):

    column_list = ('title', 'slug')

    def __init__(self, session, **kwargs):
        self.form_excluded_columns.append("type")
        super(AdminComplexStaticPageView, self).__init__(ComplexStaticPage, session, **kwargs)


class AdminLinkPageView(AdminBaseView):

    column_list = ('title', 'url')

    def __init__(self, session, **kwargs):
        self.form_excluded_columns.append("type")
        super(AdminLinkPageView, self).__init__(LinkPage, session, **kwargs)


class AdminCarouselImagesView(AdminBaseView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=thumbgen_filename(model.image)))

    column_formatters = {
        'path': _list_thumbnail
    }


    form_extra_fields = {
        'path': ImageUploadField('Image',
                                  base_path=op.join(base_path, CAROUSEL_IMG_PATH),
                                  thumbnail_size=(100, 100, True))
    }

    def on_model_change(self, form, model, is_created):
        file_data = request.files.get(form.image.name)

        if file_data:
            model.path = CAROUSEL_IMG_PATH + '/' + file_data.filename

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCarouselImagesView, self).__init__(CarouselImages, session, **kwargs)