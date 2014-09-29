import cocos
from cocos.actions import Delay, CallFunc
import pyglet
import random

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


#
#------------------------------------------------------------------------------
class Rpg3(cocos.layer.Layer):

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

    #--------------------------------------------------------------------------
    def createCommandLine(self):
        self.cmd = cocos.text.Label('Command Line', position=(400, 460), width=200, height=200, multiline=True)
        self.add(self.cmd, name='CommandLine')
        self.cmd.line = 0

    #--------------------------------------------------------------------------
    def newEntryInCommandLine(self, theNewLine):
        self.cmd.element.text = '%s\n%s' % (self.cmd.element.text, 'match found')

    #--------------------------------------------------------------------------
    def createCellCb(self, thePosition):
        """
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
        """
        """
        return tableboard.TableBoard(theSize, theNewCellCb=self.createCellCb)

    #--------------------------------------------------------------------------
    def cellSelected(self):
        """
        """
        return [aCell for aCell in self.tableboard.iterCell() if aCell.isSelected()]

    #--------------------------------------------------------------------------
    def processCellSelected(self, x, y):
        for aCell in self.tableboard.iterCell():
            aCell.select(x, y)
        cells = self.cellSelected()
        if len(cells) == 2:
            if self.tableboard.cellTogetherCell(*cells):
                self.tableboard.swapCells(*cells)
            [aCell.select() for aCell in cells]

    #--------------------------------------------------------------------------
    def updateStats(self, theMatches):
        statsDict = self.tableboard.matchResults(theMatches)
        for stat, value in statsDict.iteritems():
            self.statsDict[stat] += value
            label = self.get(stat)
            label.element.text = '%s: %d' % (stat, self.statsDict[stat], )
        self.logger.debug("stats: %s" % (self.statsDict))

    #--------------------------------------------------------------------------
    def updateTableboard(self):
        self.tableboard.fallBoard()
        for aCell in self.tableboard.emptyCellsInBoard():
            self.tableboard.removeCell(aCell.getPosition())
            self.remove(aCell.getSprite())
            newCell = self.tableboard.addNewCell(aCell.getPosition())
            self.add(newCell.getSprite())
        self.processMatch()

    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    def processMatch(self):
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

            #self.tableboard.fallBoard()
            #self.updateTableboard()
            #matches = self.tableboard.matchBoard()

    #--------------------------------------------------------------------------
    def on_mouse_press(self, x, y, buttons, modifiers):
        """
        """
        self.processCellSelected(x, y)
        self.processMatch()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init(width=800)
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
