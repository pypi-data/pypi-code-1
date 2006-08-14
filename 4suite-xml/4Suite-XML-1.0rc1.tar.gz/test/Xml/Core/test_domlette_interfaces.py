#Test a domlette interface
from xml.dom import Node
from xml.dom import NamespaceErr
from Ft.Xml import XMLNS_NAMESPACE, EMPTY_NAMESPACE, Domlette, EMPTY_PREFIX, InputSource

def _test_simple_attribute(tester,name,dom,items,attrName = None):
    for tName,get,comp in items:
        tester.startTest("%s %s attribute" % (tName,name))
        if attrName:
            x = getattr(get,attrName)
        else:
            exec "x = " + get
        tester.compare(comp,x)
        tester.testDone()

def _test_simple_method(tester, name, dom, items, methodName=None):
    for tName,get,comp,args in items:
        tester.startTest("%s %s method" % (tName,name))
        if methodName:
            x = apply(getattr(get,methodName),args)
        else:
            exec "x = " + get
        tester.compare(comp,x)
        tester.testDone()

def test_node_access(tester,dom):

    tester.startGroup("Node Access Interfaces")

    _test_simple_attribute(tester, "childNodes", dom,
                           [('Document','len(dom.childNodes)',2),
                            ('Element','len(dom.documentElement.childNodes)',9),
                            ('Text','len(getFirstText(dom).childNodes)',0),
                            ('Comment','len(getComment(dom).childNodes)',0),
                            ('PI','len(getPi(dom).childNodes)',0),
                            ])

    _test_simple_attribute(tester,"nodeName",dom,
                           [('Document',dom,'#document'),
                            ('Element',getChild(dom),u'child'),
                            ('NsElement',getNsChild(dom),'ft:nschild'),
                            ('Text',getFirstText(dom),'#text'),
                            ('Comment',getComment(dom),'#comment'),
                            ('PI',getPi(dom),'xml-stylesheet'),
                            ('Attr',getAttr(dom),'foo'),
                            ('NsAttr',getNsAttr(dom),'ft:foo'),
                            ],attrName='nodeName')

    _test_simple_attribute(tester,"nodeValue",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),None),
                            ('Text',getFirstText(dom),'Some Text'),
                            ('Comment',getComment(dom),'A comment'),
                            ('PI',getPi(dom),'href="addr_book1.xsl" type="text/xml"'),
                            ('Attr',getAttr(dom),'bar'),
                            ],attrName='nodeValue')

    _test_simple_attribute(tester,"parentNode",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),dom.documentElement),
                            ('Text',getFirstText(dom),getChild(dom)),
                            ('Comment',getComment(dom),dom.documentElement),
                            ('PI',getPi(dom),dom),
                            ('Attr',getAttr(dom),getChild(dom)),
                            ],attrName='parentNode')

    _test_simple_attribute(tester,"firstChild",dom,
                           [('Document','dom.firstChild',getPi(dom)),
                            ('Element','getChild(dom).firstChild',getFirstText(dom)),
                            ('Text','getFirstText(dom).firstChild',None),
                            ('Comment','getComment(dom).firstChild',None),
                            ('PI','getPi(dom).firstChild',None),
                            ('Attr','getAttr(dom).firstChild',None),
                            ])

    _test_simple_attribute(tester,"lastChild",dom,
                           [('Document','dom.lastChild',dom.documentElement),
                            ('Element','getChild(dom).lastChild',getFirstText(dom)),
                            ('Text','getFirstText(dom).lastChild',None),
                            ('Comment','getComment(dom).lastChild',None),
                            ('PI','getPi(dom).lastChild',None),
                            ('Attr','getAttr(dom).lastChild',None),
                            ])

    _test_simple_attribute(tester,"previousSibling",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),dom.documentElement.childNodes[0]),
                            ('Text',getFirstText(dom),None),
                            ('Comment',getComment(dom),dom.documentElement.childNodes[2]),
                            ('PI',getPi(dom),None),
                            ('Attr',getAttr(dom),None),
                            ],attrName='previousSibling')

    _test_simple_attribute(tester,"nextSibling",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),dom.documentElement.childNodes[2]),
                            ('Text',getFirstText(dom),None),
                            ('Comment',getComment(dom),dom.documentElement.childNodes[4]),
                            ('PI',getPi(dom),dom.documentElement),
                            ('Attr',getAttr(dom),None),
                            ],attrName='nextSibling')

    _test_simple_attribute(tester,"attributes",dom,
                           [('Document','dom.attributes',None),
                            ('Element','len(getChild(dom).attributes.keys())',1),
                            ('Text','getFirstText(dom).attributes',None),
                            ('Comment','getComment(dom).attributes',None),
                            ('PI','getPi(dom).attributes',None),
                            ('Attr','getAttr(dom).attributes',None),
                            ])

    _test_simple_attribute(tester,"ownerDocument",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),dom),
                            ('Text',getFirstText(dom),dom),
                            ('Comment',getComment(dom),dom),
                            ('PI',getPi(dom),dom),
                            ('Attr',getAttr(dom),dom),
                            ],attrName='ownerDocument')

    _test_simple_attribute(tester,"namespaceURI",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),None),
                            ('NsElement',getNsChild(dom),'http://fourthought.com'),
                            ('Text',getFirstText(dom),None),
                            ('Comment',getComment(dom),None),
                            ('PI',getPi(dom),None),
                            ('Attr',getAttr(dom),None),
                            ('NsAttr',getNsAttr(dom),'http://fourthought.com'),
                            ],attrName='namespaceURI')

    _test_simple_attribute(tester,"prefix",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),None),
                            ('NsElement',getNsChild(dom),'ft'),
                            ('Text',getFirstText(dom),None),
                            ('Comment',getComment(dom),None),
                            ('PI',getPi(dom),None),
                            ('Attr',getAttr(dom),None),
                            ('NsAttr',getNsAttr(dom),'ft'),
                            ],attrName='prefix')

    _test_simple_attribute(tester,"localName",dom,
                           [('Document',dom,None),
                            ('Element',getChild(dom),'child'),
                            ('NsElement',getNsChild(dom),'nschild'),
                            ('Text',getFirstText(dom),None),
                            ('Comment',getComment(dom),None),
                            ('PI',getPi(dom),None),
                            ('Attr',getAttr(dom),'foo'),
                            ('NsAttr',getNsAttr(dom),'foo'),
                            ],attrName='localName')

    _test_simple_attribute(tester,"nodeType",dom,
                           [('Document',dom,Node.DOCUMENT_NODE),
                            ('Element',getChild(dom),Node.ELEMENT_NODE),
                            ('Text',getFirstText(dom),Node.TEXT_NODE),
                            ('Comment',getComment(dom),Node.COMMENT_NODE),
                            ('PI',getPi(dom),Node.PROCESSING_INSTRUCTION_NODE),
                            ('Attr',getAttr(dom),Node.ATTRIBUTE_NODE),
                            ],attrName='nodeType')

    _test_simple_method(tester,"hasChildNodes",dom,
                        [('Document',dom,1,()),
                         ('Element',getChild(dom),1,()),
                         ('Text',getFirstText(dom),0,()),
                         ('Comment',getComment(dom),0,()),
                         ('PI',getPi(dom),0,()),
                         ('Attr',getAttr(dom),0,()),
                         ],methodName='hasChildNodes')

    _test_simple_method(tester, "isSameNode", dom,
                        [('Document',dom,True,(dom,)),
                         ('Document',dom,False,(dom.documentElement,)),
                         ('Element',getChild(dom),True,(getChild(dom),)),
                         ('Element',getChild(dom),False,(dom.documentElement,)),
                         ('Text',getFirstText(dom),True,(getFirstText(dom),)),
                         ('Text',getFirstText(dom),False,(dom.documentElement,)),
                         ('Comment',getComment(dom),True,(getComment(dom),)),
                         ('Comment',getComment(dom),False,(dom.documentElement,)),
                         ('PI',getPi(dom),True,(getPi(dom),)),
                         ('PI',getPi(dom),False,(dom.documentElement,)),
                         ('Attr',getAttr(dom),True,(getAttr(dom),)),
                         ('Attr',getAttr(dom),False,(dom.documentElement,)),
                         ],
                        methodName='isSameNode')

    tester.groupDone()
    return


