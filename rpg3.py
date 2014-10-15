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
import cell
import tableboard

from axe import Axe
from bow import Bow
from coin import Coin
from dagger import Dagger
from heart import Heart
from lance import Lance
from mana import Mana
from shield import Shield
from staff import Staff
from sword import Sword
from user import User
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
class Rpg3(cocos.layer.Layer):
    """
    """

    is_event_handler = True

    images = [Axe,
              Bow,
              Coin,
              Dagger,
              Heart,
              Lance,
              Mana,
              Shield,
              Staff,
              Sword, ]

    #--------------------------------------------------------------------------
    def __init__(self):
        """
        """
        super(Rpg3, self).__init__()

        self.size = 8
        while True:
            self.createBoardPhase = True
            self.tableSprites = []
            self.tableboard = self.createTableBoard(self.size)
            matches = self.tableboard.matchBoard()
            if not self.tableboard.isThereAnyMatch(matches):
                break
        self.createBoardPhase = False
        for aSprite in self.tableSprites:
            self.add(aSprite)
        self.logger = loggerator.getLoggerator('rpg3')
        self.statsDict = cell.Cell.createStatsDict()

        labelAttrs = {'font_name': 'Times New Roman',
                      'font_size': 16,
                      'anchor_x': 'left',
                      'anchor_y': 'top', }
        x, y = 32, 460
        for stat, value in self.statsDict.iteritems():
            label = cocos.text.Label('%s: %s' % (stat, value), **labelAttrs)
            label.position = x, y
            self.add(label, name=stat)
            x, y = x, y - 20
        self.createCommandLine()

        self.user = User('USERNAME')

        self.logger.debug('Is there any match: %s' % (self.tableboard.searchForAnyPossibleMatch(), ))

    #--------------------------------------------------------------------------
    def createCommandLine(self):
        """ Create command line widget
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

        :type thePosition: tuple
        :param thePosition: tuple with the new cell position

        :rtype: Cell
        :return: Cell instance created
        """
        cellKlass = random.sample(Rpg3.images, 1)[0]
        newCell = cellKlass(thePosition)
        if self.createBoardPhase:
            self.tableSprites.append(newCell.getSprite())
        else:
            self.add(newCell.getSprite())
        return newCell

    #--------------------------------------------------------------------------
    def createTableBoard(self, theSize):
        """ Create a new table board

        :type theSize: int
        :param theSize: table board size x size

        :rtype: TableBoard
        :return: TableBoard instance created
        """
        return tableboard.TableBoard(theSize, theNewCellCb=self.createCellCb)

    #--------------------------------------------------------------------------
    def cellSelected(self):
        """ Return a list with all cell selected

        :rtype: list
        :return: list with all cell selected
        """
        return [aCell for aCell in self.tableboard.iterCell() if aCell.isSelected()]

    #--------------------------------------------------------------------------
    def processCellSelected(self, x, y):
        """ Process cell selected at x, y

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
    def updateStats(self, theMatches):
        """ Update stats values with the given matches

        :type theMatches: list
        :param theMatches: list with all matches
        """
        statsDict = self.tableboard.matchResults(theMatches, self.user)
        for stat, value  in statsDict.iteritems():
            self.statsDict[stat] += value
            label = self.get(stat)
            label.element.text = '%s: %s' % (stat, self.statsDict[stat])
        #self.logger.info("stats: %s" % (self.statsDict))

    #--------------------------------------------------------------------------
    def updateTableboard(self):
        """ Update table board with all matches
        """
        self.tableboard.fallBoard()
        for aCell in self.tableboard.emptyCellsInBoard():
            self.tableboard.removeCell(aCell.getPosition())
            self.remove(aCell.getSprite())
            newCell = self.tableboard.addNewCell(aCell.getPosition())
            self.add(newCell.getSprite())
        self.processMatch()
        self.logger.debug('Is there any match: %s' % (self.tableboard.searchForAnyPossibleMatch(), ))
        statsUserData = self.user.stats.getStatsData()
        #for k, v in statsUserData.iteritems():
        #    self.logger.info('User stat[%s]: %s' % (k, v))
        self.user.addExp(100)

    #--------------------------------------------------------------------------
    def processMatch(self):
        """ Process all matches
        """
        matches = self.tableboard.matchBoard()
        if self.tableboard.isThereAnyMatch(matches):
            self.updateStats(matches)
            self.tableboard.setEmptyCells(matches)

            for aCell in self.tableboard.emptyCellsInBoard():
                sprite = cocos.sprite.Sprite('images/explosion.png')
                sprite.position = aCell.getSprite().position
                self.remove(aCell.getSprite())
                aCell.setSprite(sprite)
                self.add(aCell.getSprite())
            self.do(Delay(1) + CallFunc(self.updateTableboard))

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
        self.processMatch()


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
