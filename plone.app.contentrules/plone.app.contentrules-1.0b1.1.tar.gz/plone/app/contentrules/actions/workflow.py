from OFS.SimpleItem import SimpleItem
from persistent import Persistent 

from zope.interface import implements, Interface
from zope.component import adapts
from zope.component import queryUtility
from zope.formlib import form
from zope import schema

from plone.contentrules.rule.interfaces import IExecutable, IRuleElementData

from plone.app.contentrules.browser.formhelper import AddForm, EditForm 

import transaction
from Acquisition import aq_inner, aq_parent
from ZODB.POSException import ConflictError
from Products.CMFCore.interfaces import IConfigurableWorkflowTool
from Products.CMFPlone import PloneMessageFactory as _

class IWorkflowAction(Interface):
    """Interface for the configurable aspects of a workflow action.
    
    This is also used to create add and edit forms, below.
    """
    
    transition = schema.Choice(title=_(u"Transition"),
                               description=_(u"Select the workflow transition to attempt"),
                               required=True,
                               vocabulary='plone.app.vocabularies.WorkflowTransitions')
         
class WorkflowAction(SimpleItem):
    """The actual persistent implementation of the action element.
    """
    implements(IWorkflowAction, IRuleElementData)
    
    transition = ''
    element = "plone.actions.Workflow"
    
    @property
    def summary(self):
        return _(u"Execute transition ${transition}", mapping=dict(transition=self.transition))
    
class WorkflowActionExecutor(object):
    """The executor for this action.
    """
    implements(IExecutable)
    adapts(Interface, IWorkflowAction, Interface)
         
    def __init__(self, context, element, event):
        self.context = context
        self.element = element
        self.event = event

    def __call__(self):
        portal_workflow = queryUtility(IConfigurableWorkflowTool)
        if portal_workflow is None:
            return False
            
        obj = self.event.object
        
        try:
            portal_workflow.doActionFor(obj, self.element.transition)
        except ConflictError, e:
            raise e
        except:
            return False
        
        return True 
        
class WorkflowAddForm(AddForm):
    """An add form for workflow actions.
    """
    form_fields = form.FormFields(IWorkflowAction)
    label = _(u"Add Workflow Condition")
    description = _(u"A workflow condition can restrict rules to operating only on objects in a particular workflow state.")
    form_name = _(u"Configure element")
    
    def create(self, data):
        a = WorkflowAction()
        form.applyChanges(a, self.form_fields, data)
        return a

class WorkflowEditForm(EditForm):
    """An edit form for workflow rule actions.
    
    Formlib does all the magic here.
    """
    form_fields = form.FormFields(IWorkflowAction)
    label = _(u"Edit Workflow Condition")
    description = _(u"A workflow condition can restrict rules to operating only on objects in a particular workflow state.")
    form_name = _(u"Configure element")