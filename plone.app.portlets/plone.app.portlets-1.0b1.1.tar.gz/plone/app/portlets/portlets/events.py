from zope import schema
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider

from Acquisition import aq_inner
from DateTime.DateTime import DateTime
from Products.CMFCore.interfaces import ICatalogTool
from Products.CMFPlone import PloneMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class IEventsPortlet(IPortletDataProvider):

    count = schema.Int(title=_(u'Number of items to display'),
                       description=_(u'How many items to list'),
                       required=True,
                       default=5)

    state = schema.Tuple(title=_(u"Workflow state"),
                         description=_(u"Items in which workflow state to show."),
                         default=('published', ),
                         required=True,
                         max_length=1,
                         value_type=schema.Choice(
                             vocabulary="plone.app.vocabularies.WorkflowStates")
                         )

class Assignment(base.Assignment):
    implements(IEventsPortlet)

    def __init__(self, count=5, state=('published', )):
        self.count = count
        self.state = state

    @property
    def title(self):
        return _(u"Events")

class Renderer(base.Renderer):

    render = ViewPageTemplateFile('events.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.portal_url = portal_state.portal_url()
        self.portal = portal_state.portal()

        self.have_events_folder = 'events' in self.portal.objectIds()

    @property
    def available(self):
        return len(self._data())

    def published_events(self):
        return self._data()

    def all_events_link(self):
        if self.have_events_folder:
            return '%s/events' % self.portal_url
        else:
            return '%s/events_listing' % self.portal_url

    def prev_events_link(self):
        if self.have_events_folder and 'previous' in self.portal['events'].objectIds():
            return '%s/events/previous' % self.portal_url
        else:
            return None

    @memoize
    def _data(self):
        context = aq_inner(self.context)
        catalog = getUtility(ICatalogTool)
        limit = self.data.count
        state = self.data.state
        # We don't support querying for more than one state at a time yet
        if len(state) > 0:
            state = state[0]
        return catalog(portal_type='Event',
                       review_state=state,
                       end={'query': DateTime(),
                            'range': 'min'},
                       sort_on='start',
                       sort_limit=limit)[:limit]

class AddForm(base.AddForm):
    form_fields = form.Fields(IEventsPortlet)
    label = _(u"Add Events portlet")
    description = _(u"This portlet lists upcoming Events.")

    def create(self, data):
        return Assignment(count=data.get('count', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(IEventsPortlet)
    label = _(u"Edit Events portlet")
    description = _(u"This portlet lists upcoming Events.")
