# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LinkFlaechenToHaltung
                                 A QGIS plugin
 Verknüpft Flächen mit nächster Haltung
                             -------------------
        begin                : 2017-06-12
        copyright            : (C) 2017 by Jörg Höttges/FH Aachen
        email                : hoettges@fh-aachen.de
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
    """Load Application class from file application.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .application import Application
    return Application(iface)
