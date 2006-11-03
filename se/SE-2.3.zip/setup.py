
from distutils.core import setup



classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: Open Source',
          'Operating System :: any',
          'Programming Language :: Python',
          'Topic :: Software Development :: Bug Tracking',
          ],



long_description = '''Description: A Python stream editor with these characteristics:

   1. Does any (practical) number of search-and-replaces in one pass.
   2. Does any (practical) number of passes in one run.
   3. Handles all 256 octets.
   4. Does regular expressions.
   5. Notational conveniences.
   6. Compiles substitution sets defined in the form of a string.
   7. Compiles substitution sets edited and kept in text files.
   8. Naming a file in a definition string inserts the file's contents in
      the place of its name, making for a modular building-block system.
   9. Naming files is recursive. Files may pull in other files.
  10. Constructor compiles definitions into an Editor object that will
      translate any input.
  11. Accepts input as string, file object or file by name. Outputs any of
      these types, matching type by default.
  12. Overwrite-safe. In-place edits switch name only and keep original data
      with a backup extension.
  13. Method set () to change runtime parameters.
  14. Method show () for object inspection.
  15. Methods save (), add (), drop () and reverse () for interactive edits.
  16. Optional retention and display of intermediate data with chained passes.
  17. Method show_log () displays a list of accumulated glitches and potential
      glitches, mainly about IO operations.
  18. A Light version (SEL) without interaction except for set () and
      show_log ().
  19. Method se.SEL () returns a light version of se. Constructor SE.SE (sel)
      takes a Light editor object instead of substitutions and makes an
      interactive one from it.
  20. An extensive manual: SE-DOC.HTM.
  21. An example definition file: htm2iso.se. Converts htm-ampersand escapes
      to characters.
  22. A demo script walking through the examples in SE-DOC.HTM.
  23. FORMEX.py: A derivation for editing complex arithmetic formulas
interactively in any order and executing them.
'''



setup (name='SE',
       version='2.3',
       author='Frederic Rentsch',
       author_email='anthra.norell@vtxmail.ch',
       maintainer='Frederic Rentsch',
       maintainer_email='anthra.norell@vtxmail.ch',
       description='A Stream Editor. Compiles free-text substitution sets into Editor Objects which will translate files, file objects or strings. Modular design. Handles all 256 octets. Simple and quick usage.',
       classifiers=classifiers,
       long_description=long_description,
       data_files=[('SE-2.3', ['readme','se-demo.py','se-doc.htm','htm2iso.se'])],
       py_modules=['SEL', 'SE', 'FORMEX'],
       keywords=['stream editor','command line','filter','deletion filter','extraction filter','search and replace','find and substitute','multiple replace','multiple pass','modular concept','text editing','word processing'],  
      )    
