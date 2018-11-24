# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Galton
                                 A QGIS plugin
 Qgis оболочка для сервиса построения изохрон Galton
                             -------------------
        begin                : 2017-10-24
        copyright            : (C) 2017 by Konuchov Artem
        email                : konuchovartem@gmail.com
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
    """Load Galton class from file Galton.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .galton import Galton
    return Galton(iface)
