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

    customStatCbs = {}

    #--------------------------------------------------------------------------
    @staticmethod
    def getStats():
        """
        """
        return ('damage', 'defense', 'money', 'health', 'power')

    #--------------------------------------------------------------------------
    @staticmethod
    def createStatsDict():
        """
        """
        dicta = {}
        for stat in Cell.getStats():
            dicta[stat] = 0
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
        self.createSprite()
        self.createStats()

    #--------------------------------------------------------------------------
    def createSprite(self):
        """
        """
        x, y = self.position
        self.sprite = cocos.sprite.Sprite('images/%s.png' % (self.STRING, ))
        self.sprite.position = self.sprite.width * (y + 1), self.sprite.height * (x + 1)
        return self.sprite

    #--------------------------------------------------------------------------
    def createStats(self):
        """
        """
        self.data    = getattr(self, 'STRING', 'CELL')
        self.DAMAGE  = getattr(self, 'DAMAGE', 0)
        self.DEFENSE = getattr(self, 'DEFENSE', 0)
        self.MONEY   = getattr(self, 'MONEY', 0)
        self.HEALTH  = getattr(self, 'HEALTH', 0)
        self.POWER   = getattr(self, 'POWER', 0)
        self.statCbs = {'DAMAGE':  {'M3': self._m3Stat, 'M4': self._m4Stat, 'M5': self._m5Stat},
                        'DEFENSE': {'M3': self._m3Stat, 'M4': self._m4Stat, 'M5': self._m5Stat},
                        'MONEY':   {'M3': self._m3Stat, 'M4': self._m4Stat, 'M5': self._m5Stat},
                        'HEALTH':  {'M3': self._m3Stat, 'M4': self._m4Stat, 'M5': self._m5Stat},
                        'POWER':   {'M3': self._m3Stat, 'M4': self._m4Stat, 'M5': self._m5Stat}, }
        self.statCbs.update(self.customStatCbs)

    #--------------------------------------------------------------------------
    def _getTotalStatValue(self, theStat, theUser=None):
        """ Get total value to add for a stat

        :type theStat: str
        :param theStat: String with the stat name

        :type theUser: User
        :param theUser: user instance

        :rtype: int
        :return: Total value accumulate to the given stat
        """
        cellValue = getattr(self, theStat, 0)
        userValue = theUser.getStatValue(theStat, self.__class__.__name__) if theUser else 0
        return cellValue + userValue

    #--------------------------------------------------------------------------
    def _m3Stat(self, theMatch, theStat, theUser=None):
        """ Basic match accumulation method for any stat

        :type theMatch: list
        :param theMatch: List with position matching

        :type theStat: str
        :param theStat: String with the stat name

        :type theUser: User
        :param theUser: user instance

        :rtype: int
        :return: Total value accumulate to the given stat
        """
        value = self._getTotalStatValue(theStat, theUser)
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def _m4Stat(self, theMatch, theStat, theUser=None):
        """ Critical match accumulation method for any stat

        :type theMatch: list
        :param theMatch: List with position matching

        :type theStat: str
        :param theStat: String with the stat name

        :type theUser: User
        :param theUser: user instance

        :rtype: int
        :return: Total value accumulate to the given stat
        """
        value = self._getTotalStatValue(theStat, theUser) * 2
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def _m5Stat(self, theMatch, theStat, theUser=None):
        """ Critical match accumulation method for any stat

        :type theMatch: list
        :param theMatch: List with position matching

        :type theStat: str
        :param theStat: String with the stat name

        :type theUser: User
        :param theUser: user instance

        :rtype: int
        :return: Total value accumulate to the given stat
        """
        value = self._getTotalStatValue(theStat, theUser) * 3
        return value * len(theMatch)

    #--------------------------------------------------------------------------
    def _matchCb(self, theMatch, theStat, theUser=None):
        """
        :type theMatch: list
        :param theMatch: List with position matching

        :type theStat: str
        :param theStat: String with the stat name

        :type theUser: User
        :param theUser: user instance
        """
        matchCb = self.statCbs[theStat].get('M%d' % (len(theMatch), ), None)
        self.logger.info('Match %d %s for %s,  cb: %s' % (len(theMatch), self.__class__.__name__, theStat, matchCb))
        if matchCb:
            return matchCb(theMatch, theStat, theUser)
        return 0

    #--------------------------------------------------------------------------
    def damage(self, theMatch, theUser=None):
        """

        :type theUser: User
        :param theUser: user instance
        """
        return self._matchCb(theMatch, 'DAMAGE', theUser)

    #--------------------------------------------------------------------------
    def defense(self, theMatch, theUser=None):
        """

        :type theUser: User
        :param theUser: user instance
        """
        return self._matchCb(theMatch, 'DEFENSE', theUser)

    #--------------------------------------------------------------------------
    def money(self, theMatch, theUser=None):
        """

        :type theUser: User
        :param theUser: user instance
        """
        return self._matchCb(theMatch, 'MONEY', theUser)

    #--------------------------------------------------------------------------
    def health(self, theMatch, theUser=None):
        """

        :type theUser: User
        :param theUser: user instance
        """
        return self._matchCb(theMatch, 'HEALTH', theUser)

    #--------------------------------------------------------------------------
    def power(self, theMatch, theUser=None):
        """

        :type theUser: User
        :param theUser: user instance
        """
        return self._matchCb(theMatch, 'POWER', theUser)

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
