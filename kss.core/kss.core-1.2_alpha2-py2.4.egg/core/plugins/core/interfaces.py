from zope.interface import Interface

class IKSSCoreCommands(Interface):
    """The core commands"""

    def getSelector(type, selector):
        """Return a specific type of selector

        The type can be `css` or `htmlid`. The selector is the value for the
        selector."""

    def getCssSelector(selector):
        """Return a CSS selector with selector as the value"""

    def getHtmlIdSelector(selector):
        """Return a HTML id selector with selector as the value"""

    def replaceInnerHTML(selector, new_value):
        """Replace the contents of a node (selector) with the new_value"""

    def replaceHTML(selector, new_value):
        """Replace the node itself with new_value
        
        Node selection is done using the selector argument."""

    def setAttribute(selector, name, value):
        """Set an attribute on node(s) specified by the selector"""

    def setStyle(selector, name, value):
        """Set the style attribute of nodes specified by the selector"""

    def insertHTMLAfter(selector, new_value):
        """Insert some HTML after the node indicated by selector"""

    def insertHTMLAsFirstChild(selector, new_value):
        """Insert some HTML as the first childnode specified by selector"""

    def insertHTMLBefore(selector, new_value):
        """Insert some HTML before the node specified by selector"""

    def clearChildNodes(selector):
        """Remove all the child nodes from the node specified by selector"""

    def deleteNode(selector):
        """Remove the node itself specified by selector"""

    def deleteNodeAfter(selector):
        """Remove the node after the node specified by selector"""

    def deleteNodeBefore(selector):
        """Remove the node before the node specified by selector"""

    def copyChildNodesFrom(selector, id):
        """Copy the child nodes from the node specified by id to the selector node
        
        The copy operation will clear out all childnodes of selector."""

    def copyChildNodesTo(selector, id):
        """Copy the child nodes from the selector node to the node specified by id
        
        The copy operation will clear out all childnodes of selector."""

    def moveNodeAfter(selector, id):
        """Move the node indicated by selector to a sibling after id"""

    def setStateVar(varname, value):
        """Set a client side kukit variable"""

    def triggerEvent(name, **kw):
        """Trigger an event on the client """
        # TODO: explain a bit better what this does
