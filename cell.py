#!/usr/bin/env python

"""cell.py class required tableboard cell.

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
import loggerator
import attrs


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

    customAttrsCbs = {}

    #--------------------------------------------------------------------------
    @staticmethod
    def getCellAttrs():
        """
        """
        return ('damage', 'defense', 'money', 'health', 'power')

    #--------------------------------------------------------------------------
    @staticmethod
    def createAttrsDict():
        """
        """
        dicta = {}
        for attr in Cell.getCellAttrs():
            dicta[attr] = 0
        return dicta

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
        self.logger   = loggerator.getLoggerator('cell')
        self.position = thePosition
        self.data     = kwargs['theData'] if 'theData' in kwargs else None
        self.name     = kwargs['theName'] if 'theName' in kwargs else None
        self.sprite   = kwargs['theSprite'] if 'theSprite' in kwargs else None
        self.selected = False
        self.attrsUsed = ()
        self.createSprite()
        self.createAttrs()
        self.attrs = attrs.Attrs()

    #--------------------------------------------------------------------------
    def createSprite(self):
        """
        """
        x, y = self.position
        self.sprite = cocos.sprite.Sprite('images/%s.png' % (self.STRING, ))
        self.sprite.position = self.sprite.width * (y + 1), self.sprite.height * (x + 1)
        return self.sprite

    #--------------------------------------------------------------------------
    def createAttrs(self):
        """
        """
        self.data    = getattr(self, 'STRING', 'CELL')
        self.DAMAGE  = getattr(self, 'DAMAGE', 0)
        self.DEFENSE = getattr(self, 'DEFENSE', 0)
        self.MONEY   = getattr(self, 'MONEY', 0)
        self.HEALTH  = getattr(self, 'HEALTH', 0)
        self.POWER   = getattr(self, 'POWER', 0)

        self.attrsCbs = {}
        for attr in attrs.getAttrs():
            self.attrsCbs[attr] = {3: self.baseMatch3, 4: self.baseMatch4, 5: self.baseMatch5}
        self.attrsCbs.update(self.customAttrsCbs)

    #--------------------------------------------------------------------------
    def _getTotalAttrValue(self, theAttr, theUser=None, theMatchNumber=0):
        """ Get total value to add for a Attr

        Calculate the total value based on the cell and the user value for
        that particular cell.

        It updates the counter for the cell type for the user.

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :type theMatchNumber: int
        :param theMatchNumber: number of cells being matched

        :rtype: list
        :return: Total value accumulate to the given sta
        """
        cellValue = getattr(self, theAttr, 0)
        userValue = 0
        if theUser:
            userValue = theUser.getAttrValue(theAttr, self.__class__.__name__)
        return cellValue + userValue

    #--------------------------------------------------------------------------
    def baseMatch3(self, theMatch, theAttr, theUser=None):
        """ Basic match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value = self._getTotalStatValue(theStat, theUser, len(theMatch))
        self.logger.debug('Match %d %s, %s %s each, total %s' %
                          (len(theMatch), self.__class__.__name__.lower(), value, theStat, value * len(theMatch)))
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def baseMatch4(self, theMatch, theAttr, theUser=None):
        """ Critical match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value = self._getTotalStatValue(theStat, theUser, len(theMatch)) * 2
        self.logger.debug('Match %d %s, %s %s each, total %s' %
                          (len(theMatch), self.__class__.__name__.lower(), value, theStat, value * len(theMatch)))
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def baseMatch5(self, theMatch, theAttr, theUser=None):
        """ Critical match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value = self._getTotalStatValue(theStat, theUser, len(theMatch)) * 3
        self.logger.debug('Match %d %s, %s %s each, total %s' %
                          (len(theMatch), self.__class__.__name__.lower(), value, theStat, value * len(theMatch)))
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def executeMatch(self, theMatch, theUser=None):
        """ Execute the given match for the given cell.
        :type theMatch: list
        :param theMatch: List with position matching

        :type theUser: User
        :param theUser: user instance

        :rtype: dict
        :return: dictionary with cell attributes being updated
        """
        reto_dict = {}
        for attr in self.attrsUsed:
            reto_dict[attr] = self._matchCb(theMatch, attr, theUser)

    #--------------------------------------------------------------------------
    def _matchCb(self, theMatch, theAttr, theUser=None):
        """
        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the attr name

        :type theUser: User
        :param theUser: user instance
        """
        matchCb = self.attrsCbs[theAttr].get(len(theMatch), None)
        #self.logger.info('Match %d %s for %s,  cb: %s' % (len(theMatch), self.__class__.__name__, theAttr, matchCb))
        if matchCb:
            return matchCb(theMatch, theAttr, theUser)
        return 0

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
    def getDamage(self):
        """
        """
        return self.damage

    #--------------------------------------------------------------------------
    def setDamage(self, theDamage):
        """
        """
        self.damage = theDamage
        return True

    #--------------------------------------------------------------------------
    def getDefense(self):
        """
        """
        return self.defense

    #--------------------------------------------------------------------------
    def setDefense(self, theDefense):
        """
        """
        self.defense = theDefense
        return True

    #--------------------------------------------------------------------------
    def getMoney(self):
        """
        """
        return self.money

    #--------------------------------------------------------------------------
    def setMoney(self, theMoney):
        """
        """
        self.money = theMoney
        return True

    #--------------------------------------------------------------------------
    def getHealth(self):
        """
        """
        return self.health

    #--------------------------------------------------------------------------
    def setHealth(self, theHealth):
        """
        """
        self.health = theHealth
        return True

    #--------------------------------------------------------------------------
    def getPower(self):
        """
        """
        return self.power

    #--------------------------------------------------------------------------
    def setPower(self, thePower):
        """
        """
        self.power = thePower
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
        return self.__class__.__name__.lower()


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
#    import unittest
#    import test.test_cell as testCell
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(testCell.CellTestSuite())
    import doctest
    doctest.testmod()
