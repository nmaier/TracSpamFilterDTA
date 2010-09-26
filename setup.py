#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'TracSpamFilterDTA',
    version = '0.0.2',
    author = 'Nils Maier',
    description = 'DownThemAll! specific stuff for the trac spam filter',

    license = 'Public domain',

    zip_safe=True,
    packages=['tracspamfilterdta'],
    install_requires = [
        'trac>=0.11',
    ],
    entry_points = {
        'trac.plugins': [
            'spamfilter.dta = tracspamfilterdta.dta',
        ]
    }
)
