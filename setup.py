#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='bracket_representation',
    version='0.1',
    description='Operations with bracket representations of trees',
    author='Eugena Mihailikova',
    author_email='eugena@inbox.ru',
    url='https://github.com/eugena/bracket_representation',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),)
