#!/usr/bin/env python

"""panepos.py class required for the pane position.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     10/21/2014

"""

__docformat__ = 'restructuredtext en'

###############################################################################
##  _                            _
## (_)_ __ ___  _ __   ___  _ __| |_ ___
## | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
## | | | | | | | |_) | (_) | |  | |_\__ \
## |_|_| |_| |_| .__/ \___/|_|   \__|___/
##             |_|
###############################################################################
#
# import std python modules
#

#
# import panepos python modules
#


###############################################################################
##
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##
###############################################################################
#

###############################################################################
##            _                     _   _
##  ___ _   _| |__  _ __ ___  _   _| |_(_)_ __   ___  ___
## / __| | | | '_ \| '__/ _ \| | | | __| | '_ \ / _ \/ __|
## \__ \ |_| | |_) | | | (_) | |_| | |_| | | | |  __/\__ \
## |___/\__,_|_.__/|_|  \___/ \__,_|\__|_|_| |_|\___||___/
##
###############################################################################
#

###############################################################################
##       _                     _       __ _       _ _   _
##   ___| | __ _ ___ ___    __| | ___ / _(_)_ __ (_) |_(_) ___  _ __  ___
##  / __| |/ _` / __/ __|  / _` |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
## | (__| | (_| \__ \__ \ | (_| |  __/  _| | | | | | |_| | (_) | | | \__ \
##  \___|_|\__,_|___/___/  \__,_|\___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
##
###############################################################################
#

#
#------------------------------------------------------------------------------
class PanePosition(object):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self, thePane=None, thePoint=None):
        """ Initialize pane position instance

        :type thePane: object
        :param thePane: instance with the pane where point is referenced

        :type thePoint: Point
        :param thePoint: position point
        """
        self.pane  = thePane
        self.point = thePoint

    #--------------------------------------------------------------------------
    def set(self, thePane=None, thePoint=None):
        """ Set pane position instance

        :type thePane: object
        :param thePane: instance with the pane where point is referenced

        :type thePoint: point.Point
        :param thePoint: position point
        """
        self.pane  = thePane if thePane is not None else self.pane
        self.point = thePoint if thePoint is not None else self.point

    #--------------------------------------------------------------------------
    def get(self):
        """ Return pane position value.

        :rtype: dict
        :return: dictionary with pane and point values
        """
        return {'pane': self.pane, 'point': self.point}

    #--------------------------------------------------------------------------
    def getPane(self):
        """ Return the pane value.

        :rtype: object
        :return: object with the pane for the position
        """
        return self.pane

    #--------------------------------------------------------------------------
    def getPoint(self):
        """ Return the point value.

        :rtype: point.Point
        :return: Point with the point for the position
        """
        return self.point


###############################################################################
##                  _
##  _ __ ___   __ _(_)_ __
## | '_ ` _ \ / _` | | '_ \
## | | | | | | (_| | | | | |
## |_| |_| |_|\__,_|_|_| |_|
##
###############################################################################
#
if __name__ == '__main__':
    import doctest
    doctest.testmod()
