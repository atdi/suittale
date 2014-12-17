from setuptools import setup

setup(name='YourAppName',
      version='1.0',
      description='OpenShift App',
      author='Your Name',
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
                        'behave',
                        'requests',
                        'alembic',
                        'pyhamcrest',
                        'tornado',
                        'mysql-connector-python'],
     )
