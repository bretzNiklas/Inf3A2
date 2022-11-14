import icontract

from BorderBehavior import BorderBehavior


class ClampingPaddingBorderBehavior(BorderBehavior):

    @icontract.ensure(lambda radius: radius > 0, "radius must be 1 or more")
    def get_submatrix_list(self, point, matrix, radius = 1):
        submatrix_as_list = []

        for j in range(point[0] - radius, point[0] + radius + 1):
            for i in range(point[1] - radius, point[1] + radius + 1):
                if ClampingPaddingBorderBehavior.check_if_oob([j, i], matrix):
                    # oob oben links
                    if j == -1 and i == -1:
                        submatrix_as_list.append(matrix[j + 1][i + 1])
                        #print(f" {matrix[j + 1][i + 1]}", end="")
                    # oob unten rechts
                    elif j == len(matrix) and i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j - 1][i - 1])
                        #print(f" {matrix[j - 1][i - 1]}", end="")

                    # oob unten links
                    elif j == len(matrix) and i == -1:
                        submatrix_as_list.append(matrix[j - 1][i + 1])
                        #print(f" {matrix[j - 1][i + 1]}", end="")

                    # oob oben rechts
                    elif j == -1 and i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j + 1][i - 1])
                        #print(f" {matrix[j + 1][i - 1]}", end="")

                    # oob links
                    elif i == -1 and not j == -1:
                        submatrix_as_list.append(matrix[j][i + 1])
                        #print(f" {matrix[j][i + 1]}", end="")

                    # oob oben
                    elif j == -1 and not i == -1:
                        submatrix_as_list.append(matrix[j + 1][i])
                        #print(f" {matrix[j + 1][i]}", end="")

                    elif i == len(matrix[0]) and not j == len(matrix):
                        submatrix_as_list.append(matrix[j][i - 1])
                        #print(f" {matrix[j][i - 1]}", end="")

                    elif j == len(matrix) and not i == len(matrix[0]):
                        submatrix_as_list.append(matrix[j - 1][i])
                        #print(f" {matrix[j - 1][i]}", end="")

                else:
                    submatrix_as_list.append(matrix[j][i])

        return submatrix_as_list


    @classmethod
    def check_if_oob(cls, point, matrix):
        return super().check_if_oob(point, matrix)