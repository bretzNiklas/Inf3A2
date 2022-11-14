import icontract

from BorderBehavior import BorderBehavior


class ClampingPaddingBorderBehavior(BorderBehavior):


    #the method gets a point as list, the image as a 2d list and the value a radius
    #it returns the values around the provided point as a list
    # if one of the values around the point is out of the bounds of the given matrix, its value is the value of the nearest pixel thats not out of bounds
    @icontract.ensure(lambda radius: radius > 0, "radius must be 1 or more")
    def get_submatrix_list(self, point, matrix, radius = 1):
        submatrix_as_list = []

        for j in range(point[0] - radius, point[0] + radius + 1):
            for i in range(point[1] - radius, point[1] + radius + 1):
                if ClampingPaddingBorderBehavior.check_if_oob([j, i], matrix):
                    # oob top left
                    if j == -1 and i == -1:
                        submatrix_as_list.append(matrix[j + 1][i + 1])
                    # oob bottom right
                    elif j == len(matrix) and i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j - 1][i - 1])


                    # oob bottom left
                    elif j == len(matrix) and i == -1:
                        submatrix_as_list.append(matrix[j - 1][i + 1])


                    # oob top right
                    elif j == -1 and i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j + 1][i - 1])


                    # oob left
                    elif i == -1 and not j == -1:
                        submatrix_as_list.append(matrix[j][i + 1])


                    # oob top
                    elif j == -1 and not i == -1:
                        submatrix_as_list.append(matrix[j + 1][i])


                    # oob right
                    elif i == len(matrix[0]) and not j == len(matrix):
                        submatrix_as_list.append(matrix[j][i - 1])


                    # oob bottom
                    elif j == len(matrix) and not i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j - 1][i])


                else:
                    submatrix_as_list.append(matrix[j][i])

        return submatrix_as_list


    @classmethod
    def check_if_oob(cls, point, matrix):
        return super().check_if_oob(point, matrix)