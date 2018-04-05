from setuptools import setup, find_packages

setup(
    name='comp2005l',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-migrate',
        'flask-socketio'
    ],
    package_data={"app": ["config.py", '*.db', 'README.md', 'LICENSE']}
)
