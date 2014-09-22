import cocos
import pyglet
import random

import cell
import tableboard


class Rpg3(cocos.layer.Layer):

    is_event_handler = True

    images = ['blue', 'green', 'yellow', 'red', 'black', 'cyan', 'purple', 'orange']

    def __init__(self):
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

    def createPiece(self, x, y):
        color = random.sample(Rpg3.images, 1)[0]
        piece = cocos.sprite.Sprite('images/%s.png' % color)
        piece.position = self.spriteSize * (y + 1), self.spriteSize * (x + 1)
        self.add(piece)
        return (color, piece)

    def createCell(self, x, y):
        color, piece = self.createPiece(x, y)
        return cell.Cell((x, y), theData=color, theSprite=piece)

    def createTableBoard(self, theSize):
        #matrix = []
        matrix = [[self.createCell(x, y) for y in xrange(theSize)] for x in xrange(theSize)]
        #for col in xrange(theSize):
        #    cols = []
        #    for row in xrange(theSize):
        #        cols.append(self.createCell(row, col))
        #    matrix.append(cols)
        return tableboard.TableBoard(theSize, matrix)

    def celSelected(self):
        selected = []
        for x in xrange(self.size):
            for y in xrange(self.size):
                aCell = self.tableboard.getCell((x, y))
                if aCell.isSelected():
                    selected.append(aCell)
        return selected

    def on_mouse_press(self, x, y, buttons, modifiers):
        for xPos in xrange(self.size):
            for yPos in xrange(self.size):
                self.tableboard.getCell((xPos, yPos)).select(x, y)
        cells = self.celSelected()
        if len(cells) == 2:
            self.tableboard.swapCells(*cells)
            #cells[0].getSprite().image, cells[1].getSprite().image = cells[1].getSprite().image, cells[0].getSprite().image
            for aCell in cells:
                aCell.select()
        matches = self.tableboard.matchBoard()
        print matches
        print self.tableboard.printLogBoard()
        rowMatches, colMatches = matches
        for match in rowMatches:
            for pos in match:
                self.tableboard.setCellData(pos, None)
        for match in colMatches:
            for pos in match:
                self.tableboard.setCellData(pos, None)
        self.tableboard.fallBoard()
        print self.tableboard.emptyCellsInBoard()
        print self.tableboard.printLogBoard()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
