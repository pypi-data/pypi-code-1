#!/usr/bin/env python
"""
An alternate setup.py script for setuptools.

If you have setuptools and run this as 

>>> python setup_egg.py bdist_egg

you will get a python egg.

Use

>>> python setup_egg.py test

to run the tests.


"""
from setuptools import setup, Extension
from setup import *

if __name__ == "__main__":

    setup(
      name             = name,
      version          = version,
      author           = authors['Hagberg'][0],
      author_email     = authors['Hagberg'][1],
      description      = description,
      keywords         = keywords,
      long_description = long_description,
      license          = license,
      platforms        = platforms,
      url              = url,      
      download_url     = download_url,
      packages         = packages,
      data_files       = data,
      classifiers      = classifiers,
      ext_modules      = extension,
      package_data     = package_data,
      include_package_data = True,
      test_suite       = "pygraphviz.tests.test.test_suite", 

      )


