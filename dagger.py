import cell


class Dagger(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Dagger initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Dagger name

        :type kwargs: dict
        :param kwargs: Dictionary with Dagger attributes.
        """
        super(Dagger, self).__init__(thePosition, theName, **kwargs)

