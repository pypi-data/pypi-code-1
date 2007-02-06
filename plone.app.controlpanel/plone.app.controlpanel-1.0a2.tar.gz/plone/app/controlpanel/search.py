from zope.interface import Interface
from zope.component import adapts
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.schema import Bool
from zope.schema import Choice
from zope.schema import Tuple

from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import IPloneSiteRoot

from form import ControlPanelForm
from widgets import MultiCheckBoxThreeColumnWidget

class ISearchSchema(Interface):

    enable_livesearch = Bool(title=_(u'Enable LiveSearch'),
                             description=_(u'''Enables the LiveSearch feature,
                                            which shows live results if the
                                            browser supports Javascript.'''),
                             default=False,
                             required=True)

    types_not_searched = Tuple(title=_(u'Define the types to be searched'),
                               description=_(u'''Define the types that should be
                                             searched when you use the
                                             searchbox. Note that if new content
                                             types are installed, they will be
                                             enabled for search by default
                                             unless explicitly turned off here
                                             or by the relevant installer.'''),
                               required=True,
                               missing_value=tuple(),
                               value_type=Choice(
                                   vocabulary="plone.app.vocabularies.PortalTypes"))


class SearchControlPanelAdapter(SchemaAdapterBase):
    
    adapts(IPloneSiteRoot)
    implements(ISearchSchema)

    def __init__(self, context):
        super(SearchControlPanelAdapter, self).__init__(context)
        pprop = getToolByName(context, 'portal_properties')
        self.context = pprop.site_properties
        self.jstool=getToolByName(context, 'portal_javascripts')
        self.ttool=getToolByName(context, 'portal_types')

    def get_enable_livesearch(self):
        return self.context.enable_livesearch

    def set_enable_livesearch(self, value):
        if value:
            self.context.manage_changeProperties(enable_livesearch=True)
            self.jstool.getResource('livesearch.js').setEnabled(True)
        else:
            self.context.manage_changeProperties(enable_livesearch=False)
            self.jstool.getResource('livesearch.js').setEnabled(False)
        self.jstool.cookResources()

    enable_livesearch = property(get_enable_livesearch, set_enable_livesearch)

    def get_types_not_searched(self):
        return [t for t in self.ttool.listContentTypes()
                        if t not in self.context.types_not_searched]

    def set_types_not_searched(self, value):
        value = [t for t in self.ttool.listContentTypes() if t not in value]
        self.context._updateProperty('types_not_searched', value)

    types_not_searched = property(get_types_not_searched, set_types_not_searched)


class SearchControlPanel(ControlPanelForm):

    form_fields = FormFields(ISearchSchema)
    form_fields['types_not_searched'].custom_widget = MultiCheckBoxThreeColumnWidget
    form_fields['types_not_searched'].custom_widget.cssClass='label'

    label = _("Search settings")
    description = _("Search settings for Site.")
    form_name = _("Search details")
