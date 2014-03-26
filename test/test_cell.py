import unittest
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(ROOT)

import cell

ORIGIN  = (0, 0)
NAME    = 'cell test'
SPRITE  = 'sprite'
DAMAGE  = 100
DEFENSE = 200
MONEY   = 300
HEALTH  = 400
POWER   = 400


#------------------------------------------------------------------------------
def CellTestSuite():
    suite = unittest.TestSuite()
    suite.addTest(CellTestCase("test_create"))
    suite.addTest(CellTestCase("test_getName"))
    suite.addTest(CellTestCase("test_getSprite"))
    suite.addTest(CellTestCase("test_getDamage"))
    suite.addTest(CellTestCase("test_getDefense"))
    suite.addTest(CellTestCase("test_getMoney"))
    suite.addTest(CellTestCase("test_getHealth"))
    suite.addTest(CellTestCase("test_getPower"))
    suite.addTest(CellTestCase("test_setName"))
    suite.addTest(CellTestCase("test_setSprite"))
    suite.addTest(CellTestCase("test_setDamage"))
    suite.addTest(CellTestCase("test_setDefense"))
    suite.addTest(CellTestCase("test_setMoney"))
    suite.addTest(CellTestCase("test_setHealth"))
    suite.addTest(CellTestCase("test_setPower"))
    return suite


#
#------------------------------------------------------------------------------
#
class CellTestCase(unittest.TestCase):

    def setUp(self):
        self.cell = cell.Cell(ORIGIN,
                              NAME,
                              theSprite=SPRITE,
                              theDamage=DAMAGE,
                              theDefense=DEFENSE,
                              theMoney=MONEY,
                              theHealth=HEALTH,
                              thePower=POWER)

    def tearDown(self):
        self.tb = None

    def test_create(self):
        self.assertEqual(self.cell.position, ORIGIN)
        self.assertEqual(self.cell.name, NAME)
        self.assertEqual(self.cell.sprite, SPRITE)
        self.assertEqual(self.cell.damage, DAMAGE)
        self.assertEqual(self.cell.defense, DEFENSE)
        self.assertEqual(self.cell.money, MONEY)
        self.assertEqual(self.cell.health, HEALTH)
        self.assertEqual(self.cell.power, POWER)

    def test_getName(self):
        self.assertEqual(self.cell.getName(), NAME)

    def test_getSprite(self):
        self.assertEqual(self.cell.getSprite(), SPRITE)

    def test_getDamage(self):
        self.assertEqual(self.cell.getDamage(), DAMAGE)

    def test_getDefense(self):
        self.assertEqual(self.cell.getDefense(), DEFENSE)

    def test_getMoney(self):
        self.assertEqual(self.cell.getMoney(), MONEY)

    def test_getHealth(self):
        self.assertEqual(self.cell.getHealth(), HEALTH)

    def test_getPower(self):
        self.assertEqual(self.cell.getPower(), POWER)

    def test_setName(self):
        NEW_NAME = 'new cell name'
        self.assertTrue(self.cell.setNamName(NEW_NAME))
        self.assertEqual(self.cell.getName(), NEW_NAME)

    def test_setSprite(self):
        NEW_SPRITE = 'new sprite'
        self.assertTrue(self.cell.setSprite(NEW_SPRITE))
        self.assertEqual(self.cell.getSprite(), NEW_SPRITE)

    def test_setDamage(self):
        NEW_DAMAGE = 101
        self.assertTrue(self.cell.setDamage(NEW_DAMAGE))
        self.assertEqual(self.cell.getDamage(), NEW_DAMAGE)

    def test_setDefense(self):
        NEW_DEFENSE = 201
        self.assertTrue(self.cell.setDefense(NEW_DEFENSE))
        self.assertEqual(self.cell.getDefense(), NEW_DEFENSE)

    def test_setMoney(self):
        NEW_MONEY = 301
        self.assertTrue(self.cell.setMoney(NEW_MONEY))
        self.assertEqual(self.cell.getMoney(), NEW_MONEY)

    def test_setHealth(self):
        NEW_HEALTH = 401
        self.assertTrue(self.cell.setHealth(NEW_HEALTH))
        self.assertEqual(self.cell.getHealth(), NEW_HEALTH)

    def test_setPower(self):
        NEW_POWER = 501
        self.assertTrue(self.cell.setPower(NEW_POWER))
        self.assertEqual(self.cell.getPower(), NEW_POWER)


#if __name__ == '__main__':
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(CellTestSuite())
