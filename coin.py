import cell


class Coin(cell.Cell):

    STRING = "coin"

    def __init__(self, thePosition, **kwargs):
        """ Coin initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Coin attributes.
        """
        super(Coin, self).__init__(thePosition, **kwargs)
