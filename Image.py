from KernelFactory import KernelFactory


class Image:

    def __init__(self):
        self.pixels = [[]]

    def set_pixels(self, pixels):
        self.pixels = pixels

    def readFromFile(self, filename):
        file = open(filename, "r")
        content = file.readlines()
        content = remove_comments(content)
        lines = trim_lines(content)

        if not check_for_magic_number(lines):
            print("magic number missing")

        w_and_h = extract_width_and_height(lines[1])

        self.pixels = [[0 for x in range(w_and_h[0])] for y in range(w_and_h[1])]
        # from https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array

        k = 2

        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                self.pixels[i][j] = lines[k]
                k = k + 1


        return self.pixels

    def writeToFile(self, filename):

        file = open(filename, "w")


        file.writelines(["P2\n", f"{len(self.pixels[0])} {len(self.pixels)}\n", "255\n"])

        for l in self.pixels:
            for p in l:
                file.write(str(p))
                file.write("\n")


    def convolve(self):#, kernel, border_behavior):


        filtered_pixels = [[0 for x in range(len(self.pixels[0]))] for y in range(len(self.pixels))]


        kernel = KernelFactory().createBoxFilter(5)

        for width, rows in enumerate(self.pixels):
            for height, p in enumerate(rows):
                filtered_pixels[width][height] = kernel.get_pixel_value(height, width, self.pixels)


        test = Image()
        test.set_pixels(filtered_pixels)
        test.writeToFile("convolveImage.pgm")

        pass


def remove_comments(content):
    for e in content:
        if e.startswith("#"):
            content.remove(e)
    return content


def trim_lines(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].removesuffix('\n')
    return lines


def check_for_magic_number(lines):
    if lines[0] == "P2":
        return True
    return False


def extract_width_and_height(string):
    temp = string.split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    return temp
