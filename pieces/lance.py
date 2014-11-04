#!/usr/bin/env python

"""lance.py class required for the lance tablecell.

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
import tablecell
import skillset


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
class Lance(tablecell.TableCell):
    """
    """

    def __init__(self, thePosition, **kwargs):
        """ Lance initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Lance attributes.
        """
        self.damage     = 6
        super(Lance, self).__init__(thePosition,
                                    theName=self.getClass(),
                                    theSpriteName='lance',
                                    **kwargs)
        self.attrsUsed = ('damage', )


#
#------------------------------------------------------------------------------
class LanceSkillSet(skillset.SkillSet):
    """ Lance skill set available to be used by any player.
    """

    #--------------------------------------------------------------------------
    def __init__(self, thePlayer):
        """ Initialize LanceSkillSet instance.

        :type thePlayer: player.Player
        :param thePlayer: Player instance that will use the skillset
        """
        super(LanceSkillSet, self).__init__(thePlayer, Lance(), 'Lance Skill Set')

    #--------------------------------------------------------------------------
    def getSkills(self):
        """ Return list with all available skills.

        :rtype: list
        :return: list with available skills
        """
        return (self.baseAttack, )


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
