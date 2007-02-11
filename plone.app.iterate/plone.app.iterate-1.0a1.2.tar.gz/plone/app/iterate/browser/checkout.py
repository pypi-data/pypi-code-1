##################################################################
#
# (C) Copyright 2006 ObjectRealms, LLC
# All Rights Reserved
#
# This file is part of iterate.
#
# iterate is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# iterate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with iterate; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##################################################################

from zope.component import getMultiAdapter, getAdapters

from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from ZODB.POSException import ConflictError

from Products.statusmessages.interfaces import IStatusMessage

from plone.app.iterate.interfaces import ICheckinCheckoutPolicy
from plone.app.iterate.interfaces import CheckoutException
from plone.app.iterate.interfaces import IWCContainerLocator
from plone.app.iterate.interfaces import IObjectArchiver

class Checkout(BrowserView):
    
    template = ViewPageTemplateFile('checkout.pt')
    
    def containers(self):
        """Get a list of potential containers
        """
        context = aq_inner(self.context)
        for name, locator in getAdapters((context,), IWCContainerLocator):
            if locator.available:
                yield dict(name=name, locator=locator)
    
    def __call__(self):
        context = aq_inner(self.context)
        
        if self.request.form.has_key('form.button.Checkout'):
            control = getMultiAdapter((context, self.request), name=u"iterate_control")
            if not control.checkout_allowed():
                raise CheckoutException(u"Not allowed")

            location = self.request.form.get('checkout_location', None)
            locator = None
            try:
                locator = [c['locator'] for c in self.containers() if c['name'] == location][0]
            except IndexError:
                IStatusMessage(self.request).addStatusMessage("Cannot find checkout location", type='stop')
                self.request.response.redirect(self.context.absolute_url())
                return

            policy = ICheckinCheckoutPolicy(context)
            wc = policy.checkout(locator())
            
            # we do this for metadata update side affects which will update lock info
            context.reindexObject('review_state')
            
            IStatusMessage(self.request).addStatusMessage("Check-out created", type='info')
            self.request.response.redirect(wc.absolute_url())
        elif self.request.form.has_key('form.button.Cancel'):
            self.request.response.redirect(self.context.absolute_url())
        else:
            return self.template()