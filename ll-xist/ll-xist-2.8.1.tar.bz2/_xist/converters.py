#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-

## Copyright 1999-2004 by LivingLogic AG, Bayreuth, Germany.
## Copyright 1999-2004 by Walter D�rwald
##
## All Rights Reserved
##
## See xist/__init__.py for the license

"""
This modules contains the base class for the converter objects used in the call to the
<pyref module="ll.xist.xsc" class="Node" method="convert"><method>convert</method></pyref> method.
"""

__version__ = tuple(map(int, "$Revision: 2.36 $"[11:-2].split(".")))
# $Source: /data/cvsroot/LivingLogic/xist/_xist/converters.py,v $

import ll
import xsc


class ConverterState(object):
	def __init__(self, node, root, mode, stage, target, lang, makeaction, maketarget):
		self.node = node
		self.root = root
		self.mode = mode
		self.stage = stage
		if target is None:
			from ll.xist.ns import html
			target = html
		self.target = target
		self.lang = lang
		self.makeaction = makeaction
		self.maketarget = maketarget


class Converter(object):
	"""
	<par>An instance of this class is passed around in calls to the
	<pyref module="ll.xist.xsc" class="Node" method="convert"><method>convert</method></pyref> method.
	This instance can be used when some element needs to keep state across a nested convert call.
	A typical example are nested chapter/subchapter elements with automatic numbering.
	For an example see the element <pyref module="ll.xist.ns.doc" class="section"><class>ll.xist.ns.doc.section</class></pyref>.</par>
	"""
	def __init__(self, node=None, root=None, mode=None, stage=None, target=None, lang=None, makeaction=None, maketarget=None):
		"""
		<par>Create a <class>Converter</class>.</par>
		<par>Arguments are used to initialize the <class>Converter</class> properties of the
		same name.</par>
		"""
		self.states = [ ConverterState(node=node, root=root, mode=mode, stage=stage, target=target, lang=lang, makeaction=makeaction, maketarget=maketarget)]
		self.contexts = {}

	class node(ll.propclass):
		"""
		<par>The root node for which conversion has been called. This is automatically set by the
		<pyref module="ll.xist.xsc" class="Node" method="conv"><method>conv</method></pyref> method.</par>
		"""
		def __get__(self):
			return self.states[-1].node
	
		def __set__(self, node):
			self.states[-1].node = node
	
		def __delete__(self):
			self.states[-1].node = None

	class root(ll.propclass):
		"""
		<par>The root &url; for the conversion. Resolving &url;s during the conversion process should be done
		relative to <lit>root</lit>.</par>
		"""
		def __get__(self):
			return self.states[-1].root
	
		def __set__(self, root):
			self.states[-1].root = root
	
		def __delete__(self):
			self.states[-1].root = None

	class mode(ll.propclass):
		"""
		<par>The conversion mode. This corresponds directly to the mode in &xslt;.
		The default is <lit>None</lit>.</par>
		"""
		def __get__(self):
			return self.states[-1].mode
	
		def __set__(self, mode):
			self.states[-1].mode = mode
	
		def __delete__(self):
			self.states[-1].mode = None

	class stage(ll.propclass):
		"""
		<par>If your conversion is done in multiple steps or stages you can use this property
		to specify in which stage the conversion process currently is. The default is
		<lit>"deliver"</lit>.</par>
		"""
		def __get__(self):
			if self.states[-1].stage is None:
				return "deliver"
			else:
				return self.states[-1].stage
	
		def __set__(self, stage):
			self.states[-1].stage = stage
	
		def __delete__(self):
			self.states[-1].stage = None

	class target(ll.propclass):
		"""
		<par>Specifies the conversion target. This must be a
		<pyref module="ll.xist.xsc" class="Namespace"><class>Namespace</class></pyref> subclass.</par>
		"""
		def __get__(self):
			if self.states[-1].target is None:
				from ll.xist.ns import html
				return html
			else:
				return self.states[-1].target
	
		def __set__(self, target):
			self.states[-1].target = target
	
		def __delete__(self):
			self.states[-1].target = None

	class lang(ll.propclass):
		"""
		<par>The target language. The default is <lit>None</lit>.</par>
		"""
		def __get__(self):
			return self.states[-1].lang
	
		def __set__(self, lang):
			self.states[-1].lang = lang
	
		def __delete__(self):
			self.states[-1].lang = None

	class makeaction(ll.propclass):
		"""
		<par>If an &xist; conversion is done by an <pyref module="ll.make" class="XISTConvertAction"><class>XISTConvertAction</class></pyref>
		this property will hold the action object during that conversion. If you're not using the
		<pyref module="ll.make"><module>make</module></pyref> module you can simply ignore this property. The default is <lit>None</lit>.</par>
		"""
		def __get__(self):
			return self.states[-1].makeaction
	
		def __set__(self, makeaction):
			self.states[-1].makeaction = makeaction
	
		def __delete__(self):
			self.states[-1].makeaction = None

	class maketarget(ll.propclass):
		"""
		<par>If an &xist; conversion is done by an <pyref module="ll.make" class="XISTConvertAction"><class>XISTConvertAction</class></pyref>
		this property will hold the <pyref module="ll.make" class="Target"><class>Target</class></pyref> object during that conversion.
		If you're not using the <pyref module="ll.make"><module>make</module></pyref> module you can simply ignore this property.
		The default is <lit>None</lit>.</par>
		"""
		def __get__(self):
			return self.states[-1].maketarget
	
		def __set__(self, maketarget):
			self.states[-1].maketarget = maketarget
	
		def __delete__(self):
			self.states[-1].maketarget = None

	class makeproject(ll.propclass):
		"""
		<par>If an &xist; conversion is done by an <pyref module="ll.make" class="XISTConvertAction"><class>XISTConvertAction</class></pyref>
		this property will hold the <pyref module="ll.make" class="Project"><class>Project</class></pyref> object during that conversion.
		If you're not using the <pyref module="ll.make"><module>make</module></pyref> module you can simply ignore this property.
		"""
		def __get__(self):
			maketarget = self.maketarget
			if maketarget is None:
				return None
			else:
				return maketarget.project

	def push(self, node=None, root=None, mode=None, stage=None, target=None, lang=None, makeaction=None, maketarget=None):
		self.lastnode = None
		if node is None:
			node = self.node
		if root is None:
			root = self.root
		if mode is None:
			mode = self.mode
		if stage is None:
			stage = self.stage
		if target is None:
			target = self.target
		if lang is None:
			lang = self.lang
		if makeaction is None:
			makeaction = self.makeaction
		if maketarget is None:
			maketarget = self.maketarget
		self.states.append(ConverterState(node=node, root=root, mode=mode, stage=stage, target=target, lang=lang, makeaction=makeaction, maketarget=maketarget))

	def pop(self):
		if len(self.states)==1:
			raise IndexError("can't pop last state")
		state = self.states.pop()
		self.lastnode = state.node
		return state

	def __getitem__(self, obj):
		"""
		<par>Return a context object for <arg>obj</arg>, which should be an
		<pyref module="ll.xist.xsc" class="Node"><class>Node</class></pyref> or
		<pyref module="ll.xist.xsc" class="Namespace"><class>Namespace</class></pyref> subclass.
		Each of these classes that defines its own
		<pyref module="ll.xist.xsc" class="Element.Context"><class>Context</class></pyref>
		class gets a unique instance of this class. This instance will be created
		on the first access and the element can store information there that needs
		to be available across calls to
		<pyref module="ll.xist.xsc" class="Node" method="convert"><method>convert</method></pyref>.</par>
		"""
		contextclass = obj.Context
		# don't use setdefault(), as constructing the Context object might involve some overhead
		try:
			return self.contexts[contextclass]
		except KeyError:
			return self.contexts.setdefault(contextclass, contextclass())

	# XPython support
	def __enter__(self):
		self.push(node=xsc.Frag())

	# XPython support
	def __leave__(self):
		self.pop()
		self.lastnode = self.lastnode.convert(self)
