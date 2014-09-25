import cell


class Axe(cell.Cell):

    STRING = "axe"
    DAMAGE = 10

    def __init__(self, thePosition, **kwargs):
        """ Axe initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Axe attributes.
        """
        super(Axe, self).__init__(thePosition, **kwargs)
