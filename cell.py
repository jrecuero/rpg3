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
