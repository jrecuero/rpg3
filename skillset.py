#!/usr/bin/env python

"""skillset.py class required for the skillset.

:author:    Jose Carlos Recuero
:version:   0.1
:since:     10/21/2014

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
# import skillset python modules
#
import objecto


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
class SkillSet(objecto.Objecto):
    """ Skill set are abilities that player can use in the action phase.
    """

    #--------------------------------------------------------------------------
    def __init__(self, thePlayer, theTableCell=None, theName=None):
        """ Initialize SkillSet instance

        :type thePlayer: player.Player
        :param thePlayer: Player instance that will use the skillset

        :type theTableCell: tablecell.TableCell
        :param theTableCell: table cell related with the skill set

        :type theName: str
        :param theName: SkillSet name
        """
        super(SkillSet, self).__init__(theName)
        self.player    = thePlayer
        self.tablecell = theTableCell

    #--------------------------------------------------------------------------
    def baseAttack(self):
        """ Skill Set basic and common attack.
        """
        userDamage = self.user.getDamage()
        cellDamage = self.tablecell.attrs.damage if self.tablecell else 0
        return userDamage + cellDamage

    #--------------------------------------------------------------------------
    def baseDefense(self):
        """ Skill Set basic and common defense.
        """
        userDefense = self.user.getDefense()
        cellDefense = self.tablecell.attrs.defense if self.tablecell else 0
        return userDefense + cellDefense

    #--------------------------------------------------------------------------
    def baseMoney(self):
        """ Skill Set basic and common money.
        """
        userMoney = self.user.getMoney()
        cellMoney = self.tablecell.attrs.money if self.tablecell else 0
        return userMoney + cellMoney

    #--------------------------------------------------------------------------
    def baseHealth(self):
        """ Skill Set basic and common health.
        """
        userHealth = self.user.getHealth()
        cellHealth = self.tablecell.attrs.health if self.tablecell else 0
        return userHealth + cellHealth

    #--------------------------------------------------------------------------
    def basePower(self):
        """ Skill Set basic and common power.
        """
        userPower = self.user.getPower()
        cellPower = self.tablecell.attrs.power if self.tablecell else 0
        return userPower + cellPower

    #--------------------------------------------------------------------------
    def baseMove(self):
        """ Skill Set basic and common move.
        """
        userMove = self.user.getMove()
        cellMove = self.tablecell.attrs.move if self.tablecell else 0
        return userMove + cellMove

    #--------------------------------------------------------------------------
    def getSkills(self):
        """ Return list with all available skills.

        :rtype: list
        :return: list with available skills
        """
        return []


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
    import doctest
    doctest.testmod()
