import cell


class Sword(cell.Cell):

    STRING = "sword"
    DAMAGE = 8

    def __init__(self, thePosition, **kwargs):
        """ Sword initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        super(Sword, self).__init__(thePosition, **kwargs)
