#! /usr/bin/env/python
# -*- coding: iso-8859-1 -*-

## Copyright 2004-2006 by LivingLogic AG, Bayreuth/Germany.
## Copyright 2004-2006 by Walter D�rwald
##
## All Rights Reserved
##
## See orasql/__init__.py for the license


import sys, os, datetime

import py.test

from ll import orasql
from ll.orasql.scripts import oracreate, oradrop, oradiff, oramerge


dbname = os.environ["LL_ORASQL_TEST_CONNECT"] # Need a connectstring as environment var


# here all objects are collected, so we don't need to call iterobjects() multiple times
objlist = []
objdict = {}


def setup_module(module):
	db = orasql.connect(dbname)
	# get all definitions (this tests that iterdefinition(), iterreferences() and iterreferencedby() run to completion)
	module.objdict = {}
	for obj in db.iterobjects():
		module.objlist.append(obj)
		references = list(obj.iterreferences())
		referencedby = list(obj.iterreferencedby())
		module.objdict[obj] = (references, referencedby)


def teardown_module(module):
	del module.objlist
	del module.objdict


def test_connect():
	db = orasql.connect(dbname)
	assert isinstance(db, orasql.Connection)


def test_connection_connectstring():
	db = orasql.connect(dbname)
	user = dbname.split("/")[0]
	name = dbname.split("@")[1]
	assert "%s@%s" % (user, name) == db.connectstring()


def test_connection_iterschema():
	db = orasql.connect(dbname)
	list(db.iterschema())


def test_referenceconsistency():
	for (obj, (references, referencedby)) in objdict.iteritems():
		for refobj in references:
			# check that iterobjects() returned everything from this schema
			assert refobj.owner is not None or refobj in objdict
			# check that the referenced object points back to this one (via referencedby)
			if refobj.owner is None:
				assert obj in objdict[refobj][1]

		# do the inverted check
		for refobj in referencedby:
			assert refobj.owner is not None or refobj in objdict
			if refobj.owner is None:
				assert obj in objdict[refobj][0]


def test_ddl():
	# check various ddl methods
	for obj in objdict:
		obj.createddl()
		if isinstance(obj, orasql.Sequence):
			obj.createddlcopy()
		obj.dropddl()
		if isinstance(obj, orasql.ForeignKey):
			obj.enableddl()
			obj.disableddl()


def test_repr():
	# check that each repr method works
	for obj in objdict:
		repr(obj)


def test_cudate():
	# check that cdate/udate method works
	for obj in objdict:
		cdate = obj.cdate()
		assert cdate is None or isinstance(cdate, datetime.datetime)
		udate = obj.udate()
		assert udate is None or isinstance(udate, datetime.datetime)


def test_table_columns():
	for obj in objdict:
		if isinstance(obj, orasql.Table):
			for col in obj.itercolumns():
				# comments are not output by iterobjects(), so we have to call iterreferences()
				assert obj in col.iterreferences()
				# check various methods
				# calling modifyddl() doesn't make sense
				col.addddl()
				col.dropddl()
				col.cdate()
				col.udate()
				col.datatype()
				col.default()
				col.nullable()
				col.comment()


def test_table_comments():
	for obj in objdict:
		if isinstance(obj, orasql.Table):
			# comments are output by iterobjects(), but not for materialized views
			if obj.ismview():
				for com in obj.itercomments():
					assert obj in com.iterreferences()
			else:
				for com in obj.itercomments():
					assert obj in objdict[com][0]


def test_table_constraints():
	for obj in objdict:
		if isinstance(obj, orasql.Table):
			for con in obj.iterconstraints():
				assert obj in objdict[con][0]


def test_table_records():
	for obj in objdict:
		if isinstance(obj, orasql.Table):
			# fetch only a few records
			for (i, rec) in enumerate(obj.iterrecords()):
				if i >= 5:
					break


def test_table_mview():
	for obj in objdict:
		if isinstance(obj, orasql.Table):
			assert (obj.mview() is not None) == obj.ismview()


def test_constraints():
	for obj in objdict:
		if isinstance(obj, orasql.Constraint):
			obj.table()
			if isinstance(obj, orasql.ForeignKey):
				obj.pk()


def test_procedure_arguments():
	for obj in objdict:
		if isinstance(obj, orasql.Procedure):
			list(obj.iterarguments())


def test_procedure_nonexistant():
	db = orasql.connect(dbname)
	py.test.raises(orasql.SQLObjectNotFoundError, orasql.Procedure("DOESNOTEXIST"), db.cursor())


def test_createorder():
	# check that the default output order of iterobjects() (i.e. create order) works
	done = set()
	for obj in objlist:
		for refobj in objdict[obj][0]:
			print obj, refobj
			assert refobj in done
		done.add(obj)


class BitBucket(object):
	def write(self, text):
		pass


def withbitbucket(func):
	def decorator(*args, **kwargs):
		oldstdout = sys.stdout
		oldstderr = sys.stderr
		bitbucket = BitBucket()
		try:
			sys.stdout = bitbucket
			sys.stderr = bitbucket
			return func(*args, **kwargs)
		finally:
			sys.stdout = oldstdout
			sys.stderr = oldstderr
	return decorator


@withbitbucket
def test_scripts_oracreate():
	# Test oracreate without executing anything
	args = "--color yes --verbose --seqcopy %s" % dbname
	oracreate.main(args.split())


@withbitbucket
def test_scripts_oradrop():
	# Test oradrop without executing anything
	args = "--color yes --verbose %s" % dbname
	oradrop.main(args.split())


@withbitbucket
def test_scripts_oradiff():
	# Test oradiff (not really: we will not get any differences)
	args = "--color yes --verbose %s %s" % (dbname, dbname)
	oradiff.main(args.split())


@withbitbucket
def test_scripts_oramerge():
	# Test oramerge (not really: we will not get any differences)
	args = "--color yes --verbose %s %s %s" % (dbname, dbname, dbname)
	oramerge.main(args.split())


def test_callprocedure():
	db = orasql.connect(dbname)
	proc = orasql.Procedure("orasql_test")
	result = proc(db.cursor(), p_in=42, p_inout=17)
	assert result.p_in == 42
	assert result.p_out == 17
	assert result.p_inout == 40
