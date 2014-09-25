import cocos
import pyglet
import random

import loggerator
import cell
import tableboard


#
#------------------------------------------------------------------------------
class Rpg3(cocos.layer.Layer):

    is_event_handler = True

    images = ['blue', 'green', 'yellow', 'red', 'black', 'cyan', 'purple', 'orange']

    #--------------------------------------------------------------------------
    def __init__(self):
        """
        """
        super(Rpg3, self).__init__()
        label = cocos.text.Label('RPG Match 3',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)

        self.size = 4
        self.spriteSize = 64
        self.tableboard = self.createTableBoard(self.size)
        self.logger = loggerator.getLoggerator('rpg3')

    #--------------------------------------------------------------------------
    def createPiece(self, x, y):
        """
        """
        color = random.sample(Rpg3.images, 1)[0]
        piece = cocos.sprite.Sprite('images/%s.png' % color)
        piece.position = self.spriteSize * (y + 1), self.spriteSize * (x + 1)
        self.add(piece)
        return (color, piece)

    #--------------------------------------------------------------------------
    def createCell(self, x, y):
        """
        """
        color, piece = self.createPiece(x, y)
        return cell.Cell((x, y), theData=color, theSprite=piece)

    #--------------------------------------------------------------------------
    def createCellCb(self, thePosition):
        """
        """
        x, y = thePosition
        color, piece = self.createPiece(x, y)
        return {'theData': color, 'theSprite': piece}

    #--------------------------------------------------------------------------
    def createTableBoard(self, theSize):
        """
        """
        #matrix = [[self.createCell(x, y) for y in xrange(theSize)] for x in xrange(theSize)]
        #return tableboard.TableBoard(theSize, matrix)
        return tableboard.TableBoard(theSize, theNewCellCb=self.createCellCb)

    #--------------------------------------------------------------------------
    def cellSelected(self):
        """
        """
        #selected = []
        #for x in xrange(self.size):
        #    for y in xrange(self.size):
        #        aCell = self.tableboard.getCell((x, y))
        #        if aCell.isSelected():
        #            selected.append(aCell)
        return [aCell for aCell in self.tableboard.iterCell() if aCell.isSelected()]

    #--------------------------------------------------------------------------
    def on_mouse_press(self, x, y, buttons, modifiers):
        """
        """
        #for xPos in xrange(self.size):
        #    for yPos in xrange(self.size):
        #        self.tableboard.getCell((xPos, yPos)).select(x, y)
        for aCell in self.tableboard.iterCell():
            aCell.select(x, y)
        cells = self.cellSelected()
        if len(cells) == 2:
            self.tableboard.swapCells(*cells)
            [aCell.select() for aCell in cells]
        matches = self.tableboard.matchBoard()
        self.logger.debug("#------------------------------------------------#")
        self.tableboard.logBoard()
        #rowMatches, colMatches = matches
        #for match in rowMatches:
        #    for pos in match:
        #        self.tableboard.setCellData(pos, None)
        #for match in colMatches:
        #    for pos in match:
        #        self.tableboard.setCellData(pos, None)
        self.tableboard.setEmptyCells(matches)
        for aCell in self.tableboard.emptyCellsInBoard():
            self.logger.debug('empty cells: %s' % (aCell.getPosition(), ))
        self.tableboard.fallBoard()
        for aCell in self.tableboard.emptyCellsInBoard():
            self.logger.debug('empty cells: %s' % (aCell.getPosition(), ))
            self.tableboard.removeCell(aCell.getPosition())
            self.remove(aCell.getSprite())
            newCell = self.tableboard.addNewCell(aCell.getPosition())
            self.add(newCell.getSprite())
        self.tableboard.logBoard()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
