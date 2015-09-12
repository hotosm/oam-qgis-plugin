# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenAerialMap
                                 A QGIS plugin
 This plugin can be used as an OAM client to browse, search, download and
 upload imagery from/to the OAM catalog.
                             -------------------
        begin                : 2015-07-01
        copyright            : (C) 2015 by Humanitarian OpenStreetMap Team (HOT)
        email                : tassia@acaia.ca / yoji.salut@gmail.com
        git sha              : $Format:%H$
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

import sys
import os

path_root = os.path.join(os.path.dirname(__file__))
sys.path.append(path_root)

# path to external libs
path_boto = os.path.join(os.path.dirname(__file__),'ext_libs/boto-2.38.0')
path_filechunkio = os.path.join(os.path.dirname(__file__),'ext_libs/filechunkio-1.6')
path_requests = os.path.join(os.path.dirname(__file__),'ext_libs/requests-2.7.0')
sys.path.append(path_boto)
sys.path.append(path_filechunkio)
sys.path.append(path_requests)

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OpenAerialMap class from file OpenAerialMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .oam_main import OpenAerialMap
    return OpenAerialMap(iface)
