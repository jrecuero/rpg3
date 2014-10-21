#!/usr/bin/env python

"""tablecell.py class required tableboard tablecell.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     10/01/2014

"""

__docformat__ = 'restructuredtext en'

###############################################################################
##  _                            _
## (_)_ __ ___  _ __   ___  _ __| |_ ___
## | | '_ ` _ \| '_ \ / _ \| '__| __/ __|
## | | | | | | | |_) | (_) | |  | |_\__ \
## |_|_| |_| |_| .__/ \___/|_|   \__|___/
##             |_|
###############################################################################
#
# import std python modules
#

#
# import user python modules
#
import attrs
import cell


###############################################################################
##
##   ___ ___  _ __  ___| |_ __ _ _ __ | |_ ___
##  / __/ _ \| '_ \/ __| __/ _` | '_ \| __/ __|
## | (_| (_) | | | \__ \ || (_| | | | | |_\__ \
##  \___\___/|_| |_|___/\__\__,_|_| |_|\__|___/
##
###############################################################################
#


###############################################################################
##            _                     _   _
##  ___ _   _| |__  _ __ ___  _   _| |_(_)_ __   ___  ___
## / __| | | | '_ \| '__/ _ \| | | | __| | '_ \ / _ \/ __|
## \__ \ |_| | |_) | | | (_) | |_| | |_| | | | |  __/\__ \
## |___/\__,_|_.__/|_|  \___/ \__,_|\__|_|_| |_|\___||___/
##
###############################################################################
#


###############################################################################
##       _                     _       __ _       _ _   _
##   ___| | __ _ ___ ___    __| | ___ / _(_)_ __ (_) |_(_) ___  _ __  ___
##  / __| |/ _` / __/ __|  / _` |/ _ \ |_| | '_ \| | __| |/ _ \| '_ \/ __|
## | (__| | (_| \__ \__ \ | (_| |  __/  _| | | | | | |_| | (_) | | | \__ \
##  \___|_|\__,_|___/___/  \__,_|\___|_| |_|_| |_|_|\__|_|\___/|_| |_|___/
##
###############################################################################
#

