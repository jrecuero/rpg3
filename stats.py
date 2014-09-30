import loggerator


EXP_NEXT_LEVEL = 100


#
#------------------------------------------------------------------------------
class Stats (object):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self):
        """ Initialize Stats instance
        """
        self.level  = 0
        self.exp    = 0
        self.money  = 0
        self.shield = 0
        self.health = 0
        self.power  = 0
        self.axe    = 0
        self.bow    = 0
        self.dagger = 0
        self.lance  = 0
        self.staff  = 0
        self.sword  = 0
        self.logger = loggerator.getLoggerator('stat')

    #--------------------------------------------------------------------------
    def addExp(self, theExp):
        """ Add some experience

        :type theExp: int
        :param theExp: experience to be added
        """
        self.exp += theExp
        while self.exp >= EXP_NEXT_LEVEL:
            self.exp -= EXP_NEXT_LEVEL
            self.levelUp()

    #--------------------------------------------------------------------------
    def levelUp(self):
        """ Level up instance
        """
        self.level  += 1
        self.money  += 1
        self.shield += 1
        self.health += 1
        self.power  += 1
        self.axe    += 1
        self.bow    += 1
        self.dagger += 1
        self.lance  += 1
        self.staff  += 1
        self.sword  += 1

    #--------------------------------------------------------------------------
    def getStatValue(self, theStat, theKlass):
        """ Return value for the given stat

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        self.logger.debug("getStatValue for %s, %s" % (theStat, theKlass))
        statValue = getattr(self, theStat, None)
        if statValue is None:
            statValue = getattr(self, theKlass.lower(), None)
        return statValue


#
#------------------------------------------------------------------------------
if __name__ == '__main__':
    pass
