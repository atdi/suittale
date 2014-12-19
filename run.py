from sqlalchemy.engine import create_engine
from suittale import init_app, app, db
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from suittale.core import BaseModel

init_app('suittale.local_config')

if __name__ == '__main__':
    #engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
    #BaseModel.metadata.create_all(bind=engine)
    #db.create_all()
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(5000)
    IOLoop.instance().start()
