


m = [[3, 9, 3, 4],
    [4, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 7],
    [1, 2, 6, 4],]


def get_submatrix(matrix, point, radius=1):


    submatrix_as_list = []

    for j in range(point[0] - radius, point[0] + radius + 1):
        for i in range(point[1] - radius, point[1] + radius + 1):
            if check_if_oob([j, i], matrix):


                #oob oben links
                if j == -1 and i == -1:
                    submatrix_as_list.append(matrix[j+1][i+1])
                    print(f" {matrix[j+1][i+1]}", end="")
                #oob unten rechts
                elif j == len(matrix) and i == len(matrix[0]) :
                    submatrix_as_list.append(matrix[j-1][i-1])
                    print(f" {matrix[j-1][i-1]}", end="")

                #oob unten links
                elif j == len(matrix) and i == -1:
                    submatrix_as_list.append(matrix[j-1][i+1])
                    print(f" {matrix[j - 1][i + 1]}", end="")

                #oob oben rechts
                elif j == -1 and i == len(matrix[0]):
                    submatrix_as_list.append(matrix[j+1][i-1])
                    print(f" {matrix[j + 1][i - 1]}", end="")

                #oob links
                elif i == -1 and not j == -1:
                    submatrix_as_list.append(matrix[j][i + 1])
                    print(f" {matrix[j][i + 1]}", end="")

                #oob oben
                elif j == -1 and not i == -1:
                    submatrix_as_list.append(matrix[j + 1][i])
                    print(f" {matrix[j +1][i ]}", end="")

                elif i == len(matrix[0]) and not j == len(matrix):
                    submatrix_as_list.append(matrix[j][i - 1])
                    print(f" {matrix[j][i - 1]}", end="")

                elif j == len(matrix) and not i == len(matrix[0]):
                    submatrix_as_list.append(matrix[j - 1][i])
                    print(f" {matrix[j - 1][i]}", end="")


                #else:
                 #   submatrix_as_list.append(0)
                 #   print()
                  #  print(f"j ist {j}, i ist{i}", end="")
                  #  print()


            else:
                print(f" {matrix[j][i]}", end="")
                submatrix_as_list.append(matrix[j][i])
        print()

    return submatrix_as_list

def check_if_oob(point, matrix):
    if point[0] < 0 or point[1] < 0:
        return True

    if point[0] > len(matrix) - 1 or point[1] > len(matrix[0]) - 1:
        return True
    return False


sm = get_submatrix(m, [0, 3])

k = 0

