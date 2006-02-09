"""
parser.http package (imdb package).

This package provides the IMDbHTTPAccessSystem class used to access
IMDb's data through the web interface.
the imdb.IMDb function will return an instance of this class when
called with the 'accessSystem' argument set to "http" or "web"
or "html" (this is the default).

Copyright 2004-2006 Davide Alberani <da@erlug.linux.it>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

from urllib import FancyURLopener, quote_plus
from codecs import lookup

from imdb import IMDbBase
from imdb._exceptions import IMDbDataAccessError, IMDbParserError
from movieParser import movie_parser, plot_parser, movie_awards_parser, \
                        taglines_parser, keywords_parser, \
                        alternateversions_parser, crazycredits_parser, \
                        goofs_parser, trivia_parser, quotes_parser, \
                        releasedates_parser, ratings_parser, \
                        officialsites_parser, connections_parser, \
                        tech_parser, locations_parser, soundtrack_parser, \
                        dvd_parser, rec_parser, externalrev_parser, \
                        newsgrouprev_parser, misclinks_parser, \
                        soundclips_parser, videoclips_parser, news_parser, \
                        photosites_parser, amazonrev_parser, guests_parser, \
                        business_parser, sales_parser
from searchMovieParser import search_movie_parser
from personParser import maindetails_parser, bio_parser, \
                        otherworks_parser, person_awards_parser, \
                        person_officialsites_parser, publicity_parser, \
                        agent_parser
from searchPersonParser import search_person_parser
from utils import ParserBase


# Misc URLs
imdbURL_movie = 'http://akas.imdb.com/title/tt%s/'
imdbURL_person = 'http://akas.imdb.com/name/nm%s/'
imdbURL_search = 'http://akas.imdb.com/find?%s'

# The cookies for the "adult" search.
# Please don't mess with this account.
_cookie_id = 'boM2bYxz9MCsOnH9gZ0S9QHs12NWrNdApxsls1Vb5/NGrNdjcHx3dUas10UASoAjVEvhAbGagERgOpNkAPvxdbfKwaV2ikEj9SzXY1WPxABmDKQwdqzwRbM+12NSeJFGUEx3F8as10WwidLzVshDtxaPIbP13NdjVS9UZTYqgTVGrNcT9vyXU1'
_cookie_uu = '3M3AXsquTU5Gur/Svik+ewflPm5Rk2ieY3BIPlLjyK3C0Dp9F8UoPgbTyKiGtZp4x1X+uAUGKD7BM2g+dVd8eqEzDErCoYvdcvGLvVLAen1y08hNQtALjVKAe+1hM8g9QbNonlG1/t4S82ieUsBbrSIQbq1yhV6tZ6ArvSbA7rgHc8n5AdReyAmDaJ5Wm/ee3VDoCnGj/LlBs2ieUZNorhHDKK5Q=='


class IMDbURLopener(FancyURLopener):
    """Fetch web pages and handle errors."""
    def __init__(self, *args, **kwargs):
        FancyURLopener.__init__(self, *args, **kwargs)
        # XXX: IMDb's web server doesn't like urllib-based programs,
        #      so lets fake to be Mozilla.
        #      Wow!  I'm shocked by my total lack of ethic! <g>
        self.addheaders = [('User-agent', 'Mozilla/5.0')]

    def http_error_default(self, url, fp, errcode, errmsg, headers):
        raise IMDbDataAccessError, {'url': 'http:%s' % url,
                                    'errcode': errcode,
                                    'errmsg': errmsg,
                                    'headers': headers,
                                    'proxy': self.proxies.get('http', '')}
    def open_unknown(self, fullurl, data=None):
        raise IMDbDataAccessError, {'fullurl': fullurl,
                                    'data': str(data),
                                    'proxy': self.proxies.get('http', '')}
    def open_unknown_proxy(self, proxy, fullurl, data=None):
        raise IMDbDataAccessError, {'proxy': str(proxy),
                                    'fullurl': fullurl,
                                    'data': str(data)}


class IMDbHTTPAccessSystem(IMDbBase):
    """The class used to access IMDb's data through the web."""

    accessSystem = 'http'

    urlOpener = IMDbURLopener()

    def __init__(self, isThin=0, adultSearch=1, proxy=-1,
                *arguments, **keywords):
        """Initialize the access system."""
        IMDbBase.__init__(self, *arguments, **keywords)
        # When isThin is set, we're parsing the "maindetails" page
        # of a movie (instead of the "combined" page) and movie/person
        # references are not collected if no defaultModFunct is provided.
        self.isThin = isThin
        if isThin:
            self.accessSystem = 'httpThin'
            movie_parser.mdparse = 1
            if self._defModFunct is None:
                ParserBase.getRefs = 0
                from imdb.utils import modNull
                self._defModFunct = modNull
        else:
            movie_parser.mdparse = 0
            ParserBase.getRefs = 1
        self.do_adult_search(adultSearch)
        if proxy != -1: self.set_proxy(proxy)

    def _normalize_movieID(self, movieID):
        """Normalize the given movieID."""
        try:
            return '%07d' % int(movieID)
        except ValueError, e:
            raise IMDbParserError, 'invalid movieID "%s": %s' % (movieID, e)

    def _normalize_personID(self, personID):
        """Normalize the given personID."""
        try:
            return '%07d' % int(personID)
        except ValueError, e:
            raise IMDbParserError, 'invalid personID "%s": %s' % (personID, e)

    def get_imdbMovieID(self, movieID):
        """Translate a movieID in an imdbID; in this implementation
        the movieID _is_ the imdbID.
        """
        return movieID

    def get_imdbPersonID(self, personID):
        """Translate a personID in an imdbID; in this implementation
        the personID _is_ the imdbID.
        """
        return personID

    def set_proxy(self, proxy):
        """Set the web proxy to use.
        
        It should be a string like 'http://localhost:8080/'; if the
        string is empty, no proxy will be used.
        If set, the value of the environment variable HTTP_PROXY is
        automatically used.
        """
        if not proxy:
            if self.urlOpener.proxies.has_key('http'):
                del self.urlOpener.proxies['http']
        else:
            if not proxy.lower().startswith('http://'):
                proxy = 'http://%s' % proxy
            self.urlOpener.proxies['http'] = proxy

    def get_proxy(self):
        """Return the used proxy or an empty string."""
        return self.urlOpener.proxies.get('http', '')

    def do_adult_search(self, doAdult,
                        cookie_id=_cookie_id, cookie_uu=_cookie_uu):
        """If doAdult is true, 'adult' movies are included in the
        search results; cookie_id and cookie_uu are optional
        parameters to select a specific account (see your cookie
        or cookies.txt file."""
        for index in xrange(len(self.urlOpener.addheaders)):
            if self.urlOpener.addheaders[index][0] == 'Cookie':
                del self.urlOpener.addheaders[index]
                break
        if doAdult:
            c_header = 'id=%s; uu=%s' % (cookie_id, cookie_uu)
            self.urlOpener.addheaders += [('Cookie', c_header)]

    def _retrieve(self, url):
        """Retrieve the given URL."""
        encode = 'latin_1'
        try:
            uopener = self.urlOpener.open(url)
            content = uopener.read()
            server_encode = uopener.info().getparam('charset')
            # look at the content-type HTML meta tag.
            if server_encode is None and content:
                first_bytes = content[:512]
                begin_h = first_bytes.find('text/html; charset=')
                if begin_h != -1:
                    end_h = first_bytes[19+begin_h:].find('"')
                    if end_h != -1:
                        server_encode = first_bytes[19+begin_h:19+begin_h+end_h]
            if server_encode:
                try:
                    if lookup(server_encode):
                        encode = server_encode
                except (LookupError, ValueError, TypeError):
                    pass
            uopener.close()
            self.urlOpener.close()
        except IOError, e:
            raise IMDbDataAccessError, {'errcode': e.errno,
                                        'errmsg': str(e.strerror),
                                        'url': url,
                                        'proxy': self.get_proxy()}
        return unicode(content, encode, 'replace')

    def _search_movie(self, title, results):
        # The URL of the query.
        # XXX: To retrieve the complete results list:
        #      params = urllib.urlencode({'more': 'tt', 'q': title})
        ##params = urllib.urlencode({'tt': 'on','mx': str(results),'q': title})
        params = 'q=%s&tt=on&mx=%s' % (quote_plus(title), str(results))
        cont = self._retrieve(imdbURL_search % params)
        return search_movie_parser.parse(cont, results=results)['data']

    def get_movie_main(self, movieID):
        if not self.isThin:
            cont = self._retrieve(imdbURL_movie % movieID + 'combined')
        else:
            cont = self._retrieve(imdbURL_movie % movieID + 'maindetails')
        return movie_parser.parse(cont)

    def get_movie_plot(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'plotsummary')
        return plot_parser.parse(cont)

    def get_movie_awards(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'awards')
        return movie_awards_parser.parse(cont)

    def get_movie_taglines(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'taglines')
        return taglines_parser.parse(cont)

    def get_movie_keywords(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'keywords')
        return taglines_parser.parse(cont)

    def get_movie_alternate_versions(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'alternateversions')
        return alternateversions_parser.parse(cont)

    def get_movie_crazy_credits(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'crazycredits')
        return crazycredits_parser.parse(cont)

    def get_movie_goofs(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'goofs')
        return goofs_parser.parse(cont)

    def get_movie_quotes(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'quotes')
        return quotes_parser.parse(cont)

    def get_movie_release_dates(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'releaseinfo')
        return releasedates_parser.parse(cont)

    def get_movie_vote_details(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'ratings')
        return ratings_parser.parse(cont)

    def get_movie_official_sites(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'officialsites')
        return officialsites_parser.parse(cont)

    def get_movie_trivia(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'trivia')
        return trivia_parser.parse(cont)

    def get_movie_connections(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'movieconnections')
        return connections_parser.parse(cont)

    def get_movie_technical(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'technical')
        return tech_parser.parse(cont)

    def get_movie_business(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'business')
        return business_parser.parse(cont)

    def get_movie_literature(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'literature')
        return tech_parser.parse(cont)

    def get_movie_locations(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'locations')
        return locations_parser.parse(cont)

    def get_movie_soundtrack(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'soundtrack')
        return soundtrack_parser.parse(cont)

    def get_movie_dvd(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'dvd')
        return dvd_parser.parse(cont)

    def get_movie_recommendations(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'recommendations')
        return rec_parser.parse(cont)

    def get_movie_external_reviews(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'externalreviews')
        return externalrev_parser.parse(cont)

    def get_movie_newsgroup_reviews(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'newsgroupreviews')
        return newsgrouprev_parser.parse(cont)

    def get_movie_misc_sites(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'miscsites')
        return misclinks_parser.parse(cont)

    def get_movie_sound_clips(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'soundsites')
        return soundclips_parser.parse(cont)

    def get_movie_video_clips(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'videosites')
        return videoclips_parser.parse(cont)

    def get_movie_photo_sites(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'photosites')
        return photosites_parser.parse(cont)

    def get_movie_news(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'news')
        return news_parser.parse(cont)

    def get_movie_amazon_reviews(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'amazon')
        return amazonrev_parser.parse(cont)

    def get_movie_guests(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'epcast')
        return guests_parser.parse(cont)

    def get_movie_merchandising_links(self, movieID):
        cont = self._retrieve(imdbURL_movie % movieID + 'sales')
        return sales_parser.parse(cont)

    def _search_person(self, name, results):
        # The URL of the query.
        # XXX: To retrieve the complete results list:
        #      params = urllib.urlencode({'more': 'nm', 'q': name})
        ##params = urllib.urlencode({'nm': 'on', 'mx': str(results), 'q': name})
        params = 'q=%s&nm=on&mx=%s' % (quote_plus(name), str(results))
        cont = self._retrieve(imdbURL_search % params)
        return search_person_parser.parse(cont, results=results)['data']

    def get_person_main(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'maindetails')
        ret = maindetails_parser.parse(cont)
        ret['info sets'] = ('main', 'filmography')
        return ret

    def get_person_filmography(self, personID):
        return self.get_person_main(personID)

    def get_person_biography(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'bio')
        return bio_parser.parse(cont)

    def get_person_awards(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'awards')
        return person_awards_parser.parse(cont)

    def get_person_other_works(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'otherworks')
        return otherworks_parser.parse(cont)

    def get_person_agent(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'agent')
        return agent_parser.parse(cont)

    def get_person_publicity(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'publicity')
        return publicity_parser.parse(cont)

    def get_person_official_sites(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'officialsites')
        return person_officialsites_parser.parse(cont)

    def get_person_news(self, personID):
        cont = self._retrieve(imdbURL_person % personID + 'news')
        return news_parser.parse(cont)


