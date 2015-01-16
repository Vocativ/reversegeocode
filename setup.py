import os
from distutils.core import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='reversegeocode', 
    version='1.0',
    packages=['reversegeocode'],
    package_data={'reversegeocode' : ['geocode.csv', 'countries.csv']},
    author='Richard Penman',
    author_email='richard@webscraping.com',
    description='Reverse geocode the given latitude / longitude',
    long_description=read('README.md'),
    url='https://github.com/Vocativ/reversegeocode',
    license='lgpl',
)
