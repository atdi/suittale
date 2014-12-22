#!/usr/bin/env python
from flask.ext.admin.base import AdminIndexView, expose
from flask.ext.admin import helpers
from flask.ext.admin.menu import MenuLink
from flask.ext.security import current_user, login_user, logout_user
from flask.ext.security.forms import LoginForm
from flask import url_for, request
from werkzeug.utils import redirect
from suittale.users.models import User


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
            user = User.query.filter_by(email=form.data['email'], password=form.data['password']).first()
            login_user(user)

        if current_user.is_authenticated():
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(SuittaleAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


# Create menu links classes with reloaded accessible
class AuthenticatedMenuLink(MenuLink):

    def is_accessible(self):
        return current_user.is_authenticated()