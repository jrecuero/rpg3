import cell


class Coin(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Coin initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Coin name

        :type kwargs: dict
        :param kwargs: Dictionary with Coin attributes.
        """
        super(Coin, self).__init__(thePosition, theName, **kwargs)

