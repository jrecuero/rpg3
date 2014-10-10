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

#------------------------------------------------------------------------------
def addStats(theOneStat, theOtherStat):
    """ Add two stats values (as a pair)

    :type theOneStat: list
    :param theOneStat: first stat to add

    :type theOtherStat: list
    :param theOtherStat: second stat to add

    :rtype: list
    :param: list with both stats added
    """
    value = theOneStat[0] + theOtherStat[0]
    count = theOneStat[1] + theOtherStat[1]
    return (value, count)

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
        >>> s.coin.value
        {'count': 0, 'value': 0}
        >>> s.axe
        {'count': 0, 'value': 0}

        """
        self.level  = 0
        self.exp    = 0
        self.coin   = self._initStat()
        self.shield = self._initStat()
        self.heart  = self._initStat()
        self.mana   = self._initStat()
        self.axe    = self._initStat()
        self.bow    = self._initStat()
        self.dagger = self._initStat()
        self.lance  = self._initStat()
        self.staff  = self._initStat()
        self.sword  = self._initStat()
        self.logger = loggerator.getLoggerator('stat')

    #--------------------------------------------------------------------------
    def _initStat(self):
        """ Initialize value for a stat attribute.

        :rtype: dict
        :return: dict with initial values
        """
        return {'count': 0, 'value': 0, }

    #--------------------------------------------------------------------------
    def _incStatValue(self, theStat, theIncVal=1):
        """ Increase value field for a stat.

        :type theStat: dict
        :param theStat: dictinary with the stat to update

        :type theIncVal: int
        :param theIncVal: magnitude to increase the value
        """
        theStat['value'] += theIncVal
        return theStat['value']

    #--------------------------------------------------------------------------
    def _incStatCount(self, theStat, theIncCount=1):
        """ Increase counter field for a stat.

        :type theStat: dict
        :param theStat: dictinary with the stat to update

        :type theIncCount: int
        :param theIncCount: magnitude to increase the counter
        """
        theStat['count'] += theIncCount
        return theStat['count']

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
        >>> s.coin, s.shield, s.heart, s.mana
        (1, 1, 1, 1)
        >>> s.axe, s.bow, s.dagger, s.lance, s.staff, s.sword
        (1, 1, 1, 1, 1, 1)

        """
        self.level += 1
        self._incStatValue(self.coin)
        self._incStatValue(self.shield)
        self._incStatValue(self.heart)
        self._incStatValue(self.mana)
        self._incStatValue(self.axe)
        self._incStatValue(self.bow)
        self._incStatValue(self.dagger)
        self._incStatValue(self.lance)
        self._incStatValue(self.staff)
        self._incStatValue(self.sword)

    #--------------------------------------------------------------------------
    def getStat(self, theStat, theKlass):
        """ Return the given stat instance.

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        stat = getattr(self, theStat, None) if theStat else None
        return stat if stat else getattr(self, theKlass.lower(), None)

    #--------------------------------------------------------------------------
    def getStatValue(self, theStat, theKlass):
        """ Return value for the given stat

        >>> s = Stats()
        >>> s.coin = 100
        >>> s.sword = 25
        >>> s.getStatValue('coin', None)
        100
        >>> s.getStatValue('dummy', 'SWORD')
        25

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        #self.logger.debug("getStatValue for %s, %s" % (theStat, theKlass))
        stat = self.getStat(theStat, theKlass)
        return stat['value'] if stat else None

    #--------------------------------------------------------------------------
    def addStatCount(self, theValue, theKlass):
        """ Add a value to the stat counter field.

        :type theValue: int
        :param theValue: value to add to the counter

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        stat = self.getStat(None, theKlass)
        return self._incStatCount(stat, theValue) if stat else 0

    #--------------------------------------------------------------------------
    def getStatsData(self):
        """ Return dictionary with stats

        :rtype: dict
        :return: dictionary with stats
        """
        return {'coin': self.coin,
                'shield': self.shield,
                'heart': self.heart,
                'mana': self.mana,
                'axe': self.axe,
                'bow': self.bow,
                'dagger': self.dagger,
                'lance': self.lance,
                'staff': self.staff,
                'sword': self.sword, }


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
