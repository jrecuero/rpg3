import cell


class Shield(cell.Cell):

    STRING = "shield"

    def __init__(self, thePosition, **kwargs):
        """ Shield initialization method.

        :type thePosition: tuple
        :param thePosition: Tuple with x and y coordinates.

        :type kwargs: dict
        :param kwargs: Dictionary with Shield attributes.
        """
        super(Shield, self).__init__(thePosition, **kwargs)
