"""
/***************************************************************************
 OpenAerialMap QGIS plugin
 Module for search dialog
 ***************************************************************************/
"""

import pycurl
import json
from StringIO import StringIO

class OAMCatalogAccess:

    def __init__(self, hostUrl, action, dicQueries, parent=None):
        self.hostUrl = hostUrl
        self.action = action
        self.dicQueries = dicQueries

    def test(self):
        print str(self.dicQueries)
        endPoint = self.hostUrl + '/' + self.action
        strBuffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, endPoint)
        c.setopt(c.WRITEDATA, strBuffer)
        c.perform()
        c.close()
        metadata = strBuffer.getvalue()
        dicMetadada = json.loads(metadata)
        listResults = dicMetadada[u'results']
        return listResults