def test_document_access(tester,dom):

    tester.startGroup("Document Access Interfaces")

    tester.startTest("DocType")
    tester.compare(None,dom.doctype)
    tester.testDone()

    tester.startTest("documentElement")
    tester.compare(dom.childNodes[1],dom.documentElement)
    tester.testDone()

    tester.startTest("implementation")
    tester.compare(True, hasattr(dom.implementation,'hasFeature'))
    tester.testDone()

    tester.groupDone()

def test_element_access(tester,dom):

    tester.startGroup("Element Access Interfaces")

    tester.startTest("attributes")
    tester.compare(1,len(getChild(dom).attributes.keys()))
    tester.testDone()

    tester.startTest("tagname")
    tester.compare('child',getChild(dom).tagName)
    tester.compare('ft:nschild',getNsChild(dom).tagName)
    tester.testDone()

    tester.startTest("getAttributeNodeNS")
    tester.compare(None,getChild(dom).getAttributeNodeNS(None,u'foo2'))
    tester.compare(getAttr(dom),getChild(dom).getAttributeNodeNS(None,u'foo'))
    tester.compare(getNsAttr(dom),getNsChild(dom).getAttributeNodeNS('http://fourthought.com','foo'))
    tester.compare(None,getNsChild(dom).getAttributeNodeNS('http://fourthought.com','foo2'))
    tester.testDone()

    tester.startTest("getAttributeNS")
    tester.compare('bar',getChild(dom).getAttributeNS(None,'foo'))
    tester.compare('',getChild(dom).getAttributeNS(None,'foo2'))
    tester.compare('nsbar',getNsChild(dom).getAttributeNS('http://fourthought.com','foo'))
    tester.compare('',getNsChild(dom).getAttributeNS('http://fourthought.com','foo2'))
    tester.testDone()

    tester.startTest("hasAttributeNS")
    tester.compare(1,getChild(dom).hasAttributeNS(None,'foo'))
    tester.compare(0,getChild(dom).hasAttributeNS(None,'foo2'))
    tester.compare(1,getNsChild(dom).hasAttributeNS('http://fourthought.com','foo'))
    tester.compare(0,getNsChild(dom).hasAttributeNS('http://fourthought.com','foo2'))
    tester.testDone()

    tester.groupDone()


