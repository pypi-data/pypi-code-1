##################################################################
#
# (C) Copyright 2006 ObjectRealms, LLC
# All Rights Reserved
#
# This file is part of Alchemist.
#
# Alchemist is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Alchemist is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CMFDeployment; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##################################################################

from zope.interface import Interface, Attribute
from zope.interface.common.mapping import IEnumerableMapping
from zope.app.container.interfaces import IContainer
from zope import schema

class TransmutationException( Exception ):
    """
    schema translation exception
    """

class IAlchemistTransmutation( Interface ):

    def transmute( schema, **kw ):
        """
        translates the schema and returns the translation.

        kw are specific to the translation
        """

class IEngineVocabularyUtility( Interface ):

    engines = schema.Iterable( title = u"RDB Engines",
                               description = u"Available RDB Engines")

class IDomainVocabularyUtility( Interface ):

    domain_classes = schema.Iterable( title=u"Domain Classes",
                                      description = u"Registered Domain Classes")

class IAlchemistContainer( IContainer ):
    """
    a domain record container
    """

    title = schema.TextLine(
        title = u"Title",
        description =u"The title of the object",
        default = u"",
        required = False
        )

    domain_class = schema.Choice(
        title = u"Domain Class",
        description = u"The Python Path of the Domain Class",
        required = True,
        vocabulary = "Alchemist Domain Classes"
        )
    
    domain_model = Attribute("domain_model", "The domain class")

    def query( **kw ):
        """
        return the specified children of the container
        """
                             
class ITableSchema( Interface ):
    """
    base interface for autogenerated schemas/interfaces derived
    from sqlalchemy table definitions
    """
    

class ISchemaIntrospector( IEnumerableMapping ):
    """ a read dictionary interfaces to tables """

    def bind( metadata=None, engine=None ):
        """
        binds introspector to a particular bound metadata, if metadata is none, create a new
        metadata and bind to the passed in engine
        """

    def bindEngine( engine, schema_name=None):
        """
        bind the engine to the introspector, creates an internal bound metadata to the engine.
        """
        
    def bindMetadata( metadata ):
        """
        bind the introspector to the bound metadata, the metadata utilized will be the parent
        for any introspected tables returned.
        """
    metadata = Attribute("metadata", "Bound Metadata")

    information_schema = Attribute("information_schema",
                                   "the bound metadata containing table definitions for ansi information schema"
                                   )

class IIModelInterface( Interface ):
    """
    marker interface on generated table schema interfaces, ie. a marker for interfaces
    """

class IModelAnnotation( Interface ):
    """
    """
    def getDisplayColumns():
        """
        return the columns that should be displayed
        """

class IModelIO( Interface ):
    """
    """

class IAlchemySchemaModel( Interface ):

    def match( object ):
        """
        should this model be used for the given object
        """

    def clear( ):
        """
        clear all loaded state for the model
        """

    def __getitem__( key ):
        """
        return the peer factor for the given key or None
        """

    def loadType( archetype_klass, context ):
        """
        load the schema from the given archetype klass,
        translate it to an alchemy model, and alchemy
        mapped peer class, uses context as an acquisition
        context if nesc.
        """

    def loadInstance( instance ):
        """
        as above but load from an instance...

        does not support context based schemas.. need to
        qualify the name on storage.
        """
        
