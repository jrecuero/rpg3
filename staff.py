import cell


class Staff(cell.Cell):

    STRING = "staff"

    def __init__(self, thePosition, **kwargs):
        """ Staff initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Staff attributes.
        """
        super(Staff, self).__init__(thePosition, **kwargs)
