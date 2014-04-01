import cell


class Mana(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Mana initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Mana name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        super(Mana, self).__init__(thePosition, theName, **kwargs)

