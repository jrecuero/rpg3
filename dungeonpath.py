#!/usr/bin/env python

"""dungeonpath.py class required for the dungeonpath.

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
# import dungeonpath python modules
#
import objecto
import dungeonstep
#import player


###############################################################################
##
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##
###############################################################################
#
FORWARD    = 'forward'
BACKWARD   = 'backward'
STOP       = 'stop'
RIGHT_TURN = 'right turn'
LEFT_TURN  = 'left turn'
UPSIDE     = 'upside'
DOWNSIDE   = 'downside'


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
class DungeonPath(objecto.Objecto):
    """
    Dungeon path is composed of dungeon steps.

    Position in the dungeon path uses x coordination for the dungeon step and
    the y coordinate for the dungeon cell in the given dungeon step.
    """

    #--------------------------------------------------------------------------
    def __init__(self, theName=None):
        """ Initialize DungeonPath instance

        :type theName: str
        :param theName: DungeonPath name
        """
        super(DungeonPath, self).__init__(theName)
        self.path    = self.baseLinearPath()
        self.players = []

    #--------------------------------------------------------------------------
    def baseLinearPath(self, theLen=100, theWide=3):
        """ Create a basic linear path.

        :type theLen: int
        :param theLen: length of the path

        :type theWide: int
        :param theWide: wide for every path step

        :rtype: list
        :return: list the newly created path
        """
        path = []
        for x in xrange(theLen):
            path.append(dungeonstep.DungeonStep(theWide))
        return path

    #--------------------------------------------------------------------------
    def addPlayer(self, thePlayer, thePathPos=None):
        """ Add a player to the path.

        :type thePlayer: player.Player
        :param thePlayer: player instance to be added to the path

        :type thePathPos: point
        :param thePathPos: position in the path

        :rtype: bool
        :return: True if player was added to the path, else False
        """
        if thePlayer not in self.players:
            thePlayer.dungeonpath = {'path': self,
                                     'pathpos': thePathPos,
                                     'pathmove': 1,
                                     'pathdir': FORWARD}
            self.players.append(thePlayer)
            return True
        else:
            self.logger.error('Player %s was already in the path' % (thePlayer.name, ))
            return False

    #--------------------------------------------------------------------------
    def removePlayer(self, thePlayer):
        """ Remove a player from the path.

        :type thePlayer: player.Player
        :param thePlayer: player instance to be removed from the path

        :rtype: bool
        :return: True if player was removed from the path, else False
        """
        reto = True
        try:
            thePlayer.dungeonpath = None
            self.players.remove(thePlayer)
        except ValueError:
            self.logger.error('Player %s was not in the path' % (thePlayer.name, ))
            reto = False
        finally:
            return reto

    #--------------------------------------------------------------------------
    def placePlayer(self, thePlayer, thePathPos):
        """ Set the player in a given position

        :type thePlayer: player.Player
        :param thePlayer: player instance to be added to the path

        :type thePathPos: point
        :param thePathPos: position in the path

        :rtype: bool
        :return: True if player was added to the path, else False
        """
        if thePlayer in self.players:
            thePlayer.dungeonpath['pathpos'] = thePathPos
            return True
        else:
            self.logger.error('Player %s was not in the path' % (thePlayer.name, ))
            return False

    #--------------------------------------------------------------------------
    def movePlayer(self, thePlayer):
        """ Move a player in the path

        :type thePlayer: player.Player
        :param thePlayer: player to move
        """
        posX, posY = thePlayer.dungeonpath['pathpos']
        if thePlayer.dungeonpath['pathdir'] == FORWARD:
            posX += thePlayer.dungeonpath['pathmove']
        elif thePlayer.dungeonpath['pathdir'] == BACKWARD:
            posX -= thePlayer.dungeonpath['pathmove']
        elif thePlayer.dungeonpath['pathdir'] == STOP:
            pass
        thePlayer.dungeonpath['pathpos'] == (posX, posY)
        # Now reset to default player movement data.
        thePlayer.dungeonpath['pathmove'] = 1
        thePlayer.dungeonpath['pathdir']  = FORWARD

    #--------------------------------------------------------------------------
    def movePath(self):
        """ Move all players in the dungeon path.
        """
        map(self.movePlayer, self.players)


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
