#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

import dataexplorer

"""
{{cookiecutter.description}}
"""

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = ['{{cookiecutter.project_name}}', '{{cookiecutter.project_name}}.data',
            '{{cookiecutter.project_name}}.visualization']

tests = [p + '.tests' for p in packages]

setup(
    name='{{cookiecutter.project_name}}',
    version=dataexplorer.__version__,
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.email}}",
    packages=packages + tests,
    install_requires=[
        'python-dotenv>=0.5.1',
    ],
    long_description=long_description,
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
    #package_data={'path_to_data': [list_of_files]},
    zip_safe=False
)