def test_attr_access(tester,dom):

    tester.startGroup("Attribute Access Interfaces")


    tester.startTest("name attribute")
    tester.compare('foo',getAttr(dom).name)
    tester.compare('ft:foo',getNsAttr(dom).name)
    tester.testDone()

    tester.startTest("value attribute")
    tester.compare('bar',getAttr(dom).value)
    tester.compare('nsbar',getNsAttr(dom).value)
    tester.testDone()

    tester.startTest("specified attribute")
    tester.compare(1,getAttr(dom).specified)
    tester.testDone()

    tester.startTest("ownerElement attribute")
    tester.compare(getChild(dom),getAttr(dom).ownerElement)
    tester.compare(getNsChild(dom),getNsAttr(dom).ownerElement)
    tester.testDone()

    tester.groupDone()

def test_text_access(tester,dom):

    tester.startGroup("Text Access Interfaces")


    tester.startTest("data attribute")
    tester.compare('Some Text',getFirstText(dom).data)
    tester.testDone()

    tester.startTest("substringData method")
    tester.compare('Some',getFirstText(dom).substringData(0,4))
    tester.testDone()


    tester.groupDone()

def test_pi_access(tester,dom):

    tester.startGroup("Processing Instruction Access Interfaces")


    tester.startTest("target attribute")
    tester.compare('xml-stylesheet',getPi(dom).target)
    tester.testDone()

    tester.startTest("data attribute")
    tester.compare('href="addr_book1.xsl" type="text/xml"',getPi(dom).data)
    tester.testDone()

    tester.groupDone()

def test_comment_access(tester,dom):

    tester.startGroup("Comment Access Interfaces")

    tester.startTest("data attribute")
    tester.compare('A comment',getComment(dom).data)
    tester.testDone()

    tester.groupDone()



def test_imp_creation(tester,dom):

    tester.startTest('createDocument (empty)')
    doc = dom.implementation.createDocument(None,None,None)
    tester.compare(Node.DOCUMENT_NODE,doc.nodeType)
    tester.compare(None, doc.doctype)
    tester.compare(None, doc.documentElement)
    tester.compare(0, doc.hasChildNodes())
    tester.testDone()

    tester.startTest('createDocument (element only)')
    doc = dom.implementation.createDocument('http://foo.com', 'foo:bar', None)
    tester.compare(Node.DOCUMENT_NODE,doc.nodeType)
    tester.compare(None, doc.doctype)
    tester.compare(1, doc.hasChildNodes())
    tester.compare(1, len(doc.childNodes))
    tester.compare(doc.documentElement, doc.childNodes[0])
    tester.compare(Node.ELEMENT_NODE, doc.childNodes[0].nodeType)
    tester.compare('http://foo.com', doc.childNodes[0].namespaceURI)
    tester.compare('foo', doc.childNodes[0].prefix)
    tester.compare('bar', doc.childNodes[0].localName)
    tester.testDone()
    return
    
def test_document_creation(tester,dom):

    tester.startGroup("Document Creation Interfaces")

    tester.startTest('createElementNS')
    elem = dom.createElementNS('http://foo.com','foo:bar')
    tester.compare(Node.ELEMENT_NODE,elem.nodeType)
    tester.compare('http://foo.com',elem.namespaceURI)
    tester.compare('foo',elem.prefix)
    tester.compare('bar',elem.localName)
    tester.compare('foo:bar',elem.nodeName)
    tester.compare(dom,elem.ownerDocument)
    tester.testDone()

    tester.startTest('createElementNS exceptions')
    tester.testException(dom.createElementNS, (None, 'foo:bar'), NamespaceErr)
    tester.testDone()

