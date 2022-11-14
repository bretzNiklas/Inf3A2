class Kernel:

    def __init__(self, filter_list, radius = 1):
        self.radius = radius
        self.filter_list = filter_list
        pass


    def get_pixel_value(self, w, h, pixel_matrix, border_behavior):
        radius = 1

        t = border_behavior.getPixelValue([h, w], pixel_matrix)
        #t = get_submatrix(pixel_matrix, [h, w], radius)

        erg = 0

        for a, b in zip(self.filter_list, t):

            if type(b) == type("hallo"):
                b = int(b)

            erg = erg + (a * b)

        return erg


        #return pixel_value_logic(w, h, pixel_matrix, self.filter_list)

'''def pixel_value_logic(w, h, pixel_matrix, filter_list):

    radius = 1

    t = get_submatrix(pixel_matrix, [h, w], radius)

    erg = 0

    for a, b in zip(filter_list, t):

        if type(b) == type("hallo"):
            b = int(b)

        erg = erg + (a*b)

    return erg'''


def get_submatrix(matrix, point, radius=1):
    print(matrix[point[0]][point[1]])

    submatrix_as_list = []

    for j in range(point[0] - radius, point[0] + radius + 1):
        for i in range(point[1] - radius, point[1] + radius + 1):
            if check_if_oob([j, i], matrix):
                submatrix_as_list.append(0)
                print(" 0", end="")
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

