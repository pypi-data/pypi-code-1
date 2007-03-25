from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class ISearchPortlet(IPortletDataProvider):
    """ A portlet displaying a (live) search box
    """

    enableLivesearch = schema.Bool(
            title = _(u"Enable LiveSearch"),
            description = _(u"Enables the LiveSearch feature, which shows "
                             "live results if the browser supports "
                             "Javascript."),
            default = True,
            required = False)

class Assignment(base.Assignment):
    implements(ISearchPortlet)

    def __init__(self, enableLivesearch=True):
        self.enableLivesearch=True

    @property
    def title(self):
        return _(u"Search")


class Renderer(base.Renderer):

    render = ViewPageTemplateFile('search.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)

        self.portal_state = getMultiAdapter((context, request), name=u'plone_portal_state')


    def enable_livesearch(self):
        return self.data.enableLivesearch


    def search_form(self):
        return '%s/search_form' % self.portal_state.portal_url()


    def search_action(self):
        return '%s/search' % self.portal_state.portal_url()




class AddForm(base.AddForm):
    form_fields = form.Fields(ISearchPortlet)
    label = _(u"Add Search portlet")
    description = _(u"This portlet shows a search box.")

    def create(self, data):
        return Assignment()


class EditForm(base.EditForm):
    form_fields = form.Fields(ISearchPortlet)
    label = _(u"Edit Search portlet")
    description = _(u"This portlet shows a search box.")

