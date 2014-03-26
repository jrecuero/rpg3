import cell


class Sword(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Sword initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Sword name

        :type kwargs: dict
        :param kwargs: Dictionary with sword attributes.
        """
        super(Sword, self).__init__(thePosition, theName, **kwargs)
