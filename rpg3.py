import cocos
import pyglet
import random

import cell
import tableboard


class Piece(cocos.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Piece, self).__init__(*args, **kwargs)
        self.selected = False

    def _select(self):
        self.selected = not self.selected
        self.opacity = 125 if self.selected else 255

    def select(self, x=None, y=None):
        if (x is None and y is None) or self.contains(x, y):
            self._select()


class Rpg3(cocos.layer.Layer):

    is_event_handler = True

    images = ['blue', 'green', 'yellow', 'red', 'black', 'cyan']

    def __init__(self):
        super(Rpg3, self).__init__()
        label = cocos.text.Label('RPG Match 3',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)

        self.size = 8
        self.spriteSize = 64
        self.tableboard = self.createTableBoard(self.size)

    def createPiece(self, x, y):
        color = random.sample(Rpg3.images, 1)[0]
        piece = Piece('images/%s.png' % color)
        piece.position = self.spriteSize * x, self.spriteSize * y
        return (color, piece)

    def createCell(self, x, y):
        color, piece = self.createPiece(x, y)
        return cell.Cell((x, y), theData=color, theSprite=piece)

    def createTableBoard(self, theSize):
        matrix = [[self.createCell((x, y)) for y in xrange(theSize)] for x in xrange(theSize)]
        return tableboard.TableBoard(matrix)

    def piecesSelected(self):
        selected = []
        for x in xrange(self.size):
            for y in xrange(self.size):
                piece = self.tableboard.getCellSprite((x, y))
                if piece.selected:
                    selected.append(piece)
        return selected

    def on_mouse_press(self, x, y, buttons, modifiers):
        for xPos in xrange(self.size):
            for yPos in xrange(self.size):
                self.tableboard.getCellSprite((xPos, yPos)).select(x, y)
        selected = self.piecesSelected()
        if len(selected) == 2:
            selected[0].image, selected[1].image = selected[1].image, selected[0].image
            for piece in selected:
                piece.select()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
