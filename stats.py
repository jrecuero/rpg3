#!/usr/bin/env python

"""stats.py class required for stats used by the user.

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

EXP_NEXT_LEVEL = 100
"""
    :type: int

    Experience required to reach the next level.
"""


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
class Stats (object):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self):
        """ Initialize Stats instance

        >>> s = Stats()
        >>> s.level, s.exp
        (0, 0)
        >>> s.money, s.shield, s.health, s.power
        (0, 0, 0, 0)
        >>> s.axe, s.bow, s.dagger, s.lance, s.staff, s.sword
        (0, 0, 0, 0, 0, 0)

        """
        self.level  = 0
        self.exp    = 0
        self.money  = 0
        self.shield = 0
        self.health = 0
        self.power  = 0
        self.axe    = 0
        self.bow    = 0
        self.dagger = 0
        self.lance  = 0
        self.staff  = 0
        self.sword  = 0
        self.logger = loggerator.getLoggerator('stat')

    #--------------------------------------------------------------------------
    def addExp(self, theExp):
        """ Add some experience

        >>> s = Stats()
        >>> s.addExp(10)
        >>> s.exp, s.level
        (10, 0)
        >>> s.addExp(125)
        >>> s.exp, s.level
        (35, 1)

        :type theExp: int
        :param theExp: experience to be added
        """
        self.exp += theExp
        while self.exp >= EXP_NEXT_LEVEL:
            self.exp -= EXP_NEXT_LEVEL
            self.levelUp()

    #--------------------------------------------------------------------------
    def levelUp(self):
        """ Level up instance

        >>> s = Stats()
        >>> s.levelUp()
        >>> s.level
        1
        >>> s.money, s.shield, s.health, s.power
        (1, 1, 1, 1)
        >>> s.axe, s.bow, s.dagger, s.lance, s.staff, s.sword
        (1, 1, 1, 1, 1, 1)

        """
        self.level  += 1
        self.coin   += 1
        self.shield += 1
        self.heart  += 1
        self.mana   += 1
        self.axe    += 1
        self.bow    += 1
        self.dagger += 1
        self.lance  += 1
        self.staff  += 1
        self.sword  += 1

    #--------------------------------------------------------------------------
    def getStatValue(self, theStat, theKlass):
        """ Return value for the given stat

        >>> s = Stats()
        >>> s.money = 100
        >>> s.sword = 25
        >>> s.getStatValue('money', None)
        100
        >>> s.getStatValue('dummy', 'SWORD')
        25

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        self.logger.debug("getStatValue for %s, %s" % (theStat, theKlass))
        statValue = getattr(self, theStat, None)
        if statValue is None:
            statValue = getattr(self, theKlass.lower(), None)
        return statValue


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
