from htmlentitydefs import entitydefs
import re

def convertWebIntelligentPlainTextToHtml(orig, tab_width=4):
    """Converts text/x-web-intelligent to text/html
    """
    urlRegexp = re.compile(r'((?:ftp|https?)://(?:[a-z0-9](?:[-a-z0-9]*[a-z0-9])?\.)+(?:com|edu|biz|org|gov|int|info|mil|net|name|museum|coop|aero|[a-z][a-z])\b(?:\d+)?(?:\/[^;"\'<>()\[\]{}\s\x7f-\xff]*(?:[.,?]+[^;"\'<>()\[\]{}\s\x7f-\xff]+)*)?)', re.I|re.S|re.U)
    emailRegexp = re.compile(r'["=]?(\b[A-Z0-9._%-]+@[A-Z0-9._%-]+\.[A-Z]{2,4}\b)', re.I|re.S|re.U)
    indentRegexp = re.compile(r'^(\s+)', re.M|re.U)
    
    text = orig
    if not isinstance(text, unicode):
        text = unicode(text, 'utf-8', 'replace')
    
    # Do &amp; separately, else, it may replace an already-inserted & from
    # an entity with &amp;, so < becomes &lt; becomes &amp;lt;
    text = text.replace('&', '&amp;')
    # Make funny characters into html entity defs
    for entity, letter in entitydefs.items():
        if entity != 'amp':
            text = text.replace(letter.decode('latin-1'), '&' + entity + ';')
        
    # Replace hyperlinks with clickable <a> tags
    def replaceURL(match):
        url = match.groups()[0]
        return '<a href="%s">%s</a>' % (url, url)
    text = urlRegexp.subn(replaceURL, text)[0]
    
    # Replace email strings with mailto: links
    def replaceEmail(match):
        url = match.groups()[0]
        return '<a href="mailto:%s">%s</a>' % (url, url)
    text = emailRegexp.subn(replaceEmail, text)[0]

    # Make leading whitespace on a line into &nbsp; to preserve indents
    def indentWhitespace(match):
        indent = match.groups()[0]
        indent = indent.replace(' ', '&nbsp;')
        return indent.replace('\t', '&nbsp;' * tab_width)
    text = indentRegexp.subn(indentWhitespace, text)[0]
    
    # Finally, make \n's into br's
    text = text.replace('\n', '<br />')

    text = text.encode('utf-8')
    
    return text
            
def convertHtmlToWebIntelligentPlainText(orig):
    """Converts text/html to text/x-web-intelligent.
    """
    preRegex = re.compile(r'<\s*pre[^>]*>(.*?)<\s*/pre\s*>', re.I | re.S)
    
    tagWhitespaceRegex = re.compile(r'\s+((<[^>]+>)\s+)+')
    whitespaceRegex = re.compile(r'\s+')
    
    tdRegex = re.compile(r'<\s*(td)([^>])*>', re.I)
    breakRegex = re.compile(r'<\s*(br)\s*/?>', re.I)
    startBlockRegex = re.compile(r'<\s*(dt)[^>]*>', re.I)
    endBlockRegex = re.compile(r'<\s*/\s*(p|div|tr|ul|ol|dl)[^>]*>', re.I)
    indentBlockRegex = re.compile(r'<\s*(blockquote|dd)[^>]*>', re.I)
    listBlockRegex = re.compile(r'<\s*(li)[^>]*>', re.I)

    tagRegex = re.compile(r'<[^>]+>', re.I | re.M)

    # Save all <pre> sections and restore after other transforms
    preSections = {}
    def savePres(match):
        marker = '__pre_marker__%d__' % (len(preSections),)
        preSections[marker] = match.group(1)
        return marker
    text = preRegex.sub(savePres, orig)

    # Make whitespace-tag-whitespace into whitespace-tag. Repeat this 
    # in case there are directly nested tags
    def fixTagWhitespace(match):
        # Remove any superfluous whitespace, but preserve one leading space
        return ' ' + whitespaceRegex.sub('', match.group(0))
    text = tagWhitespaceRegex.sub(fixTagWhitespace, text)

    # Make all whitespace into a single space
    text = whitespaceRegex.sub(' ', text)

    # Fix entities
    text = text.replace('&nbsp;', ' ')
    for entity, letter in entitydefs.items():
        # Do &lt; and &gt; later, else we may be creating what looks like 
        # tags
        if entity != 'lt' and entity != 'gt':
            text = text.replace('&' + entity + ';', letter)

    # XXX: Remove <head>, <script>, <style> ?

    # Make tabs out of td's
    text = tdRegex.sub('\t', text)

    # Make br's and li's into newlines
    text = breakRegex.sub('\n', text)

    # Make the start of list blocks into paragraphs
    text = startBlockRegex.sub('\n\n', text)

    # Make the close of p's, div's and tr's into paragraphs
    text = endBlockRegex.sub('\n\n', text)

    # Make blockquotes and dd blocks indented
    text = indentBlockRegex.sub('\n\n  ', text)

    # Make list items indented and prefixed with -
    text = listBlockRegex.sub('\n\n  - ', text)

    # Remove other tags
    text = tagRegex.sub('', text)

    # Fix < and > entities
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')

    # Restore pres
    for marker, section in preSections.items():
        text = text.replace(marker, '\n\n' + section + '\n\n')
    
    return text