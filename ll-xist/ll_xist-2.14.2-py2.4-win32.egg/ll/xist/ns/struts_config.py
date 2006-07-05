#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

## Copyright 1999-2006 by LivingLogic AG, Bayreuth/Germany.
## Copyright 1999-2006 by Walter D�rwald
##
## All Rights Reserved
##
## See xist/__init__.py for the license

"""
<par>Namespace module for <link href="http://jakarta.apache.org/struts/">Struts</link>
configuration files: <link href="http://jakarta.apache.org/struts/dtds/struts-config_1_1.dtd">http://jakarta.apache.org/struts/dtds/struts-config_1_1.dtd</link>.</par>
"""

__version__ = "$Revision: 1.1 $".split()[1]
# $Source: /data/cvsroot/LivingLogic/Python/xist/src/ll/xist/ns/struts_config.py,v $

from ll.xist import xsc, sims
from ll.xist.ns import xml


class DocType(xsc.DocType):
	def __init__(self):
		xsc.DocType.__init__(
			self,
			'struts-config PUBLIC '
			'"-//Apache Software Foundation//DTD Struts Configuration 1.1//EN" '
			'"http://jakarta.apache.org/struts/dtds/struts-config_1_1.dtd"'
		)


class ElementWithID(xsc.Element):
	class Attrs(xsc.Element.Attrs):
		class id(xsc.IDAttr): pass


class action(ElementWithID):
	class Attrs(ElementWithID.Attrs):
		class attribute(xsc.TextAttr): pass
		class className(xsc.TextAttr): pass
		class forward(xsc.TextAttr): pass
		class include(xsc.TextAttr): pass
		class input(xsc.TextAttr): pass
		class name(xsc.TextAttr): pass
		class parameter(xsc.TextAttr): pass
		class path(xsc.TextAttr): required = True
		class prefix(xsc.TextAttr): pass
		class roles(xsc.TextAttr): pass
		class scope(xsc.TextAttr): values = (u"request", u"session")
		class suffix(xsc.TextAttr): pass
		class type(xsc.TextAttr): pass
		class unknown(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class validate(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")


class action_mappings(ElementWithID):
	xmlname = "action-mappings"
	class Attrs(ElementWithID.Attrs):
		class type(xsc.TextAttr): pass


class controller(ElementWithID):
	class Attrs(ElementWithID.Attrs):
		class bufferSize(xsc.TextAttr): pass
		class className(xsc.TextAttr): pass
		class contentType(xsc.TextAttr): pass
		class debug(xsc.TextAttr): pass
		class forwardPattern(xsc.TextAttr): pass
		class inputForward(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class locale(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class maxFileSize(xsc.TextAttr): pass
		class memFileSize(xsc.TextAttr): pass
		class multipartClass(xsc.TextAttr): pass
		class nocache(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class pagePattern(xsc.TextAttr): pass
		class processorClass(xsc.TextAttr): pass
		class tempDir(xsc.TextAttr): pass


class data_source(ElementWithID):
	xmlname = "data-source"
	class Attrs(ElementWithID.Attrs):
		class className(xsc.TextAttr): pass
		class key(xsc.TextAttr): pass
		class type(xsc.TextAttr): pass


class data_sources(ElementWithID):
	xmlname = "data-sources"


class description(ElementWithID):
	pass


class display_name(ElementWithID):
	xmlname = "display-name"


class exception(ElementWithID):
	class Attrs(ElementWithID.Attrs):
		class bundle(xsc.TextAttr): pass
		class className(xsc.TextAttr): pass
		class handler(xsc.TextAttr): pass
		class key(xsc.TextAttr): required = True
		class path(xsc.TextAttr): pass
		class scope(xsc.TextAttr): pass
		class type(xsc.TextAttr): required = True


class form_bean(ElementWithID):
	xmlname = "form-bean"
	class Attrs(ElementWithID.Attrs):
		class className(xsc.TextAttr): pass
		class dynamic(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class name(xsc.TextAttr): required = True
		class type(xsc.TextAttr): required = True


class form_beans(ElementWithID):
	xmlname = "form-beans"
	class Attrs(ElementWithID.Attrs):
		class type(xsc.TextAttr): pass


class form_property(xsc.Element):
	xmlname = "form-property"
	class Attrs(xsc.Element.Attrs):
		class className(xsc.TextAttr): pass
		class initial(xsc.TextAttr): pass
		class name(xsc.TextAttr): required = True
		class size(xsc.TextAttr): pass
		class type(xsc.TextAttr): required = True


class forward(ElementWithID):
	class Attrs(ElementWithID.Attrs):
		class className(xsc.TextAttr): pass
		class contextRelative(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class name(xsc.TextAttr): required = True
		class path(xsc.TextAttr): required = True
		class redirect(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")


class global_exceptions(ElementWithID):
	xmlname = "global-exceptions"


class global_forwards(ElementWithID):
	xmlname = "global-forwards"
	class Attrs(ElementWithID.Attrs):
		class type(xsc.TextAttr): pass


class icon(ElementWithID):
	pass


class large_icon(ElementWithID):
	xmlname = "large-icon"


class message_resources(ElementWithID):
	xmlname = "message-resources"
	class Attrs(ElementWithID.Attrs):
		class className(xsc.TextAttr): pass
		class factory(xsc.TextAttr): pass
		class key(xsc.TextAttr): pass
		class null(xsc.TextAttr): values = (u"true", u"false", u"yes", u"no")
		class parameter(xsc.TextAttr): required = True


class plug_in(ElementWithID):
	xmlname = "plug-in"
	class Attrs(ElementWithID.Attrs):
		class className(xsc.TextAttr): required = True


class set_property(ElementWithID):
	xmlname = "set-property"
	class Attrs(ElementWithID.Attrs):
		class property(xsc.TextAttr): required = True
		class value(xsc.TextAttr): required = True


class small_icon(ElementWithID):
	xmlname = "small-icon"


class struts_config(ElementWithID):
	xmlname = "struts-config"


action_mappings.model = sims.Elements(action)
data_sources.model = sims.Elements(data_source)
exception.model = \
forward.model = sims.Elements(display_name, description, set_property, icon)
global_exceptions.model = sims.Elements(exception)
action.model = sims.Elements(exception, description, forward, display_name, set_property, icon)
form_beans.model = sims.Elements(form_bean)
form_bean.model = sims.Elements(form_property, display_name, description, set_property, icon)
global_forwards.model = sims.Elements(forward)
struts_config.model = sims.Elements(global_exceptions, controller, message_resources, data_sources, plug_in, action_mappings, form_beans, global_forwards)
controller.model = \
data_source.model = \
form_property.model = \
message_resources.model = \
plug_in.model = sims.Elements(set_property)
icon.model = sims.Elements(small_icon, large_icon)
set_property.model = sims.Empty()
description.model = \
display_name.model = \
large_icon.model = \
small_icon.model = sims.NoElements()


# this is no "official" struts-config element, but nonetheless useful for generating
# the final XML output
class user_struts_config(xsc.Element):
	xmlname = "user-struts-config"
	model = struts_config.model

	def convert(self, converter):
		e = xsc.Frag(
			xml.XML10(),
			u"\n",
			DocType(),
			u"\n",
			struts_config(self.content)
		)
		return e.convert(converter)


class __ns__(xsc.Namespace):
	xmlname = "struts_config"
	xmlurl = "http://jakarta.apache.org/struts/dtds/struts-config_1_1.dtd"
__ns__.makemod(vars())