##    tester.startTest('createAttributeNs')
##    attr = dom.createAttributeNS('http://foo.com','foo:bar')
##    tester.compare(Node.ATTRIBUTE_NODE,attr.nodeType)
##    tester.compare('http://foo.com',attr.namespaceURI)
##    tester.compare('foo',attr.prefix)
##    tester.compare('bar',attr.localName)
##    tester.compare('foo:bar',attr.nodeName)
##    tester.compare(dom,attr.ownerDocument)
##    tester.testDone()
##
##    tester.startTest('createAttributeNS exceptions')
##    tester.testException(dom.createAttributeNS, (None, 'foo:bar'),
##                         NamespaceErr)
##    tester.testDone()



    tester.startTest('createTextNode')
    text = dom.createTextNode('data')
    tester.compare(Node.TEXT_NODE,text.nodeType)
    tester.compare('data',text.data)
    tester.compare(dom,text.ownerDocument)
    tester.testDone()

    tester.startTest('createProcessingInstruction')
    pi = dom.createProcessingInstruction('target','data')
    tester.compare(Node.PROCESSING_INSTRUCTION_NODE,pi.nodeType)
    tester.compare('target',pi.target)
    tester.compare('data',pi.data)
    tester.compare(dom,pi.ownerDocument)
    tester.testDone()

    tester.startTest('createComment')
    com = dom.createComment('data')
    tester.compare(Node.COMMENT_NODE,com.nodeType)
    tester.compare('data',com.data)
    tester.compare(dom,com.ownerDocument)
    tester.testDone()

##    tester.startTest('createDocumentFragment')
##    df = dom.createDocumentFragment()
##    tester.compare(Node.DOCUMENT_FRAGMENT_NODE,df.nodeType)
##    tester.compare(dom,df.ownerDocument)
##    tester.testDone()

    tester.groupDone()


def test_append_child(tester,dom):

    tester.startTest("Append Simple Child")
    elem = dom.createTextNode('data')
    child = getAppendChild(dom)
    child.appendChild(elem)
    tester.compare(1,len(child.childNodes))
    tester.compare(Node.TEXT_NODE,child.childNodes[0].nodeType)
    tester.compare('data',child.childNodes[0].data)
    tester.compare(child,elem.parentNode)
    tester.compare(elem,child.firstChild)
    tester.compare(elem,child.lastChild)
    tester.compare(None,elem.previousSibling)
    tester.compare(None,elem.nextSibling)
    tester.testDone()

    tester.startTest("Append Second Child")
    elem2 = dom.createTextNode('data2')
    child.appendChild(elem2)
    tester.compare(2,len(child.childNodes))
    tester.compare(Node.TEXT_NODE,child.childNodes[1].nodeType)
    tester.compare('data2',child.childNodes[1].data)
    tester.compare(child,elem2.parentNode)
    tester.compare(elem,child.firstChild)
    tester.compare(elem2,child.lastChild)
    tester.compare(None,elem.previousSibling)
    tester.compare(elem2,elem.nextSibling)
    tester.compare(elem,elem2.previousSibling)
    tester.compare(None,elem2.nextSibling)
    tester.testDone()


##    tester.startTest("Append DF")
##    df = dom.createDocumentFragment()
##    elem3 = dom.createTextNode('data3')
##    elem4 = dom.createTextNode('data4')
##    df.appendChild(elem3)
##    df.appendChild(elem4)
##    child.appendChild(df)
##    tester.compare(4,len(child.childNodes))
##    tester.compare(elem4,child.lastChild)
##    tester.compare(elem2,elem3.previousSibling)
##    tester.compare(elem4,elem3.nextSibling)
##    tester.compare(elem3,elem4.previousSibling)
##    tester.compare(None,elem4.nextSibling)
##    tester.compare(child,elem3.parentNode)
##    tester.compare(child,elem4.parentNode)
##    tester.testDone()


