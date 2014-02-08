import unittest
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(ROOT)

import cell

ORIGIN = (0, 0)
DATA   = 'data'
SPRITE = 'sprite'


#------------------------------------------------------------------------------
def CellTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(CellTestCase("test_create"))
    suite.addTest(CellTestCase("test_getData"))
    suite.addTest(CellTestCase("test_getSprite"))
    suite.addTest(CellTestCase("test_setData"))
    suite.addTest(CellTestCase("test_setSprite"))
    return suite


#
#------------------------------------------------------------------------------
#
class CellTestCase(unittest.TestCase):

    def setUp(self):
        self.cell = cell.Cell(ORIGIN, SPRITE, DATA)

    def tearDown(self):
        self.tb = None

    def test_create(self):
        self.assertEqual(self.cell.position, ORIGIN)
        self.assertEqual(self.cell.data, DATA)
        self.assertEqual(self.cell.sprite, SPRITE)

    def test_getData(self):
        self.assertEqual(self.cell.getData(), DATA)

    def test_getSprite(self):
        self.assertEqual(self.cell.getSprite(), SPRITE)

    def test_setData(self):
        NEW_DATA = 'new data'
        self.assertTrue(self.cell.setData(NEW_DATA))
        self.assertEqual(self.cell.getData(), NEW_DATA)

    def test_setSprite(self):
        NEW_SPRITE = 'new sprite'
        self.assertTrue(self.cell.setSprite(NEW_SPRITE))
        self.assertEqual(self.cell.getSprite(), NEW_SPRITE)

#if __name__ == '__main__':
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(CellTestSuite())
