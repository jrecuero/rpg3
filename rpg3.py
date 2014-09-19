import cocos
import pyglet
import random


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

        # self.pieces = [Piece('images/%s.png' % x) for x in Rpg3.images]
        self.pieces = []

        for x in xrange(1, 7):
            for y in xrange(1, 7):
                piece = self.createNewPiece()
                piece.position = 64 * x, 64 * y
                self.add(piece)
                self.pieces.append(piece)

    def piecesSelected(self):
        return [x for x in self.pieces if x.selected]

    def on_mouse_press(self, x, y, buttons, modifiers):
        for piece in self.pieces:
            piece.select(x, y)
        selected = self.piecesSelected()
        if len(selected) == 2:
            selected[0].image, selected[1].image = selected[1].image, selected[0].image
            for piece in selected:
                piece.select()

    def createNewPiece(self):
        color = random.sample(Rpg3.images, 1)[0]
        return Piece('images/%s.png' % color)


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
