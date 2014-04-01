import cell


class Axe(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Axe initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Axe name

        :type kwargs: dict
        :param kwargs: Dictionary with Axe attributes.
        """
        super(Axe, self).__init__(thePosition, theName, **kwargs)
