#!/usr/bin/env python
from flask.ext.admin.model.form import InlineFormAdmin
from suittale.admin_core import AdminBaseView
from .models import User, Role, Country, \
    Region, City, Customer, Address


class AdminUserView(AdminBaseView):

    column_list = ('first_name', 'last_name', 'email', 'phone')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminUserView, self).__init__(User, session, **kwargs)


class AdminRoleView(AdminBaseView):

    column_list = ('name', 'creation_date')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminRoleView, self).__init__(Role, session, **kwargs)


class AdminCountryView(AdminBaseView):

    column_list = ('name', 'code', 'creation_date')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCountryView, self).__init__(Country, session, **kwargs)


class AdminRegionView(AdminBaseView):

    column_list = ('name', 'code', 'creation_date')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminRegionView, self).__init__(Region, session, **kwargs)


class AdminCityView(AdminBaseView):

    column_list = ('name', 'creation_date')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCityView, self).__init__(City, session, **kwargs)


class AdminAddressForm(InlineFormAdmin):
    column_list = ('contact_person', 'phone', 'is_default')

    form_excluded_columns = ['version', 'creation_date', 'updated_by']


class AdminCustomerView(AdminBaseView):
    inline_models = (AdminAddressForm(Address),)

    column_list = ('name', 'unique_id', 'type', 'creation_date')

    form_choices = {'type': [
        ('PF', 'Persoana Fizica'),
        ('PJ', 'Persoana Juridica'),
    ]}

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminCustomerView, self).__init__(Customer, session, **kwargs)