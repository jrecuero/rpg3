import cell


class Staff(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Staff initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Staff name

        :type kwargs: dict
        :param kwargs: Dictionary with Staff attributes.
        """
        super(Staff, self).__init__(thePosition, theName, **kwargs)

