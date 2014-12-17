#!/usr/bin/env python
import os
from suittale import init_app
from suittale import app as application

init_app()

#
# Below for testing only
#
#if __name__ == '__main__':
#    from wsgiref.simple_server import make_server
#    httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
#    httpd.handle_request()
