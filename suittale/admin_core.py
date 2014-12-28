#!/usr/bin/env python
import os.path as op
from flask.ext.admin.contrib.sqla import ModelView as SqlaModelView
from werkzeug.utils import redirect
from flask.ext.security import current_user

base_path = op.join(op.dirname(__file__), 'static')


class AdminBaseView(SqlaModelView):
    # Override displayed fields
    form_excluded_columns = ['version', 'creation_date', 'updated_by']

    def is_accessible(self):
        return current_user.is_authenticated()

    def inaccessible_callback(self, name, **kwargs):
        """
            Handle the response to inaccessible views.

            By default, it throw HTTP 403 error. Override this method to
            customize the behaviour.
        """
        return redirect('admin/login')