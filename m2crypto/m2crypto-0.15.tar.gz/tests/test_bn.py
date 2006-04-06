#!/usr/bin/env python

"""
Unit tests for M2Crypto.BN.

Copyright (c) 2005 Open Source Applications Foundation. All rights reserved.
"""

RCS_id = '$Id: test_bn.py 287 2005-06-03 19:02:38Z heikki $'

import unittest, re
from M2Crypto import BN, Rand

loops = 16

class BNTestCase(unittest.TestCase):

    def check_rand(self):
        # defaults
        for x in range(loops):
            r8 = BN.rand(8)
        
        # top
        for x in range(loops):
            r8 = BN.rand(8, top=0)
            assert r8 & 128
        for x in range(loops):
            r8 = BN.rand(8, top=1)
            assert r8 & 192
        
        # bottom
        for x in range(loops):
            r8 = BN.rand(8, bottom=1)
            assert r8 % 2 == 1

        # make sure we can get big numbers and work with them
        for x in range(loops):
            r8 = BN.rand(8, top=0)
            r16 = BN.rand(16, top=0)
            r32 = BN.rand(32, top=0)
            r64 = BN.rand(64, top=0)
            r128 = BN.rand(128, top=0)
            r256 = BN.rand(256, top=0)
            r512 = BN.rand(512, top=0)
            assert r8 < r16 < r32 < r64 < r128 < r256 < r512 < (r512 + 1)
        

    def check_rand_range(self):
        # small range
        for x in range(loops):
            r = BN.rand_range(1)
            assert r == 0
        
        for x in range(loops):
            r = BN.rand_range(4)
            assert 0 <= r < 4
        
        # large range
        r512 = BN.rand(512, top=0)
        for x in range(loops):
            r = BN.rand_range(r512)
            assert 0 <= r < r512

            
    def check_randfname(self):
        m = re.compile('^[a-zA-Z0-9]{8}$')
        for x in range(loops):
            r = BN.randfname(8)
            assert m.match(r)
        

def suite():
    return unittest.makeSuite(BNTestCase, 'check')


if __name__ == '__main__':
    Rand.load_file('randpool.dat', -1) 
    unittest.TextTestRunner().run(suite())
    Rand.save_file('randpool.dat')

