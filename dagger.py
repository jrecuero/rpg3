import cell


class Dagger(cell.Cell):

    STRING = "dagger"
    DAMAGE = 3

    def __init__(self, thePosition, **kwargs):
        """ Dagger initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Dagger attributes.
        """
        super(Dagger, self).__init__(thePosition, **kwargs)