##    tester.startTest("Append DF to empty")
##    root = dom.createElementNS(None,'foo')
##    df = dom.createDocumentFragment()
##    elem5 = dom.createTextNode('data5')
##    elem6 = dom.createTextNode('data6')
##    df.appendChild(elem5)
##    df.appendChild(elem6)
##    root.appendChild(df)
##    tester.compare(2,len(root.childNodes))
##    tester.compare(elem5,root.firstChild)
##    tester.compare(elem6,root.lastChild)
##    tester.compare(None,elem5.previousSibling)
##    tester.compare(elem6,elem5.nextSibling)
##    tester.compare(elem5,elem6.previousSibling)
##    tester.compare(None,elem6.nextSibling)
##    tester.compare(root,elem5.parentNode)
##    tester.compare(root,elem6.parentNode)
##    tester.testDone()

    tester.startTest("Append New Element to a new document")
    newdoc = dom.implementation.createDocument(None,None,None)
    elem10 = newdoc.createElementNS(None,'foo')
    newdoc.appendChild(elem10)
    tester.compare(elem10,newdoc.documentElement)
    tester.testDone()

def test_normalize(tester,dom):
    tester.startGroup("Normalize")
    tester.startTest("Normalize All Text Nodes")
    child = getAppendChild(dom)
    child.normalize()
    tester.compare(1,len(child.childNodes))
    tester.compare("datadata2data3data4",child.childNodes[0].data)
    tester.testDone()

    tester.startTest("Normalize Mixed Text Nodes")
    child = getAppendChild(dom)
    sub1 = dom.createElementNS(None,'one')
    sub2 = dom.createElementNS(None,'two')
    t1 = dom.createTextNode('o')
    t2 = dom.createTextNode('t')
    t3 = dom.createTextNode('g')
    t4 = dom.createTextNode('h')
    child.appendChild(t1)
    child.appendChild(sub1)
    child.appendChild(t2)
    child.appendChild(t3)
    child.appendChild(sub2)
    child.appendChild(t4)
    child.normalize()
    tester.compare(5,len(child.childNodes))
    tester.compare("datadata2data3data4o",child.childNodes[0].data)
    tester.compare("tg",child.childNodes[2].data)
    tester.compare("h",child.childNodes[4].data)
    tester.testDone()

    tester.groupDone()


def test_insert_before(tester,dom):

    tester.startTest("Empty Insert")
    elem = dom.createTextNode('data')
    child = dom.createElementNS(None,'insertTest')
    child.insertBefore(elem,None)
    tester.compare(1,len(child.childNodes))
    tester.compare(child,elem.parentNode)
    tester.compare(Node.TEXT_NODE,child.childNodes[0].nodeType)
    tester.compare('data',child.childNodes[0].data)
    tester.compare(child,elem.parentNode)
    tester.compare(elem,child.firstChild)
    tester.compare(elem,child.lastChild)
    tester.compare(None,elem.previousSibling)
    tester.compare(None,elem.nextSibling)
    tester.testDone()

    tester.startTest("Second Insert")
    elem2 = dom.createTextNode('data2')
    child.insertBefore(elem2,elem)
    tester.compare(2,len(child.childNodes))
    tester.compare(child,elem2.parentNode)
    tester.compare(Node.TEXT_NODE,child.childNodes[0].nodeType)
    tester.compare('data2',child.childNodes[0].data)
    tester.compare(child,elem2.parentNode)
    tester.compare(elem2,child.firstChild)
    tester.compare(elem,child.lastChild)
    tester.compare(elem2,elem.previousSibling)
    tester.compare(None,elem.nextSibling)
    tester.compare(None,elem2.previousSibling)
    tester.compare(elem,elem2.nextSibling)
    tester.testDone()

##    tester.startTest("DF Insert")
##    df = dom.createDocumentFragment()
##    elem3 = dom.createTextNode('data3')
##    elem4 = dom.createTextNode('data4')
##    df.appendChild(elem3)
##    df.appendChild(elem4)
##    child.insertBefore(df,elem)

##    tester.compare(4,len(child.childNodes))
##    tester.compare(child,elem3.parentNode)
##    tester.compare(child,elem4.parentNode)
##    tester.compare(elem2,child.firstChild)
##    tester.compare(elem,child.lastChild)

##    tester.compare(None,elem2.previousSibling)
##    tester.compare(elem3,elem2.nextSibling)
##    tester.compare(elem2,elem3.previousSibling)
##    tester.compare(elem4,elem3.nextSibling)
##    tester.compare(elem3,elem4.previousSibling)
##    tester.compare(elem,elem4.nextSibling)
##    tester.compare(elem4,elem.previousSibling)
##    tester.compare(None,elem.nextSibling)
##    tester.testDone()

