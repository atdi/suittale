#!/usr/bin/env python
from flask.ext.admin.base import AdminIndexView, expose
from flask.ext.security import current_user, login_user
from flask.ext.security.forms import LoginForm
from flask import url_for, request, helpers
from werkzeug.utils import redirect


class SuittaleAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(SuittaleAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(SuittaleAdminIndexView, self).index()