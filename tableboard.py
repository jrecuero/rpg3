import loggerator
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


#
#------------------------------------------------------------------------------
class TableBoard(object):

    #--------------------------------------------------------------------------
    def __init__(self, theSize, theMatrix=None, theNewCellCb=None):
        """ TableBoard initialization method.

        :type theSize: int
        :param theSize: Size of the board (size x size).

        :type theMatrix: list
        :param theMatrix: Matrix to be used for the tableboard

        :type theNewCellCb: func
        :param theNewCellCb: Function to be called to create a new cell
        """
        self.size      = theSize
        self.newCellCb = theNewCellCb
        self.matrix = theMatrix if theMatrix else self._createDefaultTableBoard()
        self.logger = loggerator.getLoggerator('tableboard')

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
    def _createDefaultTableBoard(self):
        """ Create a new default table board

        :rtype: list
        :return: matrix with a default table board
        """
        return [[self.newCellCb((x, y)) for y in xrange(self.size)] for x in xrange(self.size)]

    #--------------------------------------------------------------------------
    def addNewCell(self, thePosition):
        """ Create a new cell at the given position

        :type thePosition: tuple
        :param thePosition: Tuple with x and y position coordinates

        :rtype: Cell
        :return: New cell instance
        """
        x, y  = thePosition
        aCell = self.newCellCb(thePosition)
        self.matrix[x][y] = aCell
        return aCell

    #--------------------------------------------------------------------------
    def removeCell(self, thePosition):
        """ Remove a cell from the given position

        :type thePosition: tuple
        :param thePosition: Tuple with x and y position coordinates

        :rtype: Cell
        :return: Cell instance being removed
        """
        x, y  = thePosition
        aCell = self.getCell(thePosition)
        self.matrix[x][y] = None
        return aCell

    #--------------------------------------------------------------------------
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
                #self.logger.debug('%s %s %s %s' % (theSide, firstLoopIdx, secondLoopIdx, match))
                position  = MOVE_IN_BOARD[theSide]['loopFunc'](firstLoopIdx, secondLoopIdx)
                traverseMatch = set()
                inc = self.findMatch(position, self.getCellData(position), 0, traverseMatch, theSide)
                if inc >= MIN_MATCH:
                    traverseListMatch = list(traverseMatch)
                    traverseListMatch.sort()
                    match.append(traverseListMatch)
                secondLoopIdx += inc
        return match

    #--------------------------------------------------------------------------
    def isValueIn(self, theValue):
        """ Check if the given value is inside the range.

        :type theValue: int
        :param theValue: Value t o check.

        :rtype: boolean
        :return: True if position is in the range. False if it is outside.
        """
        return theValue in xrange(self.size)

    #--------------------------------------------------------------------------
    def isCellInBoard(self, thePosition):
        """ Check if the given cell is inside the board.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: boolean
        :return: True if position is inside the board. False if it is outside.
        """
        x, y = thePosition
        return self.isValueIn(x) and self.isValueIn(y)

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
    def getCellData(self, thePosition):
        """ Get the cell data instance for a given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: object
        :return: The data object instance for the given position.
        """
        aCell = self.getCell(thePosition)
        return aCell.getData() if aCell else None

    #--------------------------------------------------------------------------
    def getCellSprite(self, thePosition):
        """ Get the cell sprite instance for a given position.

        :type thePosition: list
        :param thePosition: Point with the position.

        :rtype: object
        :return: The sprite object instance for the given position.
        """
        aCell = self.getCell(thePosition)
        return aCell.getSprite() if aCell else None

    #--------------------------------------------------------------------------
    def iterCell(self):
        """ Iterate all cells in the matrix.

        :rtype: iterator
        :return: iterator with next cell in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell

    #--------------------------------------------------------------------------
    def iterCellData(self):
        """ Iterate all cells data in the matrix.

        :rtype: iterator
        :return: iterator with next cell data in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell.getData()

    #--------------------------------------------------------------------------
    def iterCellSprite(self):
        """ Iterate all cells sprite in the matrix.

        :rtype: iterator
        :return: iterator with next cell sprite in the matrix
        """
        for row in self.matrix:
            for aCell in row:
                yield aCell.getSprite()

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
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
        self.logger.debug("Swap (%s, %s) %s for (%s, %s) %s" % (x1, y1, theFirstCell.data, x2, y2, theSecondCell.data))
        theFirstCell.swap(theSecondCell)
        self.matrix[x1][y1], self.matrix[x2][y2] = self.matrix[x2][y2], self.matrix[x1][y1]
        return True

    #--------------------------------------------------------------------------
    def fallCell(self, theCell):
        """ Move down all non-empty cells on top of the given one.

        :type theCell: Cell
        :param theCell: Cells on top of this will be moved down
        """
        if theCell.getData() is None:
            self.logger.debug('falling cell %s %s' % (theCell.getPosition(), theCell.getData()))
            x, y = theCell.getPosition()
            if x == (self.size - 1):
                return -1
            topCell = self.matrix[x + 1][y]
            if topCell.getData() is None:
                if self.fallCell(topCell) == -1:
                    return -1
            topCell = self.matrix[x + 1][y]
            self.swapCells(theCell, topCell)
        else:
            return 0

    #--------------------------------------------------------------------------
    def isMatch(self, theValue, theMatch):
        """ Check if the given value is a valid match.

        :type theValue: object
        :param theValue: Value to match.

        :rtype: boolean
        :return: True if value is a valid match. False if it is not.
        """
        return theValue == theMatch or theMatch == WILDCARD

    #--------------------------------------------------------------------------
    def incPosition(self, thePosition, theSide):
        """ Increase a traverse cell through the board in a given direction.

        :type thePosition: list
        :param thePostion: Point with the initial position.

        :type theSide: object
        :param theSide: Direction to traverse.
        """
        newPosition = MOVE_IN_BOARD[theSide]['incFunc'](thePosition)
        return None if False in map(self.isValueIn, newPosition) else newPosition

    #--------------------------------------------------------------------------
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
        #self.logger.debug("pos: (%s, %s), value: %s data: %s" % (x, y, theValue, self.getCellData(thePosition)))
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

    #--------------------------------------------------------------------------
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

    #--------------------------------------------------------------------------
    def matchBoard(self):
        """ Look for matches in all the board.

        :rtype: list
        :return: List with all matches found in the board.
        """
        matches = []
        for side in ('right', 'down'):
            matches.append(self._loopForCells(side))
        self.logger.debug('matches: %s' % (matches, ))
        return matches

    #--------------------------------------------------------------------------
    def defaultMatches(self):
        """ Return default matches list to be used in a loop

        :rtype: list
        :return: List with default values to be used in a loop
        """
        return [True, True]

    #--------------------------------------------------------------------------
    def isThereAnyMatch(self, theMatches):
        """ Check if there is any match in the parameter passed

        :type theMatches: list
        :param theMatches: list with row and column matches

        :rtype: bool
        :return: True if there is any match, else False
        """
        return theMatches[0] or theMatches[1]

    #--------------------------------------------------------------------------
    def emptyCellsInBoard(self):
        """ Look for cells with None data

        :rtype: list
        :return: List with all cells wiht None data
        """
        matches = []
        for aCell in self.iterCell():
            if aCell.data is None:
                matches.append(aCell)
        return matches

    #--------------------------------------------------------------------------
    def setEmptyCells(self, theMatches):
        """ Set Cell data to none for all position being passed

        :type theMatches: list
        :param theMatches: Row and Column lists with matches to None
        """
        rowMatches, colMatches = theMatches
        for match in rowMatches:
            for pos in match:
                self.setCellData(pos, None)
        for match in colMatches:
            for pos in match:
                self.setCellData(pos, None)

    #--------------------------------------------------------------------------
    def fallBoard(self):
        """ Traverse all cells in the board and make then fall
        """
        for aCell in self.iterCell():
            self.fallCell(aCell)

    #--------------------------------------------------------------------------
    def logBoard(self):
        """ Log all board information
        """
        for x in xrange(self.size):
            row = ""
            for y in xrange(self.size):
                pos = (x, y)
                c = self.getCell(pos)
                row += '%s %s' % (c.position, c.data)
            self.logger.debug('%s' % (row, ))

    #--------------------------------------------------------------------------
    def matchResults(self, theMatches):
        stats = cell.Cell.getStats()
        statsDict = cell.Cell.createStatsDict()
        for matchLines in theMatches:
            for match in matchLines:
                for stat in stats:
                    # every match should be the same, so just use the first one
                    # to retrieve the match calculation method to be used.
                    matchStatFunc = getattr(self.getCell(match[0]), stat, None)
                    if matchStatFunc:
                        statsDict[stat] += matchStatFunc(match)
                for stat in stats:
                    self.logger.info("Match %s  = %d" % (stat, statsDict[stat]))
        return statsDict


if __name__ == '__main__':
    #import unittest
    #import test.test_tableboard as testTB
    #runner = unittest.TextTestRunner(verbosity=2)
    #runner.run(testTB.TableBoardTestSuite())
    pass
