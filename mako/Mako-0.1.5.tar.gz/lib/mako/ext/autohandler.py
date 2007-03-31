"""adds autohandler functionality to Mako templates.

requires that the TemplateLookup class is used with templates.

usage:

<%!
	from mako.ext.autohandler import autohandler
%>
<%inherit file="${autohandler(template, context)}"/>


or with custom autohandler filename:

<%!
	from mako.ext.autohandler import autohandler
%>
<%inherit file="${autohandler(template, context, name='somefilename')}"/>

"""

import posixpath, os, re

def autohandler(template, context, name='autohandler'):
    lookup = context.lookup
    _template_uri = template.module._template_uri
    if not lookup.filesystem_checks:
        try:
            return lookup._uri_cache[(autohandler, _template_uri, name)]
        except KeyError:
            pass

    tokens = re.findall(r'([^/]+)', posixpath.dirname(_template_uri)) + [name]
    while len(tokens):
        path = '/' + '/'.join(tokens)
        if path != _template_uri and _file_exists(lookup, path):
            if not lookup.filesystem_checks:
                return lookup._uri_cache.setdefault((autohandler, _template_uri, name), path)
            else:
                return path
        if len(tokens) == 1:
            break
        tokens[-2:] = [name]
        
    if not lookup.filesystem_checks:
        return lookup._uri_cache.setdefault((autohandler, _template_uri, name), None)
    else:
        return None

def _file_exists(lookup, path):
    psub = re.sub(r'^/', '',path)
    for d in lookup.directories:
        if os.access(d + '/' + psub, os.F_OK):
            return True
    else:
        return False
    