##    tester.startTest("DF Insert on empty")
##    root = dom.createElementNS(None,'foo')
##    df = dom.createDocumentFragment()
##    elem5 = dom.createTextNode('data5')
##    elem6 = dom.createTextNode('data6')
##    df.appendChild(elem5)
##    df.appendChild(elem6)
##    root.insertBefore(df,None)
##    tester.compare(2,len(root.childNodes))
##    tester.compare(elem5,root.firstChild)
##    tester.compare(elem6,root.lastChild)
##    tester.compare(None,elem5.previousSibling)
##    tester.compare(elem6,elem5.nextSibling)
##    tester.compare(elem5,elem6.previousSibling)
##    tester.compare(None,elem6.nextSibling)
##    tester.compare(root,elem5.parentNode)
##    tester.compare(root,elem6.parentNode)
##    tester.testDone()

    tester.startTest("Insert on empty doc")
    newdoc = dom.implementation.createDocument(None,None,None)
    com = newdoc.createComment('foo')
    elem10 = newdoc.createElementNS(None,'foo')
    newdoc.appendChild(com)
    newdoc.insertBefore(elem10,com)
    tester.compare(elem10,newdoc.documentElement)
    tester.testDone()


def test_replace_child(tester,dom):

    tester.startTest("Simple Replace")

    root = dom.createElementNS(None,'root')
    elem = dom.createElementNS(None,'elem')
    elem2 = dom.createElementNS(None,'elem2')

    root.appendChild(elem)
    root.replaceChild(elem2,elem)

    tester.compare(1,len(root.childNodes))
    tester.compare(elem2,root.firstChild)
    tester.compare(elem2,root.lastChild)
    tester.compare(None,elem.parentNode)
    tester.compare(None,elem2.nextSibling)
    tester.compare(None,elem2.previousSibling)
    tester.compare(None,elem.nextSibling)
    tester.compare(None,elem.previousSibling)
    tester.testDone()


    tester.startTest("Replace on doc")
    newdoc = dom.implementation.createDocument(None,None,None)
    com = newdoc.createComment('foo')
    elem10 = newdoc.createElementNS(None,'foo')
    newdoc.appendChild(com)
    newdoc.replaceChild(elem10,com)
    tester.compare(elem10,newdoc.documentElement)
    tester.testDone()


def test_remove_child(tester,dom):

    tester.startTest("Simple Remove")

    root = dom.createElementNS(None,'root')
    elem = dom.createElementNS(None,'elem')

    root.appendChild(elem)
    root.removeChild(elem)

    tester.compare(0,len(root.childNodes))
    tester.compare(None,root.firstChild)
    tester.compare(None,root.lastChild)
    tester.compare(None,elem.parentNode)
    tester.compare(None,elem.previousSibling)
    tester.compare(None,elem.nextSibling)
    tester.testDone()

    tester.startTest("Remove on doc")
    newdoc = dom.implementation.createDocument(None,None,None)
    elem10 = newdoc.createElementNS(None,'foo')
    newdoc.appendChild(elem10)
    newdoc.removeChild(elem10)
    tester.compare(None,newdoc.documentElement)
    tester.testDone()


def test_node_modification(tester,dom):

    tester.startGroup("Node Modiciation Interfaces")
    ##test_append_child(tester,dom)
    ##test_normalize(tester,dom)
    ##test_insert_before(tester,dom)
    ##test_replace_child(tester,dom)
    ##test_remove_child(tester,dom)
    tester.groupDone()

def test_element_modification(tester,dom):

    tester.startGroup("Element Modiciation Interfaces")

    tester.startTest("setAttributeNS non-NS attr")
    root = dom.createElementNS(None,'foo')
    root.setAttributeNS(None,'foo','bar')
    tester.compare(True, root.hasAttributeNS(None,'foo'))
    attr = root.getAttributeNodeNS(None,'foo')
    tester.compare(EMPTY_NAMESPACE, attr.namespaceURI)
    tester.compare(EMPTY_PREFIX, attr.prefix)
    tester.compare('foo', attr.localName)
    tester.compare('foo', attr.nodeName)
    tester.compare('foo', attr.name)
    tester.compare('bar', attr.nodeValue)
    tester.compare('bar', attr.value)
    tester.testDone()


    tester.startTest("setAttributeNS NS attr")
    root.setAttributeNS('http://fourthought.com','ft:foo','bar')
    tester.compare(True, root.hasAttributeNS('http://fourthought.com','foo'))
    attr = root.getAttributeNodeNS('http://fourthought.com','foo')
    tester.compare('http://fourthought.com',attr.namespaceURI)
    tester.compare('ft',attr.prefix)
    tester.compare('foo',attr.localName)
    tester.compare('ft:foo',attr.nodeName)
    tester.compare('ft:foo',attr.name)
    tester.compare('bar',attr.nodeValue)
    tester.compare('bar',attr.value)
    tester.testDone()


