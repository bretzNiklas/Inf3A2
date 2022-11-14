class Kernel:

    def __init__(self, filter_list, radius = 1):
        self.radius = radius
        self.filter_list = filter_list
        pass


    #method gets the point for which to compute the filtered value, the image as 2d array and a border_behavior object
    #the border_behavior.get_submatrix_list method returns the submatrix of the values around the given point as list
    #the returned list is multiplied entry by entry with the given filter_list
    #the result of this multiplication is the value of the given point with the filter applied
    def get_pixel_value(self, height, width, matrix, border_behavior):
        sub_matrix = border_behavior.get_submatrix_list([height, width], matrix)
        result = 0

        for a, b in zip(self.filter_list, sub_matrix):
            if type(b) == type("string"):
                b = int(b)
            result = result + (a * b)

        return result
