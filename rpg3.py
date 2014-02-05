import cocos

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

    def setCell(self, thePosition, theCell):
        if self.isCellInBoard(thePosition):
            x, y = thePosition
            self.matrix[x][y] = theCell


class Rpg3(cocos.layer.Layer):

    def __init__(self):
        super(Rpg3, self).__init__()
        label = cocos.text.Label('RPG Match 3',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)


if __name__ == '__main__':
    cocos.director.director.init()
    rpg3Layer = Rpg3()
    mainScene = cocos.scene.Scene(rpg3Layer)
    cocos.director.director.run(mainScene)