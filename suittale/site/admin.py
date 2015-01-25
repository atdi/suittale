#!/usr/bin/env python
from flask.ext.admin.form.upload import ImageUploadField, thumbgen_filename
from flask.helpers import url_for
from flask import request
from markupsafe import Markup
from suittale.admin_core import AdminBaseView, CKTextAreaField, base_path
from suittale.site.models import Page, CarouselImages
import os.path as op
from .constants import CAROUSEL_IMG_PATH


class AdminPageView(AdminBaseView):

    column_list = ('title', 'slug')

    can_delete = False

    form_overrides = dict(content=CKTextAreaField, second_content=CKTextAreaField)

    def __init__(self, session, **kwargs):
        super(AdminPageView, self).__init__(Page, session, **kwargs)


class AdminCarouselImagesView(AdminBaseView):
    def _list_thumbnail(view, context, model, name):
        if not model.path:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=thumbgen_filename(model.path)))

    column_formatters = {
        'path': _list_thumbnail
    }


    form_extra_fields = {
        'path': ImageUploadField('Image',
                                  base_path=op.join(base_path, CAROUSEL_IMG_PATH),
                                  thumbnail_size=(100, 100, True))
    }

    def on_model_change(self, form, model, is_created):
        file_data = request.files.get(form.path.name)

        if file_data:
            model.path = CAROUSEL_IMG_PATH + '/' + file_data.filename

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCarouselImagesView, self).__init__(CarouselImages, session, **kwargs)