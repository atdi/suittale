#!/usr/bin/env python

import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
TESTING = False
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://admin6zauNc9:wvkX75P8nvs3@$OPENSHIFT_MYSQL_DB_HOST:$OPENSHIFT_MYSQL_DB_PORT/suittale'
#SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/suittale'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'users.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')