import cell


class Bow(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Bow initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Bow name

        :type kwargs: dict
        :param kwargs: Dictionary with Bow attributes.
        """
        super(Bow, self).__init__(thePosition, theName, **kwargs)

