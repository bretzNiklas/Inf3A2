#https://stackoverflow.com/questions/4382945/abstract-methods-in-python
import abc

import icontract


class BorderBehavior:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    @icontract.require(lambda result: len(result) > 0)
    def get_submatrix_list(self, point, matrix, radius = 1):
        return

    @classmethod
    def check_if_oob(cls, point, matrix):
        if point[0] < 0 or point[1] < 0:
            return True

        if point[0] > len(matrix) - 1 or point[1] > len(matrix[0]) - 1:
            return True
        return False