#!/usr/bin/env python
from suittale.admin_core import AdminBaseView
from suittale.site.models import StaticPage, LinkPage


class AdminStaticPage(AdminBaseView):

    column_list = ('title', 'slug')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminStaticPage, self).__init__(StaticPage, session, **kwargs)


class AdminLinkPage(AdminBaseView):

    column_list = ('title', 'url')

    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(AdminLinkPage, self).__init__(LinkPage, session, **kwargs)