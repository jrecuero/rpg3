import cell


class Bow(cell.Cell):

    STRING = "bow"
    DAMAGE = 5

    def __init__(self, thePosition, **kwargs):
        """ Bow initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Bow attributes.
        """
        super(Bow, self).__init__(thePosition, **kwargs)
