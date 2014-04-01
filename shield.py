import cell


class Shield(cell.Cell):

    def __init__(self, thePosition, theName, **kwargs):
        """ Shield initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type theName: str
        :param theName: Shield name

        :type kwargs: dict
        :param kwargs: Dictionary with Shield attributes.
        """
        super(Shield, self).__init__(thePosition, theName, **kwargs)

