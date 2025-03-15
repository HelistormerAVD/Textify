from PIL import Image
import numpy as np


class ImageText:
    def __init__(self, width, height):#
        self.width = width
        self.height = height
        textArray = [[0 for x in range(width)] for x in range(height)]
        chars = ""
        for x in range(width):
            for y in range(height):
                chars += "."
                textArray[x][y] = "."
            if x < width - 1:
                chars += "\n"
        self.text = chars


    #density_characters = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    density_symbols = " .:-_^;+=!*?#$%&@"
    borders_0 = "-|_|"
    borders_1 = "─│─│"
    borders_2 = "═║═║"
    edges_0 = "/\\/\\"
    edges_1 = "┌└┘┐"
    edges_2 = "╔╚╝╗"
    crossings_0 = "T>I<+"
    crossings_1 = "┬├┴┤┼"
    crossings_2 = "╦╠╩╣╬"

    def get_dimensions(self):
        return self.width, self.height

    def setText(self, data):
        chars = ""
        for x in range(data.__len__()):
            for y in range(data[x].__len__()):
                #chars += data[x][y].__str__()
                chars += "."
            if x < data[x].__len__() - 1:
                chars += "\n"
        self.text = chars

    def setData(self, data):
        chars = ""
        for x in range(data.__len__()):
            for y in range(data[x].__len__()):
                chars += data[x][y].__str__()
            if x < data[x].__len__() - 1:
                chars += "\n"
        self.data = chars

    def getData(self):
        return self.data

    def showText(self):
        print(self.text)

    def modify_Text_by_pixelFunction(self, fucName, *args):
        chars = ""
        for x in range(self.width):
            for y in range(self.height):
                chars += self.evaluatePixelFunction(fucName, *args)
            if x < self.width - 1:
                chars += "\n"
        self.data = chars

    def add_Border(self, type):
        match type:
            case 1:
                print(self.borders_0)
            case 2:
                print(self.borders_1)
            case 3:
                print(self.borders_2)

    def pixel_average_brightness_mapping(self, pixel):
        pixNum = (pixel[0] + pixel[1] + pixel[2]) // 3
        pixChar = np.interp(pixNum, [0, 255], [0, 16])
        return self.density_symbols.__getitem__(pixChar).__str__()

    def evaluatePixelFunction(self, fucName, *args):
        out = "self." + fucName + "("
        for i in range(args.__len__()):
            out += args[i].__str__()
            if i < args.__len__():
                out += ", "
        out += ")"
        return eval(out)