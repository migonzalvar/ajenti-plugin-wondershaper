#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os.path

from setuptools import setup

__version__ = "0.2.1"


requires = [r.strip() for r in open('requirements.txt') if r]

setup(
    name='ajenti-plugin-wondershaper',
    version=__version__,
    data_files=[
        (
            '/var/lib/ajenti/plugins/wondershaper',
            [f for f in glob.glob(os.path.join('wondershaper', '*py'))]
        ),
        (
            '/var/lib/ajenti/plugins/wondershaper/layout',
            [f for f in glob.glob(os.path.join('wondershaper', 'layout', '*xml'))]
        )
    ],
    install_requires=requires,
    zip_safe=False,

    # metadata
    description='Wondershaper plugin for ajenti',
    author=u'Miguel González',
    author_email='migonzalvar@activitycentral.com',
    url='http://github.com/migonzalvar/ajenti-plugin-wondershper/',
)
