from BorderBehavior import BorderBehavior


class ZeroPaddingBorderBehavior(BorderBehavior):

    def getPixelValue(self, point, matrix):
        radius = 1

        #print(matrix[point[0]][point[1]])

        submatrix_as_list = []

        for j in range(point[0] - radius, point[0] + radius + 1):
            for i in range(point[1] - radius, point[1] + radius + 1):
                if ZeroPaddingBorderBehavior.check_if_oob([j, i], matrix):
                    submatrix_as_list.append(0)
                    #print(" 0", end="")
                else:
                    #print(f" {matrix[j][i]}", end="")
                    submatrix_as_list.append(matrix[j][i])
            #print()

        return submatrix_as_list


    @staticmethod
    def check_if_oob(point, matrix):
        if point[0] < 0 or point[1] < 0:
            return True

        if point[0] > len(matrix) - 1 or point[1] > len(matrix[0]) - 1:
            return True
        return False