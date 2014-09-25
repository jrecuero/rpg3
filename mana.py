import cell


class Mana(cell.Cell):

    STRING = "mana"
    POWER  = 20

    def __init__(self, thePosition, **kwargs):
        """ Mana initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with mana attributes.
        """
        super(Mana, self).__init__(thePosition, **kwargs)
