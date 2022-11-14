import icontract

@icontract.invariant(lambda self: self.magic_number_is_correct is True)
class Image:

    PGM_PIXEL_OFFSET = 2
    PGM_FILE_EXTENSION = ".pgm"

    def __init__(self):
        self.magic_number_is_correct = True
        self.pixels = [[]]

    @icontract.require(lambda pixels: len(pixels) >= 4)
    def set_pixels(self, pixels):
        self.pixels = pixels

    @icontract.require(lambda filename: filename.endswith(Image.PGM_FILE_EXTENSION), "provided filename should be in .pgm format")
    def readFromFile(self, filename):
        file = open(filename, "r")
        content = file.readlines()
        content = Image.remove_comments(content)
        lines = Image.trim_lines(content)

        self.magic_number_is_correct = Image.check_for_magic_number(lines)

        w_and_h = Image.extract_width_and_height(lines[1])

        self.pixels = [[0 for x in range(w_and_h[0])] for y in range(w_and_h[1])]
        #initalizing this way is from https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array

        k = Image.PGM_PIXEL_OFFSET

        for i in range(len(self.pixels)):
            for j in range(len(self.pixels[0])):
                self.pixels[i][j] = lines[k]
                k = k + 1


        return self.pixels

    @icontract.require(lambda filename: filename.endswith(Image.PGM_FILE_EXTENSION), "filename should end with .pgm")
    def write_to_file(self, filename):

        file = open(filename, "w")


        file.writelines(["P2\n", f"{len(self.pixels[0])} {len(self.pixels)}\n", "255\n"])

        for l in self.pixels:
            for p in l:
                file.write(str(p))
                file.write("\n")

    #initializes a new 2d matrix in which the filtered image gets stored
    #after this the method gets the pixel values by using the kernel method get_pixel_value
    @icontract.require(lambda output_filename: output_filename.endswith(Image.PGM_FILE_EXTENSION), "desired filename should end with .pgm")
    def convolve(self, kernel, border_behavior, output_filename):

        filtered_pixels = [[0 for x in range(len(self.pixels[0]))] for y in range(len(self.pixels))]


        for height, rows in enumerate(self.pixels):
            for width, p in enumerate(rows):
                temp = int(kernel.get_pixel_value(height, width, self.pixels, border_behavior))
                filtered_pixels[height][width] = Image.get_value_in_range(temp)



        test = Image()
        test.set_pixels(filtered_pixels)
        test.write_to_file(output_filename)


    @staticmethod
    def remove_comments(content):
        for e in content:
            if e.startswith("#"):
                content.remove(e)
        return content


    @staticmethod
    def trim_lines(lines):
        for i in range(len(lines)):
            lines[i] = lines[i].removesuffix('\n')
        return lines

    @staticmethod
    def check_for_magic_number(lines):
        if lines[0] == "P2":
            return True
        return False

    @staticmethod
    def extract_width_and_height(string):
        temp = string.split()
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        return temp

    @staticmethod
    def get_value_in_range(value):
        if value < 0:
            return 0
        if value > 255:
            return 255
        return value

'''        for width, rows in enumerate(self.pixels):
            for height, p in enumerate(rows):
                temp = int(kernel.get_pixel_value(height, width, self.pixels, border_behavior))
                filtered_pixels[width][height] = Image.get_value_in_range(temp)'''