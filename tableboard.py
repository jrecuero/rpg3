import cell


COUNT_LIMIT = 100
MIN_MATCH   = 3
WILDCARD    = 9

AXE_X = 1
AXE_Y = 2

DIR_RIGHT = 1
DIR_LEFT  = 2
DIR_UP    = 3
DIR_DOWN  = 4


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


class TableBoard(object):

    def __init__(self, theSize, theMatrix=None):
        """ TableBoard initialization method.

        :type theSize: int
        :param theSize: Size of the board (size x size).

        :type theMatrix: list
        :param theMatrix: Matrix to be used for the tableboard
        """
        self.size   = theSize
        if theMatrix:
            self.matrix = theMatrix
        else:
            self.matrix = [[cell.Cell((x, y)) for y in xrange(theSize)] for x in xrange(theSize)]

    def _copyToListAndSort(self, theSet):
        """ Copy a set to a list and sort the list result.

        :type theSet: set
        :param theSet: Set instance to copy and sort.

        :rtype: list
        :return: Sorted list with the given set content.
        """
        lista = list(theSet)
        lista.sort()
        return lista

    def _loopForCells(self, theSide):
        """ Loop a row or a column for matches.

        :type theSide: object
        :param theSide: Direction to traverse for finding matches.

        :rtype: list
        :return: List with all matches for the give direction.
        """
        match = []
        for firstLoopIdx in xrange(self.size):
            secondLoopIdx = 0
            # We don't have to loop until the end, because if it does not find
            # a match at MIN_MATCH - 1, it is not going to find it in what is
            # left.
            while secondLoopIdx <= (self.size - (MIN_MATCH - 1)):
                #print ('%s %s %s %s' % (theSide, firstLoopIdx, secondLoopIdx, match))
                position  = MOVE_IN_BOARD[theSide]['loopFunc'](firstLoopIdx, secondLoopIdx)
                traverseMatch = set()
                inc = self.findMatch(position, self.getCellData(position), 0, traverseMatch, theSide)
                if inc >= MIN_MATCH:
                    traverseListMatch = list(traverseMatch)
                    traverseListMatch.sort()
                    match.append(traverseListMatch)
                secondLoopIdx += inc
        return match

    def isValueIn(self, theValue):
        """ Check if the given value is inside the range.

        :type theValue: int
        :param theValue: Value t o check.

        :rtype: boolean
        :return: True if position is in the range. False if it is outside.
        """
        return theValue in xrange(self.size)

    def isCellInBoard(self, thePosition):
        """ Check if the given cell is inside the board.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: boolean
        :return: True if position is inside the board. False if it is outside.
        """
        x, y = thePosition
        return self.isValueIn(x) and self.isValueIn(y)

    def getCell(self, thePosition):
        """ Get the cell instance for a given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: Cell
        :return: The Cell instance for the given position.
        """
        if self.isCellInBoard(thePosition):
            x, y = thePosition
            return self.matrix[x][y]
        else:
            return None

    def getCellData(self, thePosition):
        """ Get the cell data instance for a given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: object
        :return: The data object instance for the given position.
        """
        aCell = self.getCell(thePosition)
        return aCell.getData() if aCell else None

    def getCellSprite(self, thePosition):
        """ Get the cell sprite instance for a given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: object
        :return: The sprite object instance for the given position.
        """
        aCell = self.getCell(thePosition)
        return aCell.getSprite() if aCell else None

    def iterCell(self):
        """ Iterate all cells in the matrix.

        :rtype: iterator
        :return: iterator with next cell in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell

    def iterCellData(self):
        """ Iterate all cells data in the matrix.

        :rtype: iterator
        :return: iterator with next cell data in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell.getData()

    def iterCellSprite(self):
        """ Iterate all cells sprite in the matrix.

        :rtype: iterator
        :return: iterator with next cell sprite in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell.getSprite()

    def setCell(self, thePosition, theCell):
        """ Asign the given cell instance to the given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :type theCell: Cell
        :param theCell: Cell instance to insert in the table

        :rtype: boolean
        :return: True if cell was inserted. False if not (outside the baord).
        """
        if self.isCellInBoard(thePosition):
            x, y = thePosition
            self.matrix[x][y] = theCell
            return True
        else:
            return False

    def setCellData(self, thePosition, theData):
        """ Asign the given data instance to the given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :type theData: object
        :param theData: Data object instance to insert in the table

        :rtype: boolean
        :return: True if data was inserted. False if not (outside the baord).
        """
        aCell = self.getCell(thePosition)
        return aCell.setData(theData) if aCell else False

    def setCellSprite(self, thePosition, theSprite):
        """ Asign the given sprite instance to the given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :type theSprite: object
        :param theSprite: Sprite object instance to insert in the table

        :rtype: boolean
        :return: True if sprite was inserted. False if not (outside the baord).
        """
        aCell = self.getCell(thePosition)
        return aCell.setSprite(theSprite) if aCell else False

    def swapCells(self, theFirstCell, theSecondCell):
        """ Swap cell content for given position.

        Move cell from the second position to the second one, and viceverse.

        :type theFirstCell: Cell
        :param theFirstCell: First Cell instance to swap.

        :type theSecondCell: Cell
        :param theSecondCell: Second Cell instance to swap.

        :rtype: boolean
        :return: True.
        """
        x1, y1 = theFirstCell.position
        x2, y2 = theSecondCell.position
        #print "Swap (%s, %s) %s for (%s, %s) %s" % (x1, y1, theFirstCell.data, x2, y2, theSecondCell.data)
        theFirstCell.swap(theSecondCell)
        self.matrix[x1][y1], self.matrix[x2][y2] = self.matrix[x2][y2], self.matrix[x1][y1]
        return True

    def fallCell(self, theCell):
        print theCell.position, theCell.data
        if theCell.data is None:
            x, y = theCell.position
            if x == (self.size - 1):
                return -1
            topCell = self.matrix[x + 1][y]
            if topCell.data is None:
                if self.fallCell(topCell) == -1:
                    return -1
            self.swapCells(theCell, topCell)
        else:
            return 0

    def isMatch(self, theValue, theMatch):
        """ Check if the given value is a valid match.

        :type theValue: object
        :param theValue: Value to match.

        :rtype: boolean
        :return: True if value is a valid match. False if it is not.
        """
        return theValue == theMatch or theMatch == WILDCARD

    def incPosition(self, thePosition, theSide):
        """ Increase a traverse cell through the board in a given direction.

        :type thePosition: list
        :param thePostion: Point with the initial position.

        :type theSide: object
        :param theSide: Direction to traverse.
        """
        newPosition = MOVE_IN_BOARD[theSide]['incFunc'](thePosition)
        return None if False in map(self.isValueIn, newPosition) else newPosition

    def findMatch(self, thePosition, theValue, theCounter, theMatchSet, theSide):
        """ Find how many matches can be found in a given direction.

        :type thePosition: list
        :param thePosition: Point with position to check matches.

        :type theValue: object
        :param theValue: Value to check any match.

        :type theCounter: int
        :param theCounter: Number of matches.

        :type theMatchSet: set
        :param theMatchSet: Set with all points that match the value.

        :type theSide: object
        :param theSide: Direction to traverse for finding matches..
        """
        x, y = thePosition
        #print "pos: (%s, %s), value: %s data: %s" % (x, y, theValue, self.getCellData(thePosition))
        if self.isMatch(theValue, self.getCellData(thePosition)):
            theCounter += 1
            theMatchSet.add(thePosition)
            if theCounter == COUNT_LIMIT:
                return theCounter
            else:
                newPosition = self.incPosition(thePosition, theSide)
                return self.findMatch(newPosition, theValue, theCounter, theMatchSet, theSide) if newPosition else theCounter
        else:
            return theCounter

    def matchAtCell(self, thePosition):
        """ Find matches in all direction for a given position.

        :type thePosition: list
        :param thePosition: Point with the position to check all matches.

        :rtype: tuple
        :return: Tuple with all row and column matches.
        """
        xMatch = set()
        yMatch = set()
        self.findMatch(thePosition, self.getCellData(thePosition), 0, xMatch, 'right')
        self.findMatch(thePosition, self.getCellData(thePosition), 0, xMatch, 'left')
        self.findMatch(thePosition, self.getCellData(thePosition), 0, yMatch, 'down')
        self.findMatch(thePosition, self.getCellData(thePosition), 0, yMatch, 'up')
        return (self._copyToListAndSort(xMatch), self._copyToListAndSort(yMatch))

    def matchBoard(self):
        """ Look for matches in all the board.

        :rtype: list
        :return: List with all matches found in the board.
        """
        match = []
        for side in ('right', 'down'):
            match.append(self._loopForCells(side))
        return match

    def fallBoard(self):
        for aCell in self.iterCell():
            self.fallCell(aCell)

    def emptyCellsInBoard(self):
        match = []
        for aCell in self.iterCell():
            if aCell.data is None:
                match.append(aCell)
        return match

    def printLogBoard(self):
        for x in xrange(self.size):
            print '\n'
            for y in xrange(self.size):
                pos = (x, y)
                c = self.getCell(pos)
                print pos, c.position, c.data,
        print '\n'


if __name__ == '__main__':
    #import unittest
    #import test.test_tableboard as testTB
    #runner = unittest.TextTestRunner(verbosity=2)
    #runner.run(testTB.TableBoardTestSuite())
    pass
