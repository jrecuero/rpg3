import cocos
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

        self.size = 5
        self.tableboard = self.createTableBoard(self.size)
        self.logger = loggerator.getLoggerator('rpg3')
        self.statsDict = cell.Cell.createStatsDict()

        labelAttrs = {'font_name': 'Times New Roman',
                      'font_size': 16,
                      'anchor_x': 'left',
                      'anchor_y': 'top', }
        x, y = 5, 460
        for stat, value in self.statsDict.iteritems():
            label = cocos.text.Label('%s: %s' % (stat, value), **labelAttrs)
            label.position = x, y
            self.add(label, name=stat)
            x, y = x, y - 20

    #--------------------------------------------------------------------------
    def createCellCb(self, thePosition):
        """
        """
        cellKlass = random.sample(Rpg3.images, 1)[0]
        newCell = cellKlass(thePosition)
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
    def on_mouse_press(self, x, y, buttons, modifiers):
        """
        """
        for aCell in self.tableboard.iterCell():
            aCell.select(x, y)
        cells = self.cellSelected()
        if len(cells) == 2:
            self.tableboard.swapCells(*cells)
            [aCell.select() for aCell in cells]
        self.logger.debug("#------------------------------------------------#")
        matches = self.tableboard.defaultMatches()
        while self.tableboard.isThereAnyMatch(matches):
            matches = self.tableboard.matchBoard()
            statsDict = self.tableboard.matchResults(matches)
            for stat, value in statsDict.iteritems():
                self.statsDict[stat] += value
                label = self.get(stat)
                label.element.text = '%s: %d' % (stat, self.statsDict[stat], )
            self.logger.debug("stats: %s" % (self.statsDict))
            #self.tableboard.logBoard()
            self.tableboard.setEmptyCells(matches)
            #for aCell in self.tableboard.emptyCellsInBoard():
            #    self.logger.debug('empty cells: %s' % (aCell.getPosition(), ))
            self.tableboard.fallBoard()
            for aCell in self.tableboard.emptyCellsInBoard():
            #    self.logger.debug('empty cells: %s' % (aCell.getPosition(), ))
                self.tableboard.removeCell(aCell.getPosition())
                self.remove(aCell.getSprite())
                newCell = self.tableboard.addNewCell(aCell.getPosition())
                self.add(newCell.getSprite())
            #self.tableboard.logBoard()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
