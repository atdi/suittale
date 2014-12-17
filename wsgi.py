#!/usr/bin/env python
from suittale import init_app, app
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

init_app()

#
# Below for testing only
#
if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(8051)
    IOLoop.instance().start()

    #from wsgiref.simple_server import make_server
    #httpd = make_server('localhost', 8051, application)
    # Wait for a single request, serve it and quit.
    #httpd.handle_request()
