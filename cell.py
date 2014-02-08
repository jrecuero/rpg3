class Cell(object):

    def __init__(self, thePosition, theSprite=None, theData=None):
        self.position = thePosition
        self.sprite   = theSprite
        self.data     = theData

    def getData(self):
        return self.data

    def setData(self, theData):
        self.data = theData
        return True

    def getSprite(self):
        return self.sprite

    def setSprite(self, theSprite):
        self.sprite = theSprite
        return True


if __name__ == '__main__':
    import unittest
    import test.test_cell as testCell
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testCell.CellTestSuite())
