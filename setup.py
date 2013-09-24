#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

__version__ = "0.2.1"


requires = [r.strip() for r in open('requirements.txt') if r]


setup(
    name='ajenti-plugin-wondershaper',
    version=__version__,
    packages=['wondershaper', ],

    install_requires=requires,

    # metadata
    description='Wondershaper plugin for ajenti',
    author=u'Miguel González',
    author_email='migonzalvar@activitycentral.com',
    url='http://github.com/migonzalvar/ajenti-plugin-wondershper/',
)
