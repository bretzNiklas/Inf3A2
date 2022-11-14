from BorderBehavior import BorderBehavior


class ZeroPaddingBorderBehavior(BorderBehavior):


    #the method gets a point as list, the image as a 2d list and the value a radius
    #it returns the values around the provided point as a list
    #if one of the values around the point is out of the bounds of the given matrix, its value is 0
    def get_submatrix_list(self, point, matrix, radius = 1):
        submatrix_as_list = []

        for j in range(point[0] - radius, point[0] + radius + 1):
            for i in range(point[1] - radius, point[1] + radius + 1):
                if ZeroPaddingBorderBehavior.check_if_oob([j, i], matrix):
                    submatrix_as_list.append(0)
                else:

                    submatrix_as_list.append(matrix[j][i])


        return submatrix_as_list


    @classmethod
    def check_if_oob(cls, point, matrix):
        return super().check_if_oob(point, matrix)