##    tester.startTest("setAttributeNodeNS NS attr")
##    attr = dom.createAttributeNS('http://fourthought.com','ft:foo2')
##    attr.value = 'bar'
##    root.setAttributeNodeNS(attr)
##    tester.compare(True, root.hasAttributeNS('http://fourthought.com','foo2'))
##    attr = root.getAttributeNodeNS('http://fourthought.com','foo2')
##    tester.compare('http://fourthought.com',attr.namespaceURI)
##    tester.compare('ft',attr.prefix)
##    tester.compare('foo2',attr.localName)
##    tester.compare('ft:foo2',attr.nodeName)
##    tester.compare('ft:foo2',attr.name)
##    tester.compare('bar',attr.nodeValue)
##    tester.compare('bar',attr.value)
##    tester.testDone()

##    tester.startTest("setAttributeNodeNS non-NS attr")
##    attr = dom.createAttributeNS(None,'foo2')
##    attr.value = 'bar'
##    root.setAttributeNodeNS(attr)
##    tester.compare(True, root.hasAttributeNS(None,'foo2'))
##    attr = root.getAttributeNodeNS(None,'foo2')
##    tester.compare(None,attr.namespaceURI)
##    tester.compare(None, attr.prefix)
##    tester.compare('foo2',attr.localName)
##    tester.compare('foo2',attr.nodeName)
##    tester.compare('foo2',attr.name)
##    tester.compare('bar',attr.nodeValue)
##    tester.compare('bar',attr.value)
##    tester.testDone()


    tester.startTest("removeAttributeNode NS attr")
    root.setAttributeNS('http://fourthought.com', 'ft:foo2', 'bar')
    attr = root.getAttributeNodeNS('http://fourthought.com','foo2')
    root.removeAttributeNode(attr)
    tester.compare(False, root.hasAttributeNS('http://fourthought.com','foo2'))
    tester.testDone()

    tester.startTest("removeAttributeNode non-NS attr")
    root.setAttributeNS(None, 'foo2', 'bar')
    attr = root.getAttributeNodeNS(None,'foo2')
    root.removeAttributeNode(attr)
    tester.compare(False, root.hasAttributeNS(None,'foo2'))
    tester.testDone()


    tester.startTest("removeAttributeNS NS attr")
    root.removeAttributeNS('http://fourthought.com','foo')
    tester.compare(False, root.hasAttributeNS('http://fourthought.com','foo'))
    tester.testDone()

    tester.startTest("removeAttributeNS non-NS attr")
    root.removeAttributeNS(None,'foo')
    tester.compare(False, root.hasAttributeNS(None,'foo'))
    tester.testDone()
    tester.groupDone()

def test_text_modification(tester,dom):

    tester.startGroup("Text Modification")
    tester.startTest("set value")
    text = dom.createTextNode('data')
    text.data = 'new data'
    tester.compare('new data',text.data)
    tester.compare('new data',text.nodeValue)
    tester.testDone()

    tester.startTest("insertData")
    text.insertData(3,'f')
    tester.compare('newf data',text.data)
    tester.testDone()

    tester.startTest('appendData')
    text.appendData('g')
    tester.compare('newf datag',text.data)
    tester.testDone()
    
    tester.startTest('deleteData')
    text.deleteData(1,3)
    tester.compare('n datag',text.data)
    tester.testDone()

    tester.startTest('substringData')
    d = text.substringData(1,3)
    tester.compare(' da',d)
    tester.testDone()
    tester.groupDone()


def test_comment_modification(tester,dom):

    tester.startGroup("Comment Modification")
    tester.startTest("set value")
    comment = dom.createComment('data')
    comment.data = 'new data'
    tester.compare('new data',comment.data)
    tester.compare('new data',comment.nodeValue)
    tester.testDone()

    tester.startTest("insertData")
    comment.insertData(3,'f')
    tester.compare('newf data',comment.data)
    tester.testDone()

    tester.startTest('appendData')
    comment.appendData('g')
    tester.compare('newf datag',comment.data)
    tester.testDone()
    
    tester.startTest('deleteData')
    comment.deleteData(1,3)
    tester.compare('n datag',comment.data)
    tester.testDone()

    tester.startTest('substringData')
    d = comment.substringData(1,3)
    tester.compare(' da',d)
    tester.testDone()
    tester.groupDone()


def test_processing_instruction_modification(tester,dom):

    tester.startGroup("Processing Instruction Modification")
    pi = dom.createProcessingInstruction('target','data')

    tester.startTest("set data")
    pi.data = 'new data'
    tester.compare('new data',pi.data)
    tester.compare('new data',pi.nodeValue)
    tester.testDone()

    tester.groupDone()


