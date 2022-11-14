from BorderBehavior import BorderBehavior


class ZeroPaddingBorderBehavior(BorderBehavior):

    def get_submatrix_list(self, point, matrix, radius = 1):

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


    @classmethod
    def check_if_oob(cls, point, matrix):
        return super().check_if_oob(point, matrix)
