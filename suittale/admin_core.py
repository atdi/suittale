#!/usr/bin/env python

from flask.ext.admin.contrib.sqla import ModelView as SqlaModelView

class AdminBaseView(SqlaModelView):
    # Override displayed fields
    form_excluded_columns = ['version', 'creation_date', 'updated_by']