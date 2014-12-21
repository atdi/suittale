#!/usr/bin/env python
from flask.ext.admin.form.upload import ImageUploadField, thumbgen_filename
from flask.ext.admin.model.form import InlineFormAdmin
from flask.helpers import url_for
from markupsafe import Markup
from suittale.admin_core import AdminBaseView, base_path
from .models import Category, Product, Texture, op, ProductAttribute, ProductImage
from flask import request
from .constants import PRODUCTS_IMG_PATH, TEXTURES_IMG_PATH


class AdminCategoryView(AdminBaseView):
    # Override displayed fields
    column_list = ('name', 'creation_date')

    def __init__(self, session, **kwargs):
        self.form_excluded_columns.append('parent_id')
        self.form_excluded_columns.append('products')
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
                                  base_path=op.join(base_path, TEXTURES_IMG_PATH),
                                  thumbnail_size=(100, 100, True))
    }

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminTextureView, self).__init__(Texture, session, **kwargs)

    def on_model_change(self, form, model, is_created):
        file_data = request.files.get(form.image.name)

        if file_data:
            model.image = TEXTURES_IMG_PATH + '/' + file_data.filename


class AdminAttributesForm(InlineFormAdmin):
    form_columns = ('name', 'value')


class AdminProductImagesForm(InlineFormAdmin):
    form_columns = ('name', 'path', 'default')

    form_extra_fields = {
        'path': ImageUploadField('Image',
                                 base_path=op.join(base_path, PRODUCTS_IMG_PATH),
                                 thumbnail_size=(100, 100, True))
    }


class AdminProductView(AdminBaseView):
    inline_models = (AdminAttributesForm(ProductAttribute),
                     AdminProductImagesForm(ProductImage))

    # Override displayed fields
    column_list = ('name', 'code')

    form_columns = ('name', 'code', 'description',
                    'thumbnail', 'price', 'category',
                    'attributes', 'images')

    form_extra_fields = {
        'thumbnail': ImageUploadField('Image',
                                      base_path=op.join(base_path, PRODUCTS_IMG_PATH),
                                      thumbnail_size=(100, 100, True))
    }

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminProductView, self).__init__(Product, session, **kwargs)