def test_interface(tester,domMod):
    tester.startGroup("Dom Module Interface")

    tester.startTest("TestTree")
    tester.compare(True, hasattr(domMod,'TestTree'))
    dom = domMod.TestTree()
    tester.compare('docelem',dom.documentElement.nodeName)
    tester.testDone()

    tester.startTest("ValParse")
    tester.compare(True, hasattr(domMod,'ValParse'))
    tester.testDone()

    tester.startTest("NonvalParse")
    tester.compare(True, hasattr(domMod,'NonvalParse'))
    tester.testDone()

    tester.groupDone()
    return


def test_access(tester,domMod):
    tester.startGroup("Access Interfaces")
    dom = domMod.TestTree()
    test_node_access(tester,dom)
    test_document_access(tester,dom)
    test_element_access(tester,dom)
    test_attr_access(tester,dom)
    test_text_access(tester,dom)
    test_pi_access(tester,dom)
    test_comment_access(tester,dom)
    tester.groupDone()
    return


def test_reader_access(tester,domMod,doc):
    tester.startGroup("Access Interfaces after parsing")
    isrc = InputSource.DefaultFactory.fromString(doc,'reader')
    dom = domMod.NonvalParse(isrc)
    test_node_access(tester, dom)
    test_document_access(tester, dom)
    test_element_access(tester, dom)
    test_attr_access(tester, dom)
    test_text_access(tester, dom)
    test_pi_access(tester, dom)
    test_comment_access(tester, dom)
    tester.groupDone()
    return

def test_clone_node(tester,domMod):
    tester.startGroup("cloneNode")
    dom = domMod.TestTree()
    tester.startTest("shallow")

    newNode = dom.documentElement.cloneNode(0)

    tester.compare('docelem',newNode.nodeName)
    tester.compare(None,newNode.namespaceURI)
    tester.compare('docelem',newNode.localName)
    tester.compare(0,len(newNode.childNodes))
    tester.compare(1,len(newNode.attributes))
    tester.compare(True, newNode.attributes.has_key((XMLNS_NAMESPACE, 'ft')))
    tester.compare('http://fourthought.com',newNode.attributes[(XMLNS_NAMESPACE, 'ft')].value)
    tester.testDone()

    tester.startTest("deep")
    newNode = getChild(dom).cloneNode(1)
    tester.compare('child',newNode.nodeName)
    tester.compare(None,newNode.namespaceURI)
    tester.compare('child',newNode.localName)
    tester.compare(1,len(newNode.childNodes))
    tester.compare(True, hasattr(newNode.childNodes[0],'data'))
    tester.compare('Some Text',newNode.childNodes[0].data)
    tester.compare(1,len(newNode.attributes))
    tester.compare(True, newNode.attributes.has_key((EMPTY_NAMESPACE, 'foo')))
    tester.compare('bar',newNode.attributes[(EMPTY_NAMESPACE, 'foo')].value)
    tester.testDone()

    tester.groupDone()
    return


def test_import_node(tester,domMod):

    tester.startTest("importNode deep")

    dom = domMod.TestTree()

    doc = Domlette.implementation.createDocument(None,None,None)
    root = doc.createElementNS("http://foo.com","foo:import-root")
    root.setAttributeNS(EMPTY_NAMESPACE,"ID","15")
    text = doc.createTextNode("Imported Text")
    root.appendChild(text)
    

    newRoot = dom.importNode(root,1)

    tester.compare(dom,newRoot.ownerDocument)
    tester.compare(dom,newRoot.childNodes[0].ownerDocument)
    tester.testDone()
    return


def test_mutate(tester,domMod):
    tester.startGroup("Mutation Interfaces")
    dom = domMod.TestTree()
    test_imp_creation(tester, dom)
    test_document_creation(tester, dom)
    test_node_modification(tester, dom)
    test_element_modification(tester, dom)
    test_text_modification(tester, dom)
    test_comment_modification(tester, dom)
    test_processing_instruction_modification(tester, dom)
    test_clone_node(tester, domMod)
    test_import_node(tester, domMod)
    tester.groupDone()
    return


#into the docs children
def getPi(dom):
    return dom.childNodes[0]

def getChild(dom):
    return dom.documentElement.childNodes[1]

def getNsChild(dom):
    return dom.documentElement.childNodes[5]

def getFirstText(dom):
    return getChild(dom).childNodes[0]

def getComment(dom):
    return dom.documentElement.childNodes[3]

def getAttr(dom):
    child = getChild(dom)
    return child.attributes[child.attributes.keys()[0]]

def getNsAttr(dom):
    child = getNsChild(dom)
    return child.attributes[child.attributes.keys()[0]]

def getAppendChild(dom):
    return dom.documentElement.childNodes[7]


