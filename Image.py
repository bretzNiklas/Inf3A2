
class Image:

    def __init__(self):
        self.pixels = [[]]

    def readFromFile(self, filename):
        file = open(filename, "r")
        content = file.readlines()
        content = remove_comments(content)
        lines = trim_lines(content)

        if not check_for_magic_number(lines):
            print("magic number missing")

        w_and_h = extract_width_and_height(lines[1])

        self.pixels = [[lines[x] for x in range(3, len(lines))] for y in range(w_and_h[1])]

        for p in self.pixels:
            for t in p:
                if t == 255:
                    print()


        print(self.pixels)

        return self.pixels

    def writeToFile(self, filename):

        file = open(filename, "w")

        #print(len(self.pixels[0]))


        file.writelines(["P2\n", f"{len(self.pixels)} {len(self.pixels[0])}\n", "255\n"])

        for l in self.pixels:
            #print(l)
            for p in l:
                #print(p)
                file.write(p)
                file.write("\n")





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
