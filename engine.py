#!/usr/bin/env python

"""engine.py class required for the engine.

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
# import engine python modules
#
import objecto


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
class Phase(object):
    """
    """
    NONE         = 0
    MATCH        = 1
    USER_ACTION  = 2
    OTHER_ACTION = 3
    MOVEMENT     = 4

    #--------------------------------------------------------------------------
    @staticmethod
    def nextPhase(thePhase):
        """ Return the next phase to run

        :type thePhase: int
        :param thePhase: active phase

        :rtype: int
        :return: next active phase
        """
        if thePhase == Phase.NONE:
            return Phase.NONE
        elif thePhase == Phase.MATCH:
            return Phase.USER_ACTION
        elif thePhase == Phase.USER_ACTION:
            return Phase.OTHER_ACTION
        elif thePhase == Phase.OTHER_ACTION:
            return Phase.MOVEMENT
        elif thePhase == Phase.MOVEMENT:
            return Phase.MATCH
        else:
            return Phase.NONE


#
#------------------------------------------------------------------------------
class Engine(objecto.Objecto):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self, theTableboard, theDungeon, theName=None):
        """ Initialize Engine instance

        :type theTableboard: tableboard.TableBoard
        :param theTableboard: table board instance

        :type theDungeon: dungeon.Dungeon
        :param theDungeon: dungeon instance

        :type theName: str
        :param theName: Engine name
        """
        super(Engine, self).__init__(theName)
        self.tableboard  = theTableboard
        self.dungeon     = theDungeon
        self.activePhase = Phase.NONE

    #--------------------------------------------------------------------------
    def runMatchPhase(self):
        """ Run the User match phase
        """
        pass

    #--------------------------------------------------------------------------
    def runUserActionPhase(self):
        """ Run the User action phase
        """
        pass

    #--------------------------------------------------------------------------
    def runOtherActionPhase(self):
        """ Run Other action phase
        """
        pass

    #--------------------------------------------------------------------------
    def runMovementPhase(self):
        """ Run movement phase
        """
        pass


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
