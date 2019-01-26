# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pytcf',
      version='0.1',
      description='Library for reading and writing files in Text Corpus Format (TCF)',
      url='http://github.com/lueck/pytcf',
      author=u"Christian Lück",
      author_email='cluecksbox@gmail.com',
      license='MIT',
      packages=['pytcf'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
