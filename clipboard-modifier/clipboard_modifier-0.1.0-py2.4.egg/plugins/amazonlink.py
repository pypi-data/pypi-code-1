#!/usr/bin/env python
# -*- encoding: latin1 -*-
#
# Copyright 2007 Scott Kirkwood

from _plugin import ClipboardPlugin, TestPlugin
import re

def create_plugin():
  return AmazonLink()
  
class AmazonLink(ClipboardPlugin):
  def __init__(self):
    ClipboardPlugin.__init__(self)
    self.associate_id = 'softwareforusers'

  def name(self):
    return 'Amazon Associates URL'
  
  def description(self):
    return 'Convert an amazon URL so that it has the Associates ID in it'

  def convert(self, text):
    """ Convert an http:// link to an amazon style link
    
    Returns text (url)
    """
    base_url = 'http://www.amazon.com/exec/obidos/ASIN'
    re_asin = re.compile(r'/([A-Z0-9]{10})/')
    args = re_asin.search(text)
    if not args:
      return self._ret_result("Didn't find 10 digit ASIN in link", False, "")
    asin = args.group(1)
    return self._ret_result("Created URL", True, '%s/%s/?tag=%s' % (base_url, asin, self.associate_id))

class TestAmazonLink(TestPlugin):
  def setUp(self):
    self.instance = AmazonLink()
    
  def test_good(self):
    good_samples = [
      ("http://amazon.com/o/ASIN/0201485419/ref=s9_asin_image_2-hf_favarpcbss_2238_p/102-1722741-9600945?%5Fencoding=UTF8&coliid=I1B1K3406DXXD8&colid=3TDODZYOX7Y6Z&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-2&pf_rd_r=07G7DSC9Q3E0C50S0FQM&pf_rd_t=101&pf_rd_p=279438701&pf_rd_i=507846",
      "http://www.amazon.com/exec/obidos/ASIN/0201485419/?tag=softwareforusers"
      ),
      ("http://amazon.com/Nintendo-RVLSWCUSZ-Wii/dp/B0009VXBAQ/ref=pd_ys_qtk_shop/102-1722741-9600945?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=center-1&pf_rd_r=1MXPWA8MWGFQ9K6G8JHT&pf_rd_t=1501&pf_rd_p=186414001&pf_rd_i=home",
      "http://www.amazon.com/exec/obidos/ASIN/B0009VXBAQ/?tag=softwareforusers"
      ),
    ]
    self.verify_good_samples(good_samples, "Created URL")

  def test_bad(self):
    bad_samples = [
      "bob",
      "",
    ]
    self.verify_bad_samples(bad_samples)
    
if __name__ == "__main__":
  import unittest
  unittest.main()
