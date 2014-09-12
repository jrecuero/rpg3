import cocos
import pyglet
import random


class Piece(cocos.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(Piece, self).__init__(*args, **kwargs)
        self.selected = False

    def select(self, x, y):
        if self.contains(x, y):
            self.selected = not self.selected
            self.opacity = 125 if self.selected else 255


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

    def on_mouse_press(self, x, y, buttons, modifiers):
        for piece in self.pieces:
            piece.select(x, y)

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
