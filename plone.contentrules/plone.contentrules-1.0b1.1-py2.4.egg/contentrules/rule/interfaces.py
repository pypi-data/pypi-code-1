"""
"""
__docformat__ = 'restructuredtext'

from zope.interface import Interface, Attribute
from zope.interface.interfaces import IInterface

from zope.app.container.interfaces import IReadContainer
from zope.app.container.interfaces import IContained

from zope import schema
from zope.configuration import fields as configuration_fields

class IRuleElementData(Interface):
    """Metadata for rule element data (the configuration of actions
    or conditions).
    """
    
    element = schema.ASCII(title=u"Rule element",
                              description=u"The name of the rule action or condition",
                              required=True)
                              
    summary = schema.Text(title=u"Summary",
                          description=u"A human-readable description of this element as it is configured",
                          required=True)
        
class IRuleElement(Interface):
    """Base interface for rule elements (actions and conditions)
    
    A rule element is either a condition or an action that can be combined to
    form a rule.Rules can be constructed by the user and invoked by the
    IRuleExecuter
    """
    title = schema.TextLine(
        title = u'Title',
        required = True)
   
    description = schema.Text(
        title = u'Description',
        required = False)

    for_ = configuration_fields.GlobalInterface(
        title = u'Available for',
        description = u'The interface this component is available for',
        required = False)
    
    event = configuration_fields.GlobalInterface(
        title = u'Applicable event',
        description = u'The event that can trigger this element, None meaning '
                       'it is not event specific.',
        required = False)
        
    addview = schema.TextLine(
        title = u'Add view',
        description = u'The name of the add view',
        required = True)
    
    editview = schema.TextLine(
        title = u"Edit view",
        description = u"The name of the edit view",
        required = True)

class IRuleCondition(IRuleElement):
    """A condition of a rule
    
    Rule execution will stop if the condition fails. If the condition does not
    fail, the next element will be executed.
    """

class IRuleAction(IRuleElement):
    """An action executed as part of a rule.
    
    Actions can perform operations, presuming preceding conditions do not fail.
    Once an action is finished, the next element will be executed.
    """
                             
class IRuleEventType(IInterface):
    """Marker interface for event interfaces that can be used as the 'event'
    type of an IRule.
    """

class IRuleConfiguration(Interface):
    """Configurable options for a rule
    """
    
    title = schema.TextLine(title = u'Title',
                            description = u'The title of the rule',
                            required = True)

    description = schema.Text(title = u'Description',
                              description = u'A summary of the rule',
                              required = False)

    event = schema.Choice(title = u'Triggering event',
                          description = u'The event that can trigger this rule',
                          required = True,
                          vocabulary="plone.contentrules.events")

    enabled = schema.Bool(title = u'Enabled',
                          description = u'Whether or not the rule is currently enabled',
                          required = True,
                          default = True)

    stop = schema.Bool(title = u"Stop executing rules",
                       description = u"Whether or not exection of further rules should stop after this rule is executed",
                       required = True,
                       default = False)

class IRule(IContained, IRuleConfiguration):
    """A rule - a collection of rule elements.
    
    A rule is composed, normally through the user interface, of conditions and
    actions. Upon some event, rules that are relevant in the given context will
    be executed by adapting them to IExecutable and running its execute()
    method.
    
    When saved in a rule storage, it will be given a name.
    """
    
    
    conditions = schema.List(title = u'Conditions',
                             description = u'The conditions of this rule',
                             required = True)

    actions = schema.List(title = u'Actions',
                          description = u'The actions of this rule',
                          required = True)
                           

class IExecutable(Interface):
    """An item which can be executed.
    
    The execution of a rule involves the execution of each one of its elements
    (i.e. conditions and actions). The IRule will be adapted to IExecutable in
    order to execute it (e.g. by iterating through the elements and executing
    each one), in a multi-adaptation of (context, rule, event), making it
    possible to customise the execution based on the type of event or context.
    
    Similarly, any object created via the 'addview' of an IRuleElement (i.e. 
    the configuration object for that particular instance of that particular 
    condition or action) will be adapted to IExecutable, in a multi-adaptation 
    from (context, element, event),  in order to be executed when the rule that 
    contains it is executed.
    """
    
    def __call__():
        """Execute the rule or rule element.
                
        If this method returns False, execution will stop. If it returns True,
        execution will continue if possible.
        """