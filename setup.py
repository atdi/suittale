from setuptools import setup

setup(name='Suit Tale',
      version='1.0',
      description='A tails about suites',
      author='Aurel Avramescu',
      author_email='example@example.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['sqlalchemy',
                        'flask',
                        'flask-sqlalchemy',
                        'flask-restless',
                        'flask-script',
                        'flask-migrate',
                        'flask-testing',
                        'flask-security',
                        'flask-babelPkg',
                        'behave',
                        'requests',
                        'alembic',
                        'pyhamcrest',
                        'tornado',
                        'mysql-connector-python',
                        'flask-admin',
                        'pillow'],
     )
