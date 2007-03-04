import new
from zope import interface
from zope.formlib import namedtemplate

class NamedTemplateAdapter(object):
    """A named template adapter implementation that has the ability
    to lookup the template portion from regular traversal (intended for
    being able to customize the template portion of a view component
    in the traditional portal_skins style).
    """

    interface.implements(namedtemplate.INamedTemplate)

    def __init__(self, context):
        self.context = context

    def __call__(self, *args, **kwargs):
        view = self.context.__of__(self.context.context)
        return self.default_template.__of__(view)(*args, **kwargs)

def named_template_adapter(template):
    """Return a new named template adapter which defaults the to given
    template.
    """

    new_class = new.classobj('GeneratedClass', 
                             (NamedTemplateAdapter,),
                             {})
    new_class.default_template = template
    return new_class