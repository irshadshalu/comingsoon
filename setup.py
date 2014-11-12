from setuptools import setup
setup(name='comingsoon',
version='1.0',
description="Coming Soon Page",
author='Akshay Nath.R',
author_email='akshaynathr@gmail.com',
url='http://comingsoon-hoist.rhcloud.com/',
install_requires=
[
'Flask==0.10.1',
'Flask-mongoengine',
'Flask-Login==0.2.7',
'Flask-WTF==0.9.2'
],
)
