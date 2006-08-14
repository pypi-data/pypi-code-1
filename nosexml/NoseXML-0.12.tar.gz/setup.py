from setuptools import setup, find_packages

setup(
	name="NoseXML",
	version="0.12",
	description="""Nose XML Output plugin""",
	long_description="""A plugin for nose/nosetests that produces an XML report of the result of a test. The XML can then be post-processed using XSLT or additional code into readily viewable forms, and/or stored ina database for long-term analysis of test result trends.""",
	author="Richard Clark",
	author_email="richard@onesquared.net",
	packages=['nosexml'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'Topic :: Communications :: Email',
		'Topic :: Office/Business',
		'Topic :: Software Development :: Testing',
		],
	entry_points = {	'nose.plugins': [ 'nosexml = nosexml.plugin:NoseXML' ] }
	)
