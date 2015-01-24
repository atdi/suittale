#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'site.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = '007BOND'
BABEL_DEFAULT_LOCALE = 'ro'
BABEL_DEFAULT_TIMEZONE = 'Europe/Bucharest'