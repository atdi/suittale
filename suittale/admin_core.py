#!/usr/bin/env python
import os.path as op
from flask.ext.admin.contrib.sqla import ModelView as SqlaModelView

# Figure out base upload image
base_path = op.join(op.dirname(__file__), 'static')


class AdminBaseView(SqlaModelView):
    # Override displayed fields
    form_excluded_columns = ['version', 'creation_date', 'updated_by']