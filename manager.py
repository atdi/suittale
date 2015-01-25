# coding: utf-8
from sqlalchemy.engine import create_engine
from suittale import init_app, app, db
from suittale.admin_core import base_path
from suittale.core import BaseModel
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.script import Command
from suittale.products.constants import PRODUCTS_IMG_PATH, TEXTURES_IMG_PATH
from suittale.site.constants import CAROUSEL_IMG_PATH
import os
import os.path as op
from babel.messages import extract


# Command for required folders creation
class CreateFoldersCommand(Command):
    def run(self):
        # Create directory for file fields to use
        uploads_path = op.join(base_path, 'uploads')
        prod_file_path = op.join(base_path, PRODUCTS_IMG_PATH)
        texture_file_path = op.join(base_path, TEXTURES_IMG_PATH)
        carousel_img_path = op.join(base_path, CAROUSEL_IMG_PATH)
        try:
            if not os.path.isdir(uploads_path):
                os.mkdir(uploads_path, mode=0o777)
            if not os.path.isdir(prod_file_path):
                os.mkdir(prod_file_path, mode=0o777)
            if not os.path.isdir(texture_file_path):
                os.mkdir(texture_file_path, mode=0o777)
            if not os.path.isdir(carousel_img_path):
                os.mkdir(carousel_img_path, mode=0o777)
        except OSError as err:
            print("OS error: {0}".format(err))

try:
    import suittale.local_config
    init_app('suittale.local_config')
except ImportError:
    init_app()




# Command for database creation whithout using
# alembic
class CreateDatabaseCommand(Command):
    def run(self):
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
        BaseModel.metadata.create_all(bind=engine)

# Init alembic migrations command
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('dc', CreateFoldersCommand)
manager.add_command('init-db', CreateDatabaseCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def extract_messages():
    pass
#     extract.extract_from_dir('suittale')
#-F babel.ini -k _gettext -k _ngettext -k lazy_gettext -o admin.pot --project suittale suittale
#pybabel compile -f -D admin -d ../flask_admin/translations/

@manager.option('-e', '--email', dest='email')
@manager.option('-fn', '--first_name', dest='first_name')
@manager.option('-ln', '--last_name', dest='last_name')
@manager.option('-ph', '--phone', dest='phone')
@manager.option('-p', '--password', dest='password')
def create_admin_user(email, first_name, last_name, phone, password):
    from suittale.users.models import User, Role
    role = Role.query.filter_by(name='ADMINISTRATOR').first()
    user = User()
    user.admin = True
    user.active = True
    user.first_name = first_name
    user.last_name = last_name
    user.password = password
    user.phone= phone
    user.email = email
    user.roles.append(role)
    user.save()


if __name__ == '__main__':
    manager.run()