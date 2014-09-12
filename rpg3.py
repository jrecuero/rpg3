import cocos
import pyglet
from pyglet.gl import glPushMatrix, glPopMatrix

COUNT_LIMIT = 100
MIN_MATCH   = 3
WILDCARD    = 9
BOARD_SIZE  = 8

AXE_X = 1
AXE_Y = 2

DIR_RIGHT = 1
DIR_LEFT  = 2
DIR_UP    = 3
DIR_DOWN  = 4


def _updatePositionLoopToRight(theFirstLoopIdx, theSecondLoopIdx):
    return(theFirstLoopIdx, theSecondLoopIdx)


def _updatePostionLoopToDown(theFirstLoopIdx, theSecondLoopIdx):
    return(theSecondLoopIdx, theFirstLoopIdx)


MOVE_IN_BOARD = {'right': {'loopFunc':  lambda first, second: (first, second),
                           'incFunc':   lambda (x, y): (x, y + 1),
                           'axe':       AXE_X,
                           'direction': DIR_RIGHT},
                 'left':  {'loopFunc':  lambda first, second: (first, second),
                           'incFunc':   lambda (x, y): (x, y - 1),
                           'axe':       AXE_X,
                           'direction': DIR_LEFT},
                 'down':  {'loopFunc':  lambda first, second: (second, first),
                           'incFunc':   lambda (x, y): (x + 1, y),
                           'axe':       AXE_Y,
                           'direction': DIR_DOWN},
                 'up':    {'loopFunc':  lambda first, second: (second, first),
                           'incFunc':   lambda (x, y): (x - 1, y),
                           'axe':       AXE_Y,
                           'direction': DIR_UP}, }


matrix = [[0 for x in xrange(BOARD_SIZE)] for x in xrange(BOARD_SIZE)]


def incPosition(thePosition, theAxe, theDirection, theSize):
    x, y = thePosition
    moveOp = 1
    if theDirection == DIR_UP or theDirection == DIR_LEFT:
        moveOp = -1
    if theAxe == AXE_X:
        y += moveOp
    elif theAxe == AXE_Y:
        x += moveOp
    if x >= theSize or y >= theSize or x < 0 or y < 0:
        return None
    return (x, y)


def isMatch(theValue, theMatch):
    return theValue == theMatch or theMatch == WILDCARD


def findMatch(theMatrix, thePosition, theValue, theCounter, theMatchSet, theAxe, theDirection, theSize):
    x, y = thePosition
    if isMatch(theValue, theMatrix[x][y]):
        theCounter += 1
        theMatchSet.add(thePosition)
        if theCounter == COUNT_LIMIT:
            return theCounter
        else:
            newPosition = incPosition(thePosition, theAxe, theDirection, theSize)
            return findMatch(theMatrix, newPosition, theValue, theCounter, theMatchSet, theAxe, theDirection, theSize) if newPosition else theCounter
    else:
        return theCounter


def matchAtCell(theMatrix, thePosition, theSize):
    xMatch = set()
    yMatch = set()
    x, y = thePosition
    findMatch(theMatrix, thePosition, theMatrix[x][y], 0, xMatch, AXE_X, DIR_RIGHT, theSize)
    findMatch(theMatrix, thePosition, theMatrix[x][y], 0, xMatch, AXE_X, DIR_LEFT, theSize)
    findMatch(theMatrix, thePosition, theMatrix[x][y], 0, yMatch, AXE_Y, DIR_DOWN, theSize)
    findMatch(theMatrix, thePosition, theMatrix[x][y], 0, yMatch, AXE_Y, DIR_UP, theSize)
    return (list(xMatch), list(yMatch))


def matchBoard(theMatrix, theSize):
    xMatch = []
    yMatch = []
    for x in xrange(theSize):
        y = 0
        while y <= (theSize - 2):
            match = set()
            inc = findMatch(theMatrix, (x, y), theMatrix[x][y], 0, match, AXE_X, DIR_RIGHT, theSize)
            if inc >= MIN_MATCH:
                xMatch.append(list(match))
            y += inc
    for y in xrange(theSize):
        x = 0
        while x <= (theSize - 2):
            match = set()
            inc = findMatch(theMatrix, (x, y), theMatrix[x][y], 0, match, AXE_Y, DIR_DOWN, theSize)
            if inc >= MIN_MATCH:
                yMatch.append(list(match))
            x += inc
    return (xMatch, yMatch)


class Cell(object):

    def __init__(self, thePosition, theSprite, theData):
        self.position = thePosition
        self.sprite   = theSprite
        self.data     = theData

    def getData(self):
        return self.data

    def setData(self, theData):
        self.data = theData
        return True


