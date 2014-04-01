import cell


class Heart(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Heart initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Heart name

        :type kwargs: dict
        :param kwargs: Dictionary with Heart attributes.
        """
        super(Heart, self).__init__(thePosition, theName, **kwargs)

