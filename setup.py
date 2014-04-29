#!/usr/bin/env python
# -*- coding: utf-8 -*-

import qqsuperman
from setuptools import setup, find_packages

setup(
    name='QQSuperman',
    version=qqsuperman.__version__,
    url='https://github.com/zeuxisoo/python-qqsuperman/',
    license='BSD',
    author=qqsuperman.__author__,
    author_email=qqsuperman.__email__,
    description='The short of descriptions',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=open('requirements.txt').read().splitlines(),
)