class TableBoard(object):

    def __init__(self, theSize):
        self.size   = theSize
        self.matrix = [[None for x in xrange(theSize)] for x in xrange(theSize)]

    def isCellInBoard(self, thePosition):
        x, y = thePosition
        return (x >= 0) and (x < self.size) and (y >= 0) and (y < self.size)

    def getCell(self, thePosition):
        if self.isCellInBoard(thePosition):
            x, y = thePosition
            return self.matrix[x][y]
        else:
            return None

    def getCellData(self, thePosition):
        cell = self.getCell(thePosition)
        return cell.getData() if cell else None

    def setCell(self, thePosition, theCell):
        if self.isCellInBoard(thePosition):
            x, y = thePosition
            self.matrix[x][y] = theCell
            return True
        else:
            return False

    def setCellData(self, thePosition, theData):
        cell = self.getCell(thePosition)
        return cell.setData(theData) if cell else False

    def swapCells(self, theFirstCell, theSecondCell):
        x1, y1 = theFirstCell.position
        x2, y2 = theSecondCell.position
        self.matrix[x1][y1], self.matrix[x2][y2] = self.matrix[x2][y2], self.matrix[x1][y1]

    def isValueIn(self, theValue):
        return (theValue >= 0) and (theValue < self.size)

    #def incPosition(self, thePosition, theAxe, theDirection):
    #    x, y = thePosition
    #    moveOp = 1
    #    if theDirection == DIR_UP or theDirection == DIR_LEFT:
    #        moveOp = -1
    #    if theAxe == AXE_X:
    #        y += moveOp
    #    elif theAxe == AXE_Y:
    #        x += moveOp
    #    if x >= self.size or y >= self.size or x < 0 or y < 0:
    #        return None
    #    return (x, y)

    def incPosition(self, thePosition, theSide):
        newPosition = MOVE_IN_BOARD[theSide]['incFunc'](thePosition)
        return None if False in filter(self.isValueIn, newPosition) else newPosition

    def isMatch(self, theValue, theMatch):
        return theValue == theMatch or theMatch == WILDCARD

    def findMatch(self, thePosition, theValue, theCounter, theMatchSet, theSide):
        x, y = thePosition
        if self.isMatch(theValue, self.getCellData(thePosition)):
            theCounter += 1
            theMatchSet.add(thePosition)
            if theCounter == COUNT_LIMIT:
                return theCounter
            else:
                #newPosition = self.incPosition(thePosition, theAxe, theDirection)
                newPosition = self.incPosition(thePosition, theSide)
                return self.findMatch(newPosition, theValue, theCounter, theMatchSet, theSide) if newPosition else theCounter
        else:
            return theCounter

    def matchAtCell(self, thePosition):
        xMatch = set()
        yMatch = set()
        self.findMatch(thePosition, self.getCellData(thePosition), 0, xMatch, AXE_X, DIR_RIGHT)
        self.findMatch(thePosition, self.getCellData(thePosition), 0, xMatch, AXE_X, DIR_LEFT)
        self.findMatch(thePosition, self.getCellData(thePosition), 0, yMatch, AXE_Y, DIR_DOWN)
        self.findMatch(thePosition, self.getCellData(thePosition), 0, yMatch, AXE_Y, DIR_UP)
        return (list(xMatch), list(yMatch))

    def _loopForCells(self, theSide):
        match = []
        for firstLoopIdx in xrange(self.size):
            secondLoopIdx = 0
            while secondLoopIdx <= (self.size - 2):
                position  = MOVE_IN_BOARD[theSide]['loopFunc'](firstLoopIdx, secondLoopIdx)
                axe       = MOVE_IN_BOARD[theSide]['axe']
                direction = MOVE_IN_BOARD[theSide]['direction']
                traverseMatch = set()
                inc = self.findMatch(position, self.getCellData(position), 0, traverseMatch, axe, direction)
                if inc >= MIN_MATCH:
                    match.append(list(traverseMatch))
                secondLoopIdx += inc
        return match

    def matchBoard(self):
        match = []
        for side in ('right', 'down'):
            match.append(self._loopForCells(side))
        return match
        #xMatch = []
        #yMatch = []
        #for x in xrange(self.size):
        #    y = 0
        #    while y <= (self.size - 2):
        #        position = (x, y)
        #        match = set()
        #        inc = self.findMatch(position, self.getCellData(position), 0, match, AXE_X, DIR_RIGHT)
        #        if inc >= MIN_MATCH:
        #            xMatch.append(list(match))
        #        y += inc
        #for y in xrange(self.size):
        #    x = 0
        #    while x <= (self.size - 2):
        #        position = (x, y)
        #        match = set()
        #        inc = self.findMatch(position, self.getCellData(position), 0, match, AXE_Y, DIR_DOWN)
        #        if inc >= MIN_MATCH:
        #            yMatch.append(list(match))
        #        x += inc
        #return (xMatch, yMatch)


class Rpg3(cocos.layer.Layer):

    def __init__(self, images):
        super(Rpg3, self).__init__()
        self.images = images
        label = cocos.text.Label('RPG Match 3',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)

    def draw(self):
        glPushMatrix()

        x = 10
        for img in images:
            img.blit(x, 10)
            x += 64

        glPopMatrix()


if __name__ == '__main__':
    pyglet.resource.path.append('images')
    pyglet.resource.reindex()

    images = []
    images.append(pyglet.resource.image('blue.png'))
    images.append(pyglet.resource.image('green.png'))
    images.append(pyglet.resource.image('yellow.png'))
    images.append(pyglet.resource.image('red.png'))
    images.append(pyglet.resource.image('black.png'))
    images.append(pyglet.resource.image('cyan.png'))

    cocos.director.director.init()
    rpg3Layer = Rpg3(images)
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)
