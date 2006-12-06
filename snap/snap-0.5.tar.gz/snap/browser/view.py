"""
$Id: view.py 4046 2006-02-09 03:06:14Z sidnei $
"""

import mimetypes
from datetime import datetime, timedelta
from snap.utils import get_metadata
from zope.app.rdb.interfaces import IZopeDatabaseAdapter
from zope.app import zapi
from zope.app.rdb import queryForResults
from zope.app.publisher.browser import BrowserView
from zope.app.traversing.interfaces import TraversalError, ITraverser

class DBMixin(BrowserView):

    def _getDBConnection(self):
        dba = zapi.getUtility(IZopeDatabaseAdapter, 'entransitda',
            context = self.context)
        return dba()

class BatchSupport(BrowserView):

    _batch = 10
    _sort_on = 'modified'

    def getBatch(self):
        return self._batch

    def getStart(self):
        return self.request.get('start', 0) + 1

    def getEnd(self):
        return self.request.get('start', 0) + self.getBatch()

    def getPrevStart(self):
        request = self.request
        start = request.get('start', None)
        if not start:
            return 0
        return start - self.getBatch()

    def getNextStart(self):
        request = self.request
        start = request.get('start', None)
        if not start:
            start = 0
        return start + self.getBatch()

    def showPrevious(self):
        request = self.request
        start = request.get('start', None) or 0
        return bool(start) > 0

    def showNext(self):
        request = self.request
        start = request.get('start', None) or 0
        batch = self.getBatch()
        return (start + batch) <= self.lenResults()

    def lenResults(self):
        raise NotImplementedError

    def getPages(self):
        request = self.request
        start = request.get('start', None) or 0
        len_results = self.lenResults()
        batch = self.getBatch()
        num_pages = float(len_results) / batch
        page_count = int(num_pages)
        if num_pages - page_count != 0:
            page_count = page_count + 1
        pages = list()
        for i in range(page_count):
            _start = i * batch
            query_string = 'start:int=%s' % _start
            pages.append(dict(number=i+1, query_string=query_string
                , selected=_start==start))
        return pages

class SortableSQLBatch(DBMixin, BatchSupport):

    def getSortOrder(self, field):
        request = self.request
        sort_on = request.get('sort_on', None)
        sort_order = request.get('sort_order', None)
        if sort_on == field and sort_order == 'asc':
            return 'desc'
        return 'asc'

    def getSortOn(self):
        return self.request.get('sort_on', self._sort_on)

    def _getResults(self):
        request = self.request
        start = request.get('start', None) or 0
        sort_on = request.get('sort_on', self._sort_on)
        sort_order = request.get('sort_order', 'desc')
        batch = self.getBatch()
        conn = self._getDBConnection()
        order_by = 'ORDER BY %s %s LIMIT %s OFFSET %s' % (sort_on, sort_order,
            batch, start)
        query = 'SELECT * %s %s;' % (self._getQuery(), order_by)
        return queryForResults(conn, query)

    def lenResults(self):
        conn = self._getDBConnection()
        query = 'SELECT count(*) AS count %s;' % self._getQuery()
        return queryForResults(conn, query)[0].count

    def getPages(self):
        request = self.request
        sort_on = request.get('sort_on', self._sort_on)
        sort_order = request.get('sort_order', 'desc')
        start = request.get('start', None) or 0
        len_results = self.lenResults()
        batch = self.getBatch()
        num_pages = float(len_results) / batch
        page_count = int(num_pages)
        if num_pages - page_count != 0:
            page_count = page_count + 1
        pages = list()
        for i in range(page_count):
            _start = i * batch
            query_string = 'start:int=%s&sort_on=%s&sort_order=%s' % (
                _start, sort_on, sort_order)
            pages.append(dict(number=i+1, query_string=query_string
                , selected=_start==start))
        return pages

    def _getQuery(self):
        raise NotImplementedError, 'You need to implement this'

class MetadataView(object):
    """View for Metadata
    """

class ContentView(BrowserView):

    def __call__(self):
        ct, enc = mimetypes.guess_type(self.context.path)
        if ct is not None:
            self.request.response.setHeader('content-type', ct)
        content = open(self.context.path, 'rb')
        return content.read()
