import cell


class Lance(cell.Cell):

    STRING = "lance"
    DAMAGE = 6

    def __init__(self, thePosition, **kwargs):
        """ Lance initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Lance attributes.
        """
        super(Lance, self).__init__(thePosition, **kwargs)
