# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OpenImageryNetwork
                                 A QGIS plugin
 This plugin connects to the Open Imagery Network (OIN) to browse, search and upload imagery to/from OIN nodes
                             -------------------
        begin                : 2015-06-23
        copyright            : (C) 2015 by Humanitarian OpenstreetMap Team (HOT)
        email                : tassia@acaia.ca
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load OpenImageryNetwork class from file OpenImageryNetwork.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .oin_client import OpenImageryNetwork
    return OpenImageryNetwork(iface)
