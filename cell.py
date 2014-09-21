class Cell(object):

    def __init__(self, thePosition, **kwargs):
        """ Cell initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Sword name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        self.position = thePosition
        self.data     = kwargs['theData'] if 'theData' in kwargs else None
        self.name     = kwargs['theName'] if 'theName' in kwargs else None
        self.sprite   = kwargs['theSprite'] if 'theSprite' in kwargs else None
        self.damage   = kwargs['theDamage'] if 'theDamage' in kwargs else None
        self.defense  = kwargs['theDefense'] if 'theDefense' in kwargs else None
        self.money    = kwargs['theMoney']  if 'theMoney' in kwargs else None
        self.health   = kwargs['theHealth'] if 'theHealth' in kwargs else None
        self.power    = kwargs['thePower'] if 'thePower' in kwargs else None
        self.selected = False

    def getName(self):
        return self.name

    def setName(self, theName):
        self.name = theName
        return True

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

    def getDamage(self):
        return self.damage

    def setDamage(self, theDamage):
        self.damage = theDamage
        return True

    def getDefense(self):
        return self.defense

    def setDefense(self, theDefense):
        self.defense = theDefense
        return True

    def getMoney(self):
        return self.money

    def setMoney(self, theMoney):
        self.money = theMoney
        return True

    def getHealth(self):
        return self.health

    def setHealth(self, theHealth):
        self.health = theHealth
        return True

    def getPower(self):
        return self.power

    def setPower(self, thePower):
        self.power = thePower
        return True

    def isSelected(self):
        return self.selected

    def _select(self):
        self.selected = not self.selected
        self.getSprite().opacity = 125 if self.selected else 255

    def select(self, x=None, y=None):
        if (x is None and y is None) or self.getSprite().contains(x, y):
            self._select()

    def swap(self, theOther):
        self.position, theOther.position = theOther.position, self.position,
        #self.sprite.image, theOther.sprite.image = theOther.sprite.image, self.sprite.image
        self.sprite.position, theOther.sprite.position = theOther.sprite.position, self.sprite.position


#if __name__ == '__main__':
#    import unittest
#    import test.test_cell as testCell
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(testCell.CellTestSuite())
