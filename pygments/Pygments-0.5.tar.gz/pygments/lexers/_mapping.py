# -*- coding: utf-8 -*-
"""
    pygments.lexers._mapping
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexer mapping defintions. This file is generated by itself. Everytime
    you change something on a builtin lexer defintion, run this script from
    the lexers folder to update it.

    Do not alter the LEXERS dictionary by hand.

    :copyright: 2006 by Armin Ronacher, Georg Brandl.
    :license: GNU LGPL, see LICENSE for more details.
"""

LEXERS = {
    'BooLexer': ('pygments.lexers.dotnet', 'Boo', ('boo',), ('*.boo',), ('text/x-boo',)),
    'BrainfuckLexer': ('pygments.lexers.other', 'Brainfuck', ('bf', 'brainfuck'), ('*.b', '*.bf'), ()),
    'CLexer': ('pygments.lexers.compiled', 'C', ('c',), ('*.c', '*.h'), ('text/x-chdr', 'text/x-csrc')),
    'CSharpLexer': ('pygments.lexers.dotnet', 'C#', ('c#', 'csharp'), ('*.cs',), ('text/x-csharp',)),
    'CppLexer': ('pygments.lexers.compiled', 'C++', ('cpp', 'c++'), ('*.c++', '*.hpp', '*.cpp', '*.h++'), ('text/x-c++hdr', 'text/x-c++src')),
    'CssDjangoLexer': ('pygments.lexers.templates', 'CSS+Django/Jinja', ('css+jinja', 'css+django'), (), ()),
    'CssErbLexer': ('pygments.lexers.templates', 'CSS+Ruby', ('css+ruby', 'css+erb'), (), ()),
    'CssGenshiLexer': ('pygments.lexers.templates', 'CSS+Genshi Text', ('css+genshi', 'css+genshitext'), (), ()),
    'CssLexer': ('pygments.lexers.web', 'CSS', ('css',), ('*.css',), ('text/css',)),
    'CssPhpLexer': ('pygments.lexers.templates', 'CSS+PHP', ('css+php',), (), ()),
    'CssSmartyLexer': ('pygments.lexers.templates', 'CSS+Smarty', ('css+smarty',), (), ()),
    'DelphiLexer': ('pygments.lexers.compiled', 'Delphi', ('objectpascal', 'delphi', 'pas', 'pascal'), ('*.pas',), ('text/x-pascal',)),
    'DiffLexer': ('pygments.lexers.text', 'Diff', ('diff',), ('*.diff', '*.patch'), ('text/x-diff',)),
    'DjangoLexer': ('pygments.lexers.templates', 'Django/Jinja', ('jinja', 'django'), (), ()),
    'ErbLexer': ('pygments.lexers.templates', 'ERB', ('erb',), (), ()),
    'GenshiLexer': ('pygments.lexers.templates', 'Genshi', ('xml+kid', 'xml+genshi', 'genshi', 'kid'), ('*.kid',), ()),
    'GenshiTextLexer': ('pygments.lexers.templates', 'Genshi Text', ('genshitext',), (), ()),
    'HtmlDjangoLexer': ('pygments.lexers.templates', 'HTML+Django/Jinja', ('html+jinja', 'html+django'), (), ()),
    'HtmlGenshiLexer': ('pygments.lexers.templates', 'HTML+Genshi', ('html+genshi', 'html+kid'), (), ()),
    'HtmlLexer': ('pygments.lexers.web', 'HTML', ('html',), ('*.xhtml', '*.html', '*.htm'), ('text/html', 'application/xhtml+xml')),
    'HtmlPhpLexer': ('pygments.lexers.templates', 'HTML+PHP', ('html+php',), ('*.phtml',), ('text/x-php', 'application/x-php', 'application/x-httpd-php', 'application/x-httpd-php3', 'application/x-httpd-php4', 'application/x-httpd-php5')),
    'HtmlSmartyLexer': ('pygments.lexers.templates', 'HTML+Smarty', ('html+smarty',), (), ()),
    'IniLexer': ('pygments.lexers.text', 'INI', ('cfg', 'ini'), ('*.ini', '*.cfg'), ()),
    'IrcLogsLexer': ('pygments.lexers.text', 'IRC logs', ('irc',), (), ()),
    'JavaLexer': ('pygments.lexers.compiled', 'Java', ('java',), ('*.java',), ('text/x-java',)),
    'JavascriptDjangoLexer': ('pygments.lexers.templates', 'JavaScript+Django/Jinja', ('javascript+django', 'js+jinja', 'javascript+jinja', 'js+django'), (), ()),
    'JavascriptErbLexer': ('pygments.lexers.templates', 'JavaScript+Ruby', ('javascript+ruby', 'javascript+erb', 'js+ruby', 'js+erb'), (), ()),
    'JavascriptGenshiLexer': ('pygments.lexers.templates', 'JavaScript+Genshi Text', ('javascript+genshitext', 'javascript+genshi', 'js+genshitext', 'js+genshi'), (), ()),
    'JavascriptLexer': ('pygments.lexers.web', 'JavaScript', ('javascript', 'js'), ('*.js',), ('application/x-javascript', 'text/x-javascript')),
    'JavascriptPhpLexer': ('pygments.lexers.templates', 'JavaScript+PHP', ('js+php', 'javascript+php'), (), ()),
    'JavascriptSmartyLexer': ('pygments.lexers.templates', 'JavaScript+Smarty', ('javascript+smarty', 'js+smarty'), (), ()),
    'LuaLexer': ('pygments.lexers.agile', 'Lua', ('lua',), ('*.lua',), ('text/x-lua', 'application/x-lua')),
    'MakefileLexer': ('pygments.lexers.text', 'Makefile', ('make', 'mf', 'makefile'), ('Makefile', '*.mak', 'makefile'), ('text/x-makefile',)),
    'PerlLexer': ('pygments.lexers.agile', 'Perl', ('pl', 'perl'), ('*.pl', '*.pm'), ('text/x-perl', 'application/x-perl')),
    'PhpLexer': ('pygments.lexers.web', 'PHP', ('php4', 'php5', 'php', 'php3'), ('*.php', '*.php[345]'), ()),
    'PythonConsoleLexer': ('pygments.lexers.agile', 'Python console session', ('pycon',), (), ()),
    'PythonLexer': ('pygments.lexers.agile', 'Python', ('python', 'py'), ('*.pyw', '*.py'), ('text/x-python', 'application/x-python')),
    'RawTokenLexer': ('pygments.lexers.special', 'Raw token data', ('raw',), ('*.raw',), ('application/x-pygments-tokens',)),
    'RhtmlLexer': ('pygments.lexers.templates', 'RHTML', ('html+ruby', 'rhtml', 'html+erb'), ('*.rhtml',), ()),
    'RubyConsoleLexer': ('pygments.lexers.agile', 'Ruby irb session', ('irb', 'rbcon'), (), ()),
    'RubyLexer': ('pygments.lexers.agile', 'Ruby', ('ruby', 'rb'), ('*.rb', '*.rbx', '*.gemspec', 'Rakefile', '*.rake', '*.rbw'), ('text/x-ruby', 'application/x-ruby')),
    'SmartyLexer': ('pygments.lexers.templates', 'Smarty', ('smarty',), ('*.tpl',), ()),
    'SqlLexer': ('pygments.lexers.other', 'SQL', ('sql',), ('*.sql',), ('text/x-sql',)),
    'TexLexer': ('pygments.lexers.text', 'TeX', ('tex', 'latex'), ('*.toc', '*.tex', '*.aux'), ('text/x-tex', 'text/x-latex')),
    'TextLexer': ('pygments.lexers.special', 'Text only', ('text',), ('*.txt',), ('text/plain',)),
    'VbNetLexer': ('pygments.lexers.dotnet', 'VB.net', ('vb.net', 'vbnet'), ('*.bas', '*.vb'), ('text/x-vbnet', 'text/x-vba')),
    'XmlDjangoLexer': ('pygments.lexers.templates', 'XML+Django/Jinja', ('xml+django', 'xml+jinja'), (), ()),
    'XmlErbLexer': ('pygments.lexers.templates', 'XML+Ruby', ('xml+ruby', 'xml+erb'), (), ()),
    'XmlLexer': ('pygments.lexers.web', 'XML', ('xml',), ('*.xml',), ('text/xml', 'application/xml', 'image/svg+xml')),
    'XmlPhpLexer': ('pygments.lexers.templates', 'XML+PHP', ('xml+php',), (), ()),
    'XmlSmartyLexer': ('pygments.lexers.templates', 'XML+Smarty', ('xml+smarty',), (), ())
}

if __name__ == '__main__':
    import sys
    import os

    # lookup lexers
    found_lexers = []
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    for filename in os.listdir('.'):
        if filename.endswith('.py') and not filename.startswith('_'):
            module_name = 'pygments.lexers.%s' % filename[:-3]
            print module_name
            module = __import__(module_name, None, None, [''])
            for lexer_name in module.__all__:
                lexer = getattr(module, lexer_name)
                found_lexers.append(
                    '%r: %r' % (lexer_name,
                                (module_name,
                                 lexer.name,
                                 tuple(lexer.aliases),
                                 tuple(lexer.filenames),
                                 tuple(lexer.mimetypes))))
    # sort them, that should make the diff files for svn smaller
    found_lexers.sort()

    # extract useful sourcecode from this file
    f = file(__file__)
    try:
        content = f.read()
    finally:
        f.close()
    header = content[:content.find('LEXERS = {')]
    footer = content[content.find("if __name__ == '__main__':"):]

    # write new file
    f = file(__file__, 'w')
    f.write(header)
    f.write('LEXERS = {\n    %s\n}\n\n' % ',\n    '.join(found_lexers))
    f.write(footer)
    f.close()
