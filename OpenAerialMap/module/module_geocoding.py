# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and
 upload imagery from/to the OAM catalog.
                            -------------------
        begin               : 2015-07-01
        copyright           : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email               : tassia@acaia.ca / yoji.salut@gmail.com
        git sha             : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import os, sys
from geopy.geocoders import Nominatim

def nominatim_search(addressIn):

    geolocator = Nominatim()
    location = geolocator.geocode(addressIn)
    if location is not None:
        # print('boundingbox: {}'.format(location.raw['boundingbox']))
        bbox = location.raw['boundingbox']
        strBboxForOAM = '{},{},{},{}'.format(bbox[2], bbox[0], bbox[3], bbox[1])
        return strBboxForOAM
    else:
        return 'failed'
