#!/usr/bin/env python

import sys

from setuptools import setup

sys.path.insert(0, 'xart')
from xart import __version__
VERSION = __version__
sys.path.pop(0)


setup(
    name='xart',
    version=VERSION,
    description='ASCII text by xlzd',
    license='WTFPL',
    author='xlzd',
    author_email='i@xlzd.me',
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Fonts',
    ],
    url='https://github.com/xlzd/xart',
    packages=['xart', 'xart.fonts'],
    package_data={'xart.fonts': ['*.flf', '*.flc']},
    entry_points={
        'console_scripts': [
            'xart = xart:main',
        ],
    }
)