#
#------------------------------------------------------------------------------
class TableCell(cell.Cell):
    """
    """

    tracerList     = []
    customAttrsCbs = {}

    #--------------------------------------------------------------------------
    @staticmethod
    def getTableCellAttrs():
        """
        """
        return ('damage', 'defense', 'money', 'health', 'power')

    #--------------------------------------------------------------------------
    @staticmethod
    def createAttrsDict():
        """
        """
        dicta = {}
        for attr in TableCell.getTableCellAttrs():
            dicta[attr] = 0
        return dicta

    #--------------------------------------------------------------------------
    @staticmethod
    def addTraceMatch(theCell, theAttr, theMatchLen, theValue, theTotalValue, theLog=True):
        """ Add a new match to the tracer list.

            :type theCell: object
            :param theCell: cell instance inside the match

            :type theAttr: str
            :parama theAttr: cell attribute used

            :type theMatchLen: int
            :param theMatchLen: length of the match

            :type theValue: int
            :param theValue: value of the match per cell

            :type theTotalValue: int
            :param theTotalValue: total value of the match

            :type theLog: bool
            :param theLog: send the trace to the display log
        """
        TableCell.tracerList.append({'cell':  theCell.getClass(),
                                     'attr':  theAttr,
                                     'len':   theMatchLen,
                                     'val':   theValue,
                                     'total': theTotalValue})
        if theLog:
            theCell.logger.debug('Match %d %s, %s %s each, total %s' %
                                 (theMatchLen, theCell.getClass(), theValue, theAttr, theTotalValue))

    #--------------------------------------------------------------------------
    def __init__(self, thePosition, **kwargs):
        """ TableCell initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Sword name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        super(TableCell, self).__init__(thePosition, **kwargs)
        self.attrsUsed = ()
        self.createAttrs()
        self.attrs = attrs.Attrs()

    #--------------------------------------------------------------------------
    def createAttrs(self):
        """
        """
        self.data    = getattr(self, 'STRING', 'TABLECELL')
        self.damage  = getattr(self, 'damage', 0)
        self.defense = getattr(self, 'defense', 0)
        self.money   = getattr(self, 'money', 0)
        self.health  = getattr(self, 'health', 0)
        self.power   = getattr(self, 'power', 0)

        self.attrsCbs = {}
        for attr in attrs.Attrs.getAttrs():
            self.attrsCbs[attr] = {3: self.baseMatch3, 4: self.baseMatch4, 5: self.baseMatch5}
        self.attrsCbs.update(self.customAttrsCbs)

    #--------------------------------------------------------------------------
    def _getTotalAttrValue(self, theAttr, theUser=None, theMatchNumber=0):
        """ Get total value to add for a Attr

        Calculate the total value based on the cell and the user value for
        that particular cell.

        It updates the counter for the cell type for the user.

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :type theMatchNumber: int
        :param theMatchNumber: number of cells being matched

        :rtype: list
        :return: Total value accumulate to the given sta
        """
        cellValue = getattr(self, theAttr, 0)
        userValue = 0
        if theUser:
            userValue = theUser.getStatValue(self.getClass())
        return cellValue + userValue

    #--------------------------------------------------------------------------
    def baseMatch3(self, theMatch, theAttr, theUser=None):
        """ Basic match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value      = self._getTotalAttrValue(theAttr, theUser, len(theMatch))
        totalValue = value * len(theMatch)
        #self.logger.debug('Match %d %s, %s %s each, total %s' %
        #                  (len(theMatch), self.getClass(), value, theAttr, value * len(theMatch)))
        TableCell.addTraceMatch(self, theAttr, len(theMatch), value, totalValue)
        return totalValue

    #--------------------------------------------------------------------------
    def baseMatch4(self, theMatch, theAttr, theUser=None):
        """ Critical match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value      = self._getTotalAttrValue(theAttr, theUser, len(theMatch)) * 2
        totalValue = value * len(theMatch)
        #self.logger.debug('Match %d %s, %s %s each, total %s' %
        #self.logger.debug('Match %d %s, %s %s each, total %s' %
        #                  (len(theMatch), self.getClass(), value, theAttr, value * len(theMatch)))
        TableCell.addTraceMatch(self, theAttr, len(theMatch), value, totalValue)
        return totalValue

    #--------------------------------------------------------------------------
    def baseMatch5(self, theMatch, theAttr, theUser=None):
        """ Critical match accumulation method for any Attr

        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the Attr name

        :type theUser: User
        :param theUser: user instance

        :rtype: list
        :return: Total value accumulate to the given Attr and counter
        """
        value      = self._getTotalAttrValue(theAttr, theUser, len(theMatch)) * 3
        totalValue = value * len(theMatch)
        #self.logger.debug('Match %d %s, %s %s each, total %s' %
        #self.logger.debug('Match %d %s, %s %s each, total %s' %
        #                  (len(theMatch), self.getClass(), value, theAttr, value * len(theMatch)))
        TableCell.addTraceMatch(self, theAttr, len(theMatch), value, totalValue)
        return totalValue

    #--------------------------------------------------------------------------
    def executeMatch(self, theMatch, theUser=None):
        """ Execute the given match for the given cell.
        :type theMatch: list
        :param theMatch: List with position matching

        :type theUser: User
        :param theUser: user instance

        :rtype: dict
        :return: dictionary with cell attributes being updated
        """
        reto_dict = {}
        for attr in self.attrsUsed:
            reto_dict[attr] = self._matchCb(theMatch, attr, theUser)
        return reto_dict

    #--------------------------------------------------------------------------
    def _matchCb(self, theMatch, theAttr, theUser=None):
        """
        :type theMatch: list
        :param theMatch: List with position matching

        :type theAttr: str
        :param theAttr: String with the attr name

        :type theUser: User
        :param theUser: user instance
        """
        matchCb = self.attrsCbs[theAttr].get(len(theMatch), None)
        if matchCb:
            return matchCb(theMatch, theAttr, theUser)
        return 0

    #--------------------------------------------------------------------------
    def getDamage(self):
        """
        """
        return self.damage

    #--------------------------------------------------------------------------
    def setDamage(self, theDamage):
        """
        """
        self.damage = theDamage
        return True

    #--------------------------------------------------------------------------
    def getDefense(self):
        """
        """
        return self.defense

    #--------------------------------------------------------------------------
    def setDefense(self, theDefense):
        """
        """
        self.defense = theDefense
        return True

    #--------------------------------------------------------------------------
    def getMoney(self):
        """
        """
        return self.money

    #--------------------------------------------------------------------------
    def setMoney(self, theMoney):
        """
        """
        self.money = theMoney
        return True

    #--------------------------------------------------------------------------
    def getHealth(self):
        """
        """
        return self.health

    #--------------------------------------------------------------------------
    def setHealth(self, theHealth):
        """
        """
        self.health = theHealth
        return True

    #--------------------------------------------------------------------------
    def getPower(self):
        """
        """
        return self.power

    #--------------------------------------------------------------------------
    def setPower(self, thePower):
        """
        """
        self.power = thePower
        return True


###############################################################################
##                  _
##  _ __ ___   __ _(_)_ __
## | '_ ` _ \ / _` | | '_ \
## | | | | | | (_| | | | | |
## |_| |_| |_|\__,_|_|_| |_|
##
###############################################################################
#
if __name__ == '__main__':
#    import unittest
#    import test.test_tablecell as testTableCell
#    runner = unittest.TextTestRunner(verbosity=2)
#    runner.run(testTableCell.TableCellTestSuite())
    import doctest
    doctest.testmod()
