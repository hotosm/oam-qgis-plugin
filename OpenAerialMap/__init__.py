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

#add path to models subfolder
path_root = os.path.join(os.path.dirname(__file__))
path_module = os.path.join(os.path.dirname(__file__), 'module')
path_gui = os.path.join(os.path.dirname(__file__), 'gui')
sys.path.append(path_root)
sys.path.append(path_module)
sys.path.append(path_gui)

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OpenAerialMap class from file OpenAerialMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .oam_main import OpenAerialMap
    return OpenAerialMap(iface)
