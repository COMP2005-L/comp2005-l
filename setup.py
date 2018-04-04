from setuptools import setup, find_packages

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-socketio'
    ],

    package_data = { '': ['config.py', 'app.db', 'test.db', 'README.md','LICENSE', 'migrations/*', 'documentation/*'],
                    'app': ['*']}


)
