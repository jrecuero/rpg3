#!/usr/bin/env python

"""rog3.py class for the game

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
from cocos.actions import Delay, CallFunc
import pyglet
import random

#
# import user python modules
#
import loggerator
import tablecell
import tableboard
import engine

from pieces.axe import Axe
from pieces.bow import Bow
from pieces.coin import Coin
from pieces.dagger import Dagger
from pieces.heart import Heart
from pieces.lance import Lance
from pieces.mana import Mana
from pieces.shield import Shield
from pieces.step import Step
from pieces.staff import Staff
from pieces.sword import Sword
from players.user import User
#import stats


# These assert are to avoid PEP8 complains.
assert Axe
assert Bow
assert Coin
assert Dagger
assert Heart
assert Lance
assert Mana
assert Shield
assert Step
assert Staff
assert Sword


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
class Rpg3(cocos.layer.Layer):
    """
    """

    is_event_handler = True

    #--------------------------------------------------------------------------
    def __init__(self):
        """ Initializes Rpg3 instance.

        Creates a valid table board and all required widgets and resources for
        the game.
        """
        super(Rpg3, self).__init__()

        self.size = 8
        self.user = User('USERNAME')
        self.createTableBoard(self.size)
        self.logger = loggerator.getLoggerator('rpg3')
        self.statsDict = tablecell.TableCell.createAttrsDict()

        labelAttrs = {'font_name': 'Times New Roman',
                      'font_size': 12,
                      'anchor_x': 'left',
                      'anchor_y': 'top', }
        x, y = 32, 460
        self.createCommandLine()

        for stat, value in self.user.stats.getStatsData().iteritems():
            label = cocos.text.Label('%s: %s' % (stat, value['count']), **labelAttrs)
            label.position = x, y
            self.add(label, name=stat)
            x, y = x, y - 16

        self.engine = engine.Engine(self.tableboard, None, self, self.user)

    #--------------------------------------------------------------------------
    def createCommandLine(self):
        """ Create command line widget

        Command line widget is used to provide some information to the user
        playing the game.
        """
        self.cmd = cocos.text.Label('Command Line', position=(400, 460), width=200, height=200, multiline=True)
        self.add(self.cmd, name='CommandLine')
        self.cmd.line = 0

    #--------------------------------------------------------------------------
    def newEntryInCommandLine(self, theNewLine):
        """ Add a new line to the command line

        :type theNewLine: str
        :param theNewLine: line to be added to the command line
        """
        self.cmd.element.text = '%s\n%s' % (self.cmd.element.text, theNewLine)

    #--------------------------------------------------------------------------
    def createCellCb(self, thePosition):
        """ Callback called when new cell is created

        This callback method is passed to the tableboard instance, so when a
        new cell has to be created in the tableboard, this will be called.

        :type thePosition: tuple
        :param thePosition: tuple with the new cell position

        :rtype: Cell
        :return: Cell instance created
        """
        cellStr   = random.sample(self.user.stats.getStatsData().keys(), 1)[0]
        cellKlass = eval(cellStr.capitalize())
        newCell   = cellKlass(thePosition)
        self.addSprite(newCell.getSprite())
        return newCell

    #--------------------------------------------------------------------------
    def cleanSpritesFromBoard(self):
        """ Remove all sprites from the tableboard.
        """
        for aSprite in [x for x in self.tableSprites]:
            self.removeSprite(aSprite)

    #--------------------------------------------------------------------------
    def createTableBoard(self, theSize):
        """ Create a new table board

        It creates a valid tableboard, where there is not any match placed, but
        there is at least one possible match to be done in the next movement.

        :type theSize: int
        :param theSize: table board size x size

        :rtype: TableBoard
        :return: TableBoard instance created
        """
        while True:
            self.createBoardPhase = True
            self.tableSprites = []
            self.tableboard = tableboard.TableBoard(theSize, theNewCellCb=self.createCellCb)
            matches = self.tableboard.matchBoard()
            # When there is not any match in the board, but there are possible
            # match, stop and start the game.
            if not self.tableboard.isThereAnyMatch(matches) and self.tableboard.searchForAnyPossibleMatch():
                break
        self.createBoardPhase = False
        for aSprite in self.tableSprites:
            self.add(aSprite)

    #--------------------------------------------------------------------------
    def cellSelected(self):
        """ Return a list with all cell selected by the user.

        :rtype: list
        :return: list with all cell selected
        """
        return [aCell for aCell in self.tableboard.iterCell() if aCell.isSelected()]

    #--------------------------------------------------------------------------
    def processCellSelected(self, x, y):
        """ Process cell selected at x, y

        Select a cell, when the selected cell is the second one, it proceeds to
        swap cells if the are placed together vertically or horizontally.

        When the second cell is selected, no matter what at the end no cell is
        set to selected in the tableboard.

        :type x: int
        :param x: cell x position

        :type y: int
        :param y: cell y position
        """
        for aCell in self.tableboard.iterCell():
            aCell.select(x, y)
        cells = self.cellSelected()
        if len(cells) == 2:
            if self.tableboard.cellTogetherCell(*cells):
                self.tableboard.swapCells(*cells)
            [aCell.select() for aCell in cells]

    #--------------------------------------------------------------------------
    def addSprite(self, theSprite):
        """ Add sprite to the scene and any other resource.

        :type theSprite: Sprite
        :param theSprite: sprite to add
        """
        self.tableSprites.append(theSprite)
        if not self.createBoardPhase:
            self.add(theSprite)

    #--------------------------------------------------------------------------
    def removeSprite(self, theSprite):
        """ Remove sprite from the scene and any other resource.

        :type theSprite: Sprite
        :param theSprite: sprite to remove
        """
        self.remove(theSprite)
        self.tableSprites.remove(theSprite)

    #--------------------------------------------------------------------------
    def replaceSriteForExplosionAtCell(self, theCell):
        """ Replace sprite for explosion sprite at the given cell.

        :type theCell: tablecell.TableCell
        :param theCell: table cell where sprite will be replaced
        """
        sprite = cocos.sprite.Sprite('images/explosion.png')
        sprite.position = theCell.getSprite().position
        self.removeSprite(theCell.getSprite())
        theCell.setSprite(sprite)
        self.addSprite(theCell.getSprite())

    #--------------------------------------------------------------------------
    def resetTableboard(self):
        """ Reset tableboard with a new one.

        Clean all sprites from the tableboard and create a new valid one.
        """
        self.cleanSpritesFromBoard()
        self.createTableBoard(self.size)
        self.newEntryInCommandLine('Reseted Tableboard')

    #--------------------------------------------------------------------------
    def updateStats(self):
        """ Update user stats values with given matches using dungeon engine.

        Call tableboard instance to process all matches in the board, then it
        process those results and update all required widgets.
        """
        userStats = self.user.stats.getStatsData()
        for stat, value in userStats.iteritems():
            label = self.get(stat)
            label.element.text = '%s: %s' % (stat, value['count'])

    #--------------------------------------------------------------------------
    def replaceSpriteForExplosion(self):
        """ Replace all empty cell sprites for explosion sprites.
        """
        for aCell in self.tableboard.emptyCellsInBoard():
            self.replaceSriteForExplosionAtCell(aCell)

    #--------------------------------------------------------------------------
    def processMatch(self):
        """ Process match using dungeon engine.
        """
        matches = self.engine.runMatchPhase()
        if matches is not None:
            self.updateStats()
            self.replaceSpriteForExplosion()
            self.scheduleEventAt(0.5, self.updateTableboard)
            return True
        else:
            if not self.tableboard.searchForAnyPossibleMatch():
                self.scheduleEventAt(0.5, self.resetTableboard)
            return False

    #--------------------------------------------------------------------------
    def updateTableboard(self):
        """ Update table board using dungeon engine.
        """
        self.engine.runUpdateTableboard()
        for aCell in self.tableboard.emptyCellsInBoard():
            self.tableboard.removeCell(aCell.getPosition())
            self.removeSprite(aCell.getSprite())
            self.tableboard.addNewCell(aCell.getPosition())

        self.scheduleEventAt(0, self.processMatch)

    #--------------------------------------------------------------------------
    def scheduleEventAt(self, theDelay, theAction):
        """ Schedule for running theAction at the given theDelay time.

        :type theDelay: float
        :param theDelay: delay the action should run

        :type theAction: func
        :param theAction: method to run
        """
        self.do(Delay(theDelay) + CallFunc(theAction))

    #--------------------------------------------------------------------------
    def on_mouse_press(self, x, y, buttons, modifiers):
        """ Handle when mouse button is being pressed

        :type x: int
        :param x: mouse x position

        :type y: int
        :param y: mouse y position

        :type buttons: int
        :param buttons: button being pressed

        :type modifiers: int
        :param modifiers: modifiers
        """
        self.processCellSelected(x, y)
        self.scheduleEventAt(0, self.processMatch)


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
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init(width=800)
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
