# -*- coding: utf-8 -*- 

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
#Copyright (c) 2005-2006 The PIDA Project

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import pida.utils.log as log

def set_boss(boss):
    """Called by the boss itself. Singletonish behaviour."""
    pidaobject.boss = boss


class pidaobject(object):
    """The base pida class."""

    pass
    

class pidalogenabled(pidaobject):
    """Logging mixin."""

    def __init__(self, *args, **kw):
        pidaobject.__init__(self, *args, **kw)
        try:
            log_file = os.path.join(self.boss.pida_home, 'log', 'pida.log')
            self.log = log.build_logger(self.__class__.__name__, log_file)
        except AttributeError:
            # running outside the boss (like in tests)
            pass


class pidacomponent(pidalogenabled):
    """A single component."""

    def __init__(self, *args, **kw):
        pidalogenabled.__init__(self, *args, **kw)
        self.init(*args, **kw)

    def init(self, *args, **kw):
        """The actual constructor."""

    def init_log(self):
        """
        Function to tell the wanted logging behaviour
        """
        self.use_stream_handler('INFO')

    def is_leaf(self):
        return True
    is_leaf = property(is_leaf)


class pidagroup(pidacomponent):
    """A group of components."""

    component_type = pidacomponent
    group_type = lambda *a: pidagroup(*a)

    def init(self, name):
        self.__name = name
        self.__components = {}

    def add(self, name, component):
        """Add a component."""
        self.__components[name] = component
        return component

    def add_group(self, name, *args):
        group = self.group_type(name, *args)
        self.__components[name] = group
        return group

    def new(self, componentname, *args, **kw):
        component = self.component_type(componentname, *args, **kw)
        self.add(componentname, component)
        return component

    def remove(self, name):
        if name in self.__components:
            del self.__components[name]

    def get(self, name):
        """Return the named component, or None."""
        try:
            return self.__components[name]
        except KeyError:
            return None

    def get_name(self):
        """Return the name for the group."""
        return self.__name
    name = property(get_name)

    def __iter__(self):
        for k in self.__components:
            yield self.__components[k]

    def __len__(self):
        return len(self.__components)

    def iter_groups(self):
        for component in self:
            if not component.is_leaf:
                yield component

    def iter_components(self):
        for component in self:
            if component.is_leaf:
                yield component

    def is_leaf(self):
        return False
    is_leaf = property(is_leaf)


class pidamanager(pidagroup):
    """Manage components within top-level groups."""

    def init(self):
        pidagroup.init(self, None)

    def get_component(self, groupname, componentname):
        group = self.get(groupname)
        if group is not None:
            return group.get(componentname)

    def add_component(self, groupname, componentname, component):
        group = self.get(groupname)
        if group is not None:
            group.add(componentname, component)
        
    def new_component(self, groupname, componentname, *args, **kw):
        component = self.component_type(*args, **kw)
        self.add_component(component)

    def iter_items(self):
        for group in self.iter_groups():
            for item in group.iter_components():
                yield group, item

