"""
$Id: interface.py 4143 2006-02-17 13:25:22Z sidnei $
"""
from zope.interface import Interface, Attribute

class IApplicationRoot(Interface):
    """Application Root
    """

class ILocalRoles(Interface):
    """ Object with Local Roles.
    """

class IMetadata(Interface):
    """Metadata
    """

    # XXX Add more attributes here, or create a interface per
    # portal_type.
    path = Attribute('Path')
    id = Attribute('id')
    title = Attribute('Title')
    description = Attribute('Description')
    body = Attribute('Body')
    portal_type = Attribute('Portal Type')
    creators = Attribute('Creators')
    effective_date = Attribute('Effective Date')
    expiration_date = Attribute('Expiration Date')
    start_date = Attribute('Start Date')
    end_date = Attribute('End Date')
    right_column = Attribute('Right Column')
    allowDiscussion = Attribute('Allow Discussion')
    remoteUrl = Attribute('remote URL')
    url = Attribute('URL')
    created = Attribute('Creation Date')
    rights = Attribute('Copyright Owner')

    # XXX This should go into ICase
    library_title = Attribute('Library Title')
    citation = Attribute('Citation')
    abstract = Attribute('Abstract')
    indexcodes = Attribute('Category Id')
    previously_reported = Attribute('Previous REport')
    status = Attribute('Publication Status')
    zip_coverage = Attribute('Zip Coverage')
    #keynumber = Attribute('Another UID')
    attorney_name = Attribute('Attorney Name')
    attorney_email = Attribute('Attorney Email')
    attorney_phone = Attribute('Attorney Phone')
    jurisdication = Attribute('Jurisdiction')
    docketno = Attribute('Docket Number')
    docketdate = Attribute('Docket Date')


class IDirectory(IMetadata):
    """Directory
    """

    def getChildren():
        """ Returns objects representing children """

class IContent(IMetadata):
    """Content
    """
    path = Attribute('Path')

