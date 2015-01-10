#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin6zauNc9:wvkX75P8nvs3@127.12.252.2:3306/suittale'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SECRET_KEY = '007BOND'
BABEL_DEFAULT_LOCALE = 'ro'
BABEL_DEFAULT_TIMEZONE = 'Europe/Bucharest'