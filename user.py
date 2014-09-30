import loggerator
import stats


#
#------------------------------------------------------------------------------
class User (object):
    """
    """

    #--------------------------------------------------------------------------
    def __init__(self, theName):
        """ Initialize User instance

        :type theName: str
        :param theName: user name
        """
        self.name   = theName
        self.stats  = stats.Stats()
        self.logger = loggerator.getLoggerator('user')

    #--------------------------------------------------------------------------
    def getStatValue(self, theStat, theKlass):
        """ Return value for the given stat

        :type theStat: str
        :param theStat: stat to retrieve the value

        :type theKlass: object
        :param theKlass: instance with the cell stat
        """
        return self.stats.getStatValue(theStat, theKlass)

    #--------------------------------------------------------------------------
    def addExp(self, theExp):
        """ Add some experience

        :type theExp: int
        :param theExp: experience to be added
        """
        self.stats.addExp(theExp)


#
#------------------------------------------------------------------------------
if __name__ == '__main__':
    pass
