"""
Plugin for Buffet, modified from BuffetString.
"""

import os

from shrubbery import Template


class TemplatePlugin(object):
    # all template plugins need to define a default file extension
    extension = "shrb"

    def __init__(self, extra_vars_func=None, config=None):
        """extra_vars_func == optional callable() that returns a dict
        config == optional dict() of configuration settings
        """
        self.get_extra_vars = extra_vars_func
        if config:
            self.config = config
        else:
            self.config = dict()

    def load_template(self, template_name):
        """template_name == dotted.path.to.template (without .ext)
        
        The dotted notation is present because many template engines
        allow templates to be compiled down to Python modules.  TurboGears
        uses that feature to its adavantage, and for ease of integration
        the python.templating.engines plugin format requires the path to
        the template to be supplied as a dotted.path.to.template regardless
        of whether is is a module or not.

        In the case of shrubbery templates, they are just simple
        text files, so we deal with the dotted notation and translate
        it into a standard file path to open the text file.
        """
        
        # split the template name up on the dots
        parts = template_name.split('.')
        
        # get the filename.ext
        template_filename = "%s.%s" % (parts.pop(), self.extension)
        
        # get the _real_ path to the template text file
        template_path = os.path.join(*parts)
        template_file_path = os.path.join(template_path, template_filename)

        template_file = open(template_file_path)
        template_obj = template_file.read()
        template_file.close()
        
        return template_obj

    def render(self, info, format="html", fragment=False, template=None):
        """info == dict() of variables to stick into the template namespace
        format == output format if applicable
        fragment == special rules about rendering part of a page
        template == dotted.path.to.template (without .ext)

        You might not need all of these arguments.  info and template are the
        only ones used in this simple example.
        """
        
        vars = info
        
        # check to see if we were passed a function get extra vars
        if callable(self.get_extra_vars):
            vars.update(self.get_extra_vars())
        
        template_obj = self.load_template(template)
        return Template(template_obj, vars).prettify()
