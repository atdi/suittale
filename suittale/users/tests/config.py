#!/usr/bin/env python

import os
from suittale.config import basedir

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'suittale.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = '007BOND'