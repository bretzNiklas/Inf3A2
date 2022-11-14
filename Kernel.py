class Kernel:

    def __init__(self, filter_list, radius = 1):
        self.radius = radius
        self.filter_list = filter_list
        pass


    def get_pixel_value(self, w, h, pixel_matrix, border_behavior):
        radius = 1

        t = border_behavior.get_submatrix_list([h, w], pixel_matrix)


        erg = 0

        for a, b in zip(self.filter_list, t):
            if type(b) == type("string"):
                b = int(b)
            erg = erg + (a * b)

        return erg
