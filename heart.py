import cell


class Heart(cell.Cell):

    STRING = "heart"
    HEALTH = 50

    def __init__(self, thePosition, **kwargs):
        """ Heart initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Heart attributes.
        """
        super(Heart, self).__init__(thePosition, **kwargs)
