import unittest
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(ROOT)

import rpg3

SIZE = 8


#------------------------------------------------------------------------------
def Rpg3TestSuite():
    suite = unittest.TestSuite()
    suite.addTest(Rpg3TestCase("test_create"))
    return suite


#
#------------------------------------------------------------------------------
#
class Rpg3TestCase(unittest.TestCase):

    def setUp(self):
        self.tb = rpg3.Rpg3()

    def tearDown(self):
        self.tb = None

    def test_create(self):
        pass


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(Rpg3TestSuite())
