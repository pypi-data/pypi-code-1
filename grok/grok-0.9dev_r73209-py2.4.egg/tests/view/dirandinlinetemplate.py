"""
If multiple templates can be found, one in the module and one in the
template directory, there is an error:

  >>> grok.grok(__name__)
  Traceback (most recent call last):
    ...
  GrokError: Conflicting templates found for name 'cavepainting' in module
  <module 'grok.tests.view.dirandinlinetemplate' from '...'>,
  both inline and in template directory '...dirandinlinetemplate_templates'.

"""
import grok

class Mammoth(grok.Model):
    pass

class CavePainting(grok.View):
    pass

cavepainting = grok.PageTemplate("nothing")
