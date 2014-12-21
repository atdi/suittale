# coding: utf-8
from suittale import init_app, app, db
from suittale.admin_core import base_path
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.script import Command
from suittale.products.constants import PRODUCTS_IMG_PATH, TEXTURES_IMG_PATH
import os
import os.path as op


# Command for required folders creation
class CreateFoldersCommand(Command):
    def run(self):
        # Create directory for file fields to use
        uploads_path = op.join(base_path, 'uploads')
        prod_file_path = op.join(base_path, PRODUCTS_IMG_PATH)
        texture_file_path = op.join(base_path, TEXTURES_IMG_PATH)
        try:
            if not os.path.isdir(uploads_path):
                os.mkdir(uploads_path)
            if not os.path.isdir(prod_file_path):
                os.mkdir(prod_file_path)
            if not os.path.isdir(texture_file_path):
                os.mkdir(texture_file_path)
        except OSError as err:
            print("OS error: {0}".format(err))

init_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('dc', CreateFoldersCommand)



if __name__ == '__main__':
    manager.run()