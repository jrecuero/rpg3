#!/usr/bin/env python

"""cell.py class required any cell.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     10/01/2014

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
import cocos

#
# import user python modules
#
import utilator
import loggerator


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
class Cell(object):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self, thePosition, **kwargs):
        """ Cell initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Sword name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        self.logger     = loggerator.getLoggerator(self.getClass())
        self.position   = thePosition
        self.data       = kwargs.get('theData', None)
        self.name       = kwargs.get('theName', None)
        self.sprite     = kwargs.get('theSprite', None)
        self.spriteName = kwargs.get('theSpriteName', None)
        self.selected   = False
        self.createSprite()

    #--------------------------------------------------------------------------
    def createSprite(self):
        """
        """
        if self.spriteName:
            x, y = self.position
            self.sprite = cocos.sprite.Sprite('images/%s.png' % (self.spriteName, ))
            self.sprite.position = self.sprite.width * (y + 1), self.sprite.height * (x + 1)
        return self.sprite

    #--------------------------------------------------------------------------
    def getPosition(self):
        """
        """
        return self.position

    #--------------------------------------------------------------------------
    def setPosition(self, thePosition):
        """
        """
        self.position = thePosition
        return True

    #--------------------------------------------------------------------------
    def getName(self):
        """
        """
        return self.name

    #--------------------------------------------------------------------------
    def setName(self, theName):
        """
        """
        self.name = theName
        return True

    #--------------------------------------------------------------------------
    def getData(self):
        """
        """
        return self.data

    #--------------------------------------------------------------------------
    def setData(self, theData):
        """
        """
        self.data = theData
        return True

    #--------------------------------------------------------------------------
    def getSprite(self):
        """
        """
        return self.sprite

    #--------------------------------------------------------------------------
    def setSprite(self, theSprite):
        """
        """
        self.sprite = theSprite
        return True

    #--------------------------------------------------------------------------
    def isSelected(self):
        """
        """
        return self.selected

    #--------------------------------------------------------------------------
    def _select(self):
        """
        """
        self.selected = not self.selected
        self.getSprite().opacity = 125 if self.selected else 255

    #--------------------------------------------------------------------------
    def select(self, x=None, y=None):
        """
        """
        if (x is None and y is None) or self.getSprite().contains(x, y):
            self._select()
            return True
        return False

    #--------------------------------------------------------------------------
    def swap(self, theOther):
        """
        """
        self.position, theOther.position = theOther.position, self.position,
        #self.sprite.image, theOther.sprite.image = theOther.sprite.image, self.sprite.image
        self.sprite.position, theOther.sprite.position = theOther.sprite.position, self.sprite.position

    #--------------------------------------------------------------------------
    def getClass(self):
        """ Return the cell class name

        :rtype: str
        :return: string with the class name
        """
        return utilator.getClass(self)


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
