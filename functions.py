from PIL import Image
import numpy as np


class ImageText:
    def __init__(self, width, height):#
        self.width = width
        self.height = height
        chars = ""
        for x in range(width):
            for y in range(height):
                chars += "."
            if x < width - 1:
                chars += "\n"
        self.text = chars


    density_characters = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    density_symbols = " .:-_^;+=!*?#$%&@"
    borders = ["-|_|", "─│─│", "═║═║"]
    edges = ["/\\/\\", "┌└┘┐", "╔╚╝╗"]
    crossings = ["T>I<+", "┬├┴┤┼", "╦╠╩╣╬"]

    def get_dimensions(self):
        return self.width, self.height

    def setText(self, data):
        chars = ""
        for x in range(self.width):
            for y in range(self.height):
                #chars += data[x][y].__str__()
                chars += "."
            if x < self.width - 1:
                chars += "\n"
        self.text = chars

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def showText(self):
        print(self.text)

    def modify_Text_by_pixelFunction(self, fucName, *args):
        chars = ""
        for x in range(self.width):
            for y in range(self.height):
                asArray = " ".join(self.data[x][y].__str__().split())
                asArray = asArray.replace(" ", ",").replace("[,", "[")
                chars += self.evaluatePixelFunction(fucName, asArray)
            if x < self.width - 1:
                chars += "\n"
        self.text = chars

    def add_Border(self, type):
        match type:
            case 1:
                print(self.borders[0])
            case 2:
                print(self.borders[1])
            case 3:
                print(self.borders[2])

    def pixel_average_brightness_mapping(self, pixel):
        pixNum = int((pixel[0] + pixel[1] + pixel[2]) // 3)
        pixChar = int(np.interp(pixNum, [0, 255], [0, 16]))
        return self.density_symbols.__getitem__(pixChar).__str__()

    def evaluatePixelFunction(self, fucName, *args):
        out = "self." + fucName + "("
        for i in range(args.__len__()):
            out += args[i].__str__()
            if i < args.__len__() - 1:
                out += ", "
        out += ")"
        #print(out)
        return eval(out)

    def save_to_file(self, filename="ascii_output.txt"):
        """Saves ASCII output to a text file."""
        with open(filename, "w") as file:
            file.write(self.getData())