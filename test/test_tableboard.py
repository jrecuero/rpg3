import unittest
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(ROOT)


import tableboard

SIZE = 8


#------------------------------------------------------------------------------
def TableBoardTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(TableBoardTestCase("test_create"))
    suite.addTest(TableBoardTestCase("test_getCell"))
    suite.addTest(TableBoardTestCase("test_setCell"))
    suite.addTest(TableBoardTestCase("test_getCellData"))
    suite.addTest(TableBoardTestCase("test_getCellSprite"))
    suite.addTest(TableBoardTestCase("test_setCellData"))
    suite.addTest(TableBoardTestCase("test_setCellSprite"))
    suite.addTest(TableBoardTestCase("test_swapCells"))
    suite.addTest(TableBoardTestCase("test_isValueIn"))
    suite.addTest(TableBoardTestCase("test_isMatch"))
    suite.addTest(TableBoardTestCase("test_incPosition"))
    suite.addTest(TableBoardTestCase("test_findMatch"))
    suite.addTest(TableBoardTestCase("test_matchAtCell"))
    suite.addTest(TableBoardTestCase("test_matchBoard"))
    return suite


#
#------------------------------------------------------------------------------
#
class TableBoardTestCase(unittest.TestCase):

    def _createTestBoard(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.tb.setCellData((x, y), 0)

    def _createTestBoardNoMatch(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.tb.setCellData((x, y), 10 + x + y)

    def setUp(self):
        self.tb = tableboard.TableBoard(SIZE)

    def tearDown(self):
        self.tb = None

    def test_create(self):
        self.assertEqual(self.tb.size, SIZE)
        self.assertEqual(len(self.tb.matrix), SIZE)
        x = 0
        for row in self.tb.matrix:
            y = 0
            self.assertEqual(len(row), SIZE)
            for col in row:
                self.assertEqual(col.position, (x, y))
                self.assertIsNone(col.sprite)
                self.assertIsNone(col.data)
                y += 1
            x += 1

    def test_getCell(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertIsNotNone(self.tb.getCell((x, y)))
                self.assertEqual(self.tb.getCell((x, y)).position, (x, y))
        self.assertIsNone(self.tb.getCell((SIZE, SIZE)))

    def test_setCell(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertTrue(self.tb.setCell((x, y), (x, y)))
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertEqual(self.tb.getCell((x, y)), (x, y))
        self.assertFalse(self.tb.setCell((SIZE, SIZE), (0, 0)))

    def test_getCellData(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertIsNone(self.tb.getCellData((x, y)))

    def test_getCellSprite(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertIsNone(self.tb.getCellSprite((x, y)))

    def test_setCellData(self):
        NEW_DATA = 'new data'
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertTrue(self.tb.setCellData((x, y), NEW_DATA))
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertEqual(self.tb.getCellData((x, y)), NEW_DATA)

    def test_setCellSprite(self):
        NEW_SPRITE = 'new sprite'
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertTrue(self.tb.setCellSprite((x, y), NEW_SPRITE))
        for x in xrange(SIZE):
            for y in xrange(SIZE):
                self.assertEqual(self.tb.getCellSprite((x, y)), NEW_SPRITE)

    def test_swapCells(self):
        pos1 = (0, 0)
        pos2 = (1, 1)
        cell1 = self.tb.getCell(pos1)
        cell2 = self.tb.getCell(pos2)
        self.assertTrue(self.tb.swapCells(cell1, cell2))
        self.assertEqual(self.tb.getCell(pos1), cell2)
        self.assertEqual(self.tb.getCell(pos2), cell1)

    def test_isValueIn(self):
        for x in xrange(-SIZE, 0):
            self.assertFalse(self.tb.isValueIn(x))
        for x in xrange(SIZE):
            self.assertTrue(self.tb.isValueIn(x))
        for x in xrange(SIZE, SIZE + 10):
            self.assertFalse(self.tb.isValueIn(x))

    def test_isMatch(self):
        MATCH = 'match'
        NO_MATCH = 'no match'
        self.assertTrue(self.tb.isMatch(MATCH, MATCH))
        self.assertFalse(self.tb.isMatch(MATCH, NO_MATCH))
        self.assertTrue(self.tb.isMatch(MATCH, tableboard.WILDCARD))
        self.assertTrue(self.tb.isMatch(NO_MATCH, tableboard.WILDCARD))

    def test_incPosition(self):
        for x in xrange(SIZE):
            for y in xrange(SIZE - 1):
                self.assertEqual(self.tb.incPosition((x, y), 'right'), (x, y + 1))
            self.assertIsNone(self.tb.incPosition((x, SIZE), 'right'))
        for x in xrange(SIZE):
            for y in xrange(SIZE - 1, 0, -1):
                self.assertEqual(self.tb.incPosition((x, y), 'left'), (x, y - 1))
            self.assertIsNone(self.tb.incPosition((x, 0), 'left'))
        for y in xrange(SIZE):
            for x in xrange(SIZE - 1):
                self.assertEqual(self.tb.incPosition((x, y), 'down'), (x + 1, y))
            self.assertIsNone(self.tb.incPosition((SIZE, y), 'down'))
        for y in xrange(SIZE):
            for x in xrange(SIZE - 1, 0, -1):
                self.assertEqual(self.tb.incPosition((x, y), 'up'), (x - 1, y))
            self.assertIsNone(self.tb.incPosition((0, y), 'up'))

    def test_findMatch(self):
        self._createTestBoard()
        matchSet = set()
        matchCellPos = [(1, 1), (1, 2), (1, 3)]
        lenToMatch   = len(matchCellPos)
        valueToMatch = 1
        for pos in matchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        self.assertEqual(self.tb.findMatch(matchCellPos[0], valueToMatch, 0, matchSet, 'right'), lenToMatch)
        matchList = list(matchSet)
        matchList.sort()
        self.assertEqual(matchList, matchCellPos)

        self._createTestBoard()
        matchSet = set()
        matchCellPos = [(1, 1), (2, 1), (3, 1), (4, 1)]
        lenToMatch   = len(matchCellPos)
        valueToMatch = 2
        for pos in matchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        self.assertEqual(self.tb.findMatch(matchCellPos[0], valueToMatch, 0, matchSet, 'down'), lenToMatch)
        matchList = list(matchSet)
        matchList.sort()
        self.assertEqual(matchList, matchCellPos)

        self._createTestBoard()
        matchSet = set()
        matchCellPos = [(1, 1), (1, 2), (1, 3)]
        lenToMatch   = len(matchCellPos)
        valueToMatch = 1
        wrongValue   = 2
        for pos in matchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        self.assertEqual(self.tb.findMatch(matchCellPos[0], wrongValue, 0, matchSet, 'right'), 0)
        matchList = list(matchSet)
        self.assertEqual(matchList, [])

    def test_matchAtCell(self):
        self._createTestBoard()
        matchCellPos = [(1, 1), (1, 2), (1, 3)]
        valueToMatch = 1
        for pos in matchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        (xresult, yresult) = self.tb.matchAtCell(matchCellPos[0])
        self.assertEqual(xresult, matchCellPos)
        self.assertEqual(yresult, [matchCellPos[0], ])

        self._createTestBoard()
        valueToMatch = 1
        xMatchCellPos = [(1, 1), (1, 2), (1, 3)]
        yMatchCellPos = [(1, 1), (2, 1), (3, 1)]
        for pos in xMatchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        for pos in yMatchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        (xresult, yresult) = self.tb.matchAtCell(xMatchCellPos[0])
        self.assertEqual(xresult, xMatchCellPos)
        self.assertEqual(yresult, yMatchCellPos)

    def test_matchBoard(self):
        self._createTestBoardNoMatch()
        valueToMatch = 1
        xMatchCellPos = [(1, 1), (1, 2), (1, 3)]
        yMatchCellPos = [(1, 1), (2, 1), (3, 1)]
        for pos in xMatchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        for pos in yMatchCellPos:
            self.tb.setCellData(pos, valueToMatch)
        result = self.tb.matchBoard()
        self.assertEqual(result[0][0], xMatchCellPos)
        self.assertEqual(result[1][0], yMatchCellPos)


#if __name__ == '__main__':
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(TableBoardTestSuite())
