#!/usr/bin/env python
from flask.ext.admin.form.upload import ImageUploadField, thumbgen_filename
from flask.helpers import url_for
from markupsafe import Markup

from suittale.admin_core import AdminBaseView, base_path
from suittale.products.models import Category, Product, Texture, op
from wtforms import fields
from flask import request


class AdminCategoryView(AdminBaseView):
    # Override displayed fields
    column_list = ('name', 'creation_date')

    form_excluded_columns = ['version', 'creation_date',
                             'updated_by', 'parent_id', 'products']


    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCategoryView, self).__init__(Category, session, **kwargs)


class AdminTextureView(AdminBaseView):
    def _list_thumbnail(view, context, model, name):
        if not model.image:
            return ''

        return Markup('<img src="%s">' % url_for('static',
                                                 filename=thumbgen_filename(model.image)))

    column_formatters = {
        'image': _list_thumbnail
    }

    # Override displayed fields
    column_list = ('code', 'composition', 'image')

    form_extra_fields = {
        'image': ImageUploadField('Image',
                                  base_path=op.join(base_path, 'uploads'),
                                  thumbnail_size=(100, 100, True))
    }

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminTextureView, self).__init__(Texture, session, **kwargs)

    def postprocess_form(self, form_class):
        form_class.upload = fields.FileField('Image')
        return form_class

    def on_model_change(self, form, model, is_created):
        file_data = request.files.get(form.image.name)

        if file_data:
            model.image = 'uploads/' + file_data.filename


class AdminProductView(AdminBaseView):
    # Override displayed fields
    column_list = ('name', 'code')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminProductView, self).__init__(Product, session, **kwargs)


