# -*- coding: utf-8 -*-
import formencode

import os

ne = formencode.validators.NotEmpty()

def _test_builtins(func):
  def dummy(s):
    return "builtins dummy"
  import __builtin__
  __builtin__._ = dummy

  try:
      ne.to_python("")
  except formencode.api.Invalid, e:
    func(e)
  
  del __builtin__._

def test_builtins():
  def withbuiltins(e):
      assert str(e) == "builtins dummy"
    
  _test_builtins(withbuiltins)


def test_bultins_disabled():
  def withoutbuiltins(e):
      assert str(e) <> "builtins dummy"
      
  ne.use_builtins_gettext = False
  _test_builtins(withoutbuiltins)



def test_state():
  class st(object):
    def _(self, s):
      return "state dummy"
  
  try:
    ne.to_python("", state=st())
  except formencode.api.Invalid, e:
    assert str(e) == "state dummy"

  
def _test_lang(language, notemptytext):

  formencode.api.set_stdtranslation(languages=[language])
 
  try:
    ne.to_python("")
  except formencode.api.Invalid, e:
    assert unicode(e) == notemptytext
  
  formencode.api.set_stdtranslation() #set back to defaults

    
def test_de():
  _test_lang("de", u"Bitte einen Wert eingeben")

def test_es():
  _test_lang("es", u"Por favor introduzca un valor")

def test_pt_BR():
  _test_lang("pt_BR", u"Por favor digite um valor")

def test_big5():
  _test_lang("big5", u"請輸入一個值")

def test_sk():
  _test_lang("sk",u"Zadajte hodnotu, prosím")

def test_ru():
  _test_lang("ru",u"Необходимо ввести значение")

def test_sl():
  _test_lang("sl",u"Prosim, izpolnite polje")

def test_pt_PT():
  _test_lang("pt_PT", u"Por favor insira um valor")

def test_fr():
  _test_lang("fr", u"Veuillez entrer une valeur")
