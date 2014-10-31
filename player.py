#!/usr/bin/env python

"""player.py class required for the player characted.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     10/08/2014

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
# import player python modules
#
import loggerator
import utilator
import objecto
import stats
import attrs
#import point
#import dungeonpath


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
class Player(objecto.Objecto):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self, theName):
        """ Initialize Player instance

        >>> u = Player('my name')
        >>> u.name
        'my name'
        >>> u.stats # doctest: +ELLIPSIS
        <stats.Stats object at 0x...>

        :type theName: str
        :param theName: Player name
        """
        super(Player, self).__init__(theName)
        self.stats   = stats.Stats()
        self.attrs   = attrs.Attrs()
        self.logger  = loggerator.getLoggerator(utilator.getClass(self))
        self.dungeonpath = None

    #--------------------------------------------------------------------------
    def getDamage(self):
        """ Return player damage
        """
        return self.attrs.damage

    #--------------------------------------------------------------------------
    def getDefense(self):
        """ Return player defense
        """
        return self.attrs.defense

    #--------------------------------------------------------------------------
    def getMoney(self):
        """ Return player money
        """
        return self.attrs.money

    #--------------------------------------------------------------------------
    def getHealth(self):
        """ Return player health
        """
        return self.attrs.health

    #--------------------------------------------------------------------------
    def getPower(self):
        """ Return player power
        """
        return self.attrs.power

    #--------------------------------------------------------------------------
    def getMove(self):
        """ Set player move
        """
        return self.attrs.move

    #--------------------------------------------------------------------------
    def setDamage(self, theDamage):
        """ Set player damage

        :type theDamage: int
        :param theDamage: new damage value
        """
        self.attrs.damage = theDamage

    #--------------------------------------------------------------------------
    def setDefense(self, theDefense):
        """ Set player defense

        :type theDefense: int
        :param theDefense: new defense value
        """
        self.attrs.defense = theDefense

    #--------------------------------------------------------------------------
    def setMoney(self, theMoney):
        """ Set player money

        :type theMoney: int
        :param theMoney: new money value
        """
        self.attrs.money = theMoney

    #--------------------------------------------------------------------------
    def setHealth(self, theHealth):
        """ Set player health

        :type theHealth: int
        :param theHealth: new health value
        """
        self.attrs.health = theHealth

    #--------------------------------------------------------------------------
    def setPower(self, thePower):
        """ Set player power

        :type thePower: int
        :param thePower: new power value
        """
        self.attrs.power = thePower

    #--------------------------------------------------------------------------
    def setMove(self, theMove):
        """ Set player move

        :type theMove: int
        :param theMove: new move value
        """
        self.attrs.move = theMove

    #--------------------------------------------------------------------------
    def getStatValue(self, theKlass):
        """ Return value for the given stat

        >>> u = Player('my name')
        >>> u.stats.power = 99
        >>> u.stats.axe = 24
        >>> u.getStatValue('axe')
        24

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self.stats.getStatValue(theKlass)

    #--------------------------------------------------------------------------
    def addStatValue(self, theKlass, theValue=1):
        """ Add a value to the stat value field.

        :type theValue: int
        :param theValue: value to add to the counter

        :type theKlass: object
        :param theKlass: instance with the cell stat

        :rtype: int/bool
        :return: new stat count value, None if stat not found
        """
        return self.stats.addStatValue(theKlass, theValue)

    #--------------------------------------------------------------------------
    def addStatCount(self, theKlass, theValue=1):
        """ Add a value to the stat counter field.

        :type theKlass: object
        :param theKlass: instance with the cell stat

        :type theValue: int
        :param theValue: value to add to the counter
        """
        return self.stats.addStatCount(theKlass, theValue)

    #--------------------------------------------------------------------------
    def addStatRuns(self, theKlass, theValue=1):
        """ Add a value to the stat runs field.

        :type theValue: int
        :param theValue: value to add to the counter

        :type theKlass: object
        :param theKlass: instance with the cell stat

        :rtype: int/bool
        :return: new stat count value, None if stat not found
        """
        return self.stats.addStatRuns(theKlass, theValue)

    #--------------------------------------------------------------------------
    def addExp(self, theExp):
        """ Add some experience

        >>> u = Player('the name')
        >>> u.addExp(23)
        >>> u.stats.exp, u.stats.level
        (23, 0)
        >>> u.addExp(201)
        >>> u.stats.exp, u.stats.level
        (24, 2)

        :type theExp: int
        :param theExp: experience to be added
        """
        self.stats.addExp(theExp)


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
