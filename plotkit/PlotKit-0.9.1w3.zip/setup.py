from setuptools import setup, find_packages
from turbogears.finddata import find_package_data

import os
execfile(os.path.join("plotkit", "release.py"))

setup(
    name="PlotKit",
    version=version,
    
    # uncomment the following lines if you fill them out in release.py
    description=description,
    long_description=long_description,
    author=author,
    author_email=email,
    url=url,
    download_url=download_url,
    license=license,
    
    install_requires = ["TurboGears >= 1.0b2"],
    zip_safe=True,
    packages=find_packages(),
    package_data = find_package_data(where='plotkit',
                                     package='plotkit'),
    keywords = [
        # Use keywords if you'll be adding your package to the
        # Python Cheeseshop
        
        # if this has widgets, uncomment the next line
        'turbogears.widgets',
        
        # if this has a tg-admin command, uncomment the next line
        # 'turbogears.command',
        
        # if this has identity providers, uncomment the next line
        # 'turbogears.identity.provider',
    
        # If this is a template plugin, uncomment the next line
        # 'python.templating.engines',
        
        # If this is a full application, uncomment the next line
        # 'turbogears.app',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: TurboGears',
        # if this is an application that you'll distribute through
        # the Cheeseshop, uncomment the next line
        # 'Framework :: TurboGears :: Applications',
        
        # if this is a package that includes widgets that you'll distribute
        # through the Cheeseshop, uncomment the next line
        'Framework :: TurboGears :: Widgets',
    ],
    entry_points = """
    [turbogears.widgets]
    plotkit = plotkit.widgets
    """,
    test_suite = 'nose.collector',
    )
    
