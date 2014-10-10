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
import stats


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
class Player(object):
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
        self.name   = theName
        self.stats  = stats.Stats()
        self.logger = loggerator.getLoggerator(self.__class__.__name__.lower())

    #--------------------------------------------------------------------------
    def getStatValue(self, theStat, theKlass):
        """ Return value for the given stat

        >>> u = Player('my name')
        >>> u.stats.power = 99
        >>> u.stats.axe = 24
        >>> u.getStatValue('power', None)
        99
        >>> u.getStatValue('dummy', 'AXE')
        24

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self.stats.getStatValue(theStat, theKlass)

    #--------------------------------------------------------------------------
    def addStatCount(self, theValue, theStat, theKlass):
        """ Add a value to the stat counter field.

        :type theValue: int
        :param theValue: value to add to the counter

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self.stats.addStatCount(theValue, theStat, theKlass)

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
