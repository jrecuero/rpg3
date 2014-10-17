#!/usr/bin/env python

"""stats.py class required for stats used by the user.

Information contained in this module is related with cells that can be placed
on the board. Every cells is a stat value that the used should be account for.

New cells, it means new stats can be added along the design of the game.

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
import yaml

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
    runs  = theOneStat[1] + theOtherStat[1]
    return (value, count, runs)


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
        statsStream = open('stats.yaml', 'r')
        self.stdict = yaml.load(statsStream)
        for key, val in self.stdict.iteritems():
            self.stdict[key] = self._initStat(val)
        self.logger = loggerator.getLoggerator('stat')

    #--------------------------------------------------------------------------
    def _initStat(self, theInitValue):
        """ Initialize value for a stat attribute.

        :type theInitValue: int
        :param theInitValue: initial value for a stat

        :rtype: dict
        :return: dict with initial values
        """
        return {'count': 0, 'value': theInitValue, 'runs': 0}

    #--------------------------------------------------------------------------
    def _incStatField(self, theStat, theField, theIncVal=1):
        """ Increase a field for a stat.

        :type theStat: dict
        :param theStat: dictinary with the stat to update

        :type theField: str
        :param theField: name of the field

        :type theIncVal: int
        :param theIncVal: magnitude to increase the value
        """
        theStat[theField] += theIncVal
        return theStat[theField]

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

        """
        self.level += 1
        for key in self.stdict.keys():
            self.addStatValue(key)

    #--------------------------------------------------------------------------
    def getStatsData(self):
        """ Return dictionary with stats

        :rtype: dict
        :return: dictionary with stats
        """
        return self.stdict

    #--------------------------------------------------------------------------
    def _getStatField(self, theKlass, theField):
        """ Return the given stat instance.

        :type theKlass: str
        :param theKlass: name of the stat

        :type theField: str
        :param theField: name of the field to retrieve information

        :rtype: int
        :return: field content
        """
        stat = self.stdict.get(theKlass, None)
        return stat[theField] if stat else None

    #--------------------------------------------------------------------------
    def getStatValue(self, theKlass):
        """ Return value for the given stat

        >>> s = Stats()
        >>> s.coin = 100

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self._getStatField(theKlass, 'value')

    #--------------------------------------------------------------------------
    def getStatCount(self, theKlass):
        """ Return count for the given stat

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self._getStatField(theKlass, 'count')

    #--------------------------------------------------------------------------
    def getStatRuns(self, theKlass):
        """ Return runs for the given stat

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self._getStatField(theKlass, 'runs')

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
        stat = self.stdict.get(theKlass, None)
        return self._incStatField(stat, 'value', theValue) if stat else None

    #--------------------------------------------------------------------------
    def addStatCount(self, theKlass, theValue=1):
        """ Add a value to the stat counter field.

        :type theValue: int
        :param theValue: value to add to the counter

        :type theKlass: object
        :param theKlass: instance with the cell stat

        :rtype: int/bool
        :return: new stat count value, None if stat not found
        """
        stat = self.stdict.get(theKlass, None)
        return self._incStatField(stat, 'count', theValue) if stat else None

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
        stat = self.stdict.get(theKlass, None)
        return self._incStatField(stat, 'runs', theValue) if stat else None


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
