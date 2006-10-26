__version__ = '1.0a2'

from setuptools import setup, find_packages
import sys, os
import textwrap

## import finddata

setup(
    name="SchevoWeb",
    
    version=__version__,
    
    description="Schevo tools for web development",
    
    long_description=textwrap.dedent("""
    Provides integration between Schevo_ and various web toolkits.

    .. _Schevo: http://schevo.org/

    The latest development version is available in a `Subversion
    repository
    <http://schevo.org/svn/trunk/Web#egg=SchevoWeb-dev>`__.
    """),
    
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Database :: Database Engines/Servers',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    
    keywords='',
    
    author='Orbtech, L.L.C. and contributors',
    author_email='schevo-devel@lists.schevo.org',

    url='http://schevo.org/trac/wiki/SchevoWeb',
    
    license='LGPL',
    
    platforms=['UNIX', 'Windows'],

    packages=find_packages(exclude=['doc', 'tests']),

##     package_data=finddata.find_package_data(),

    zip_safe=False,
    
    install_requires=[
    'Schevo >= 3.0b2',
    'RuleDispatch >= 0.5a0dev',
    'elementtree >= 1.2.6',
    ],
    
    tests_require=[
    'nose >= 0.9.0',
    ],
    test_suite='nose.collector',
    
    extras_require={
    },
    
    dependency_links = [
    'http://schevo.org/files/thirdparty/',
    ],
    
    entry_points = """
    """,
    )
