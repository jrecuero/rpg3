class Cell(object):

    def __init__(self, thePosition, theName,  **kwargs):
        """ Cell initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Sword name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        self.position = thePosition
        self.name     = theName
        self.sprite   = kwargs['theSprite'] if 'theSprite' in kwargs else None
        self.damage   = kwargs['theDamage'] if 'theDamage' in kwargs else None
        self.defense  = kwargs['theDefense'] if 'theDefense' in kwargs else None
        self.money    = kwargs['theMoney']  if 'theMoney' in kwargs else None
        self.health   = kwargs['theHealth'] if 'theHealth' in kwargs else None
        self.power    = kwargs['thePower'] if 'thePower' in kwargs else None

    def getName(self):
        return self.name

    def setName(self, theName):
        self.name = theName
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
        return self.damage

    def setDefense(self, theDefense):
        self.damage = theDefense
        return True

    def getMoney(self):
        return self.damage

    def setMoney(self, theMoney):
        self.damage = theMoney
        return True

    def getHealth(self):
        return self.damage

    def setHealth(self, theHealth):
        self.damage = theHealth
        return True

    def getPower(self):
        return self.damage

    def setPower(self, thePower):
        self.damage = thePower
        return True


if __name__ == '__main__':
    import unittest
    import test.test_cell as testCell
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(testCell.CellTestSuite())
