"""
$Id: test_security.py 3965 2006-01-26 13:50:03Z sidnei $
"""

import unittest
from snap.interface import ILocalRoles
from snap.adapter import PrincipalRoleMap

from zope.testing.doctestunit import DocFileSuite
from zope.security.management import endInteraction
from zope.app import zapi
from zope.app.testing import placelesssetup, ztapi
from zope.app.securitypolicy.interfaces import IPrincipalRoleMap

def setUp(test):
    placelesssetup.setUp()
    endInteraction()
    ztapi.provideAdapter(
        ILocalRoles, IPrincipalRoleMap,
        PrincipalRoleMap)

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('security.txt',
                     package='snap.tests',
                     setUp=setUp, tearDown=placelesssetup.tearDown),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
