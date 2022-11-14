import icontract

#class returns kernel matrices list
class KernelFactory:

    @staticmethod
    def createVerticalPrewittKernel():
        return [-1, -1, -1, 0, 0, 0, 1, 1, 1]


    @staticmethod
    def createHorizontalPrewittKernel():
        return [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    @staticmethod
    @icontract.require(lambda radius: isinstance(radius, int) is True, f"wrong datatype for radius provided")
    def createBoxFilter(radius):
        dimension = ((2 * radius) + 1) ** 2

        print(radius, dimension)

        return [1 / dimension for _ in range(dimension)]
