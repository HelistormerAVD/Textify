import ast

from PIL import Image
import numpy as np


class ImageText:
    ESC = "["

    def __init__(self, width, height):#
        self.colorMap = None
        self.width = width
        self.height = height
        chars = ""
        backedChars = ""
        tempData = None
        for x in range(width):
            for y in range(height):
                chars += "."
            if x < width - 1:
                chars += "\n"
        self.text = chars
        self.backedImage = ""


    density_characters = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
    density_symbols = " .:-_^;+=!*?#$%&@"
    borders = ["-|_|", "─│─│", "═║═║"]
    edges = ["/\\/\\", "┌└┘┐", "╔╚╝╗"]
    crossings = ["T>I<+", "┬├┴┤┼", "╦╠╩╣╬"]

    cmd_colors = [(12, 12, 12),(197, 15, 31), (19, 161, 14),
                  (193, 156, 0), (0, 55, 218), (136, 23, 152),
                  (58, 150, 221), (204, 204, 204), (118, 118, 118),
                  (231, 72, 86), (22, 198, 12), (249, 241, 165),
                  (58, 120, 255), (180, 0, 158), (97, 214, 214), (242, 242, 242)]

    cmd_color_codes_foreground = ("[30m", "[31m", "[32m", "[33m", "[34m", "[35m", "[36m", "[37m",
                                  "[90m", "[91m", "[92m", "[93m", "[94m", "[95m", "[96m", "[97m")
    cmd_color_codes_background = ("[40m", "[41m", "[42m", "[43m", "[44m", "[45m", "[46m", "[47m",
                                  "[100m", "[101m", "[102m", "[103m", "[104m", "[105m", "[106m", "[107m")
    cmd_color_code_modifier = ("[0m", "[1m", "[4m", "[7m")
    color_rst = "[0m"

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

    def setTempData(self, data):
        self.tempData = data

    def setColorMap(self, data):
        self.colorMap = data

    def getData(self):
        return self.data

    def getTempData(self):
        return self.tempData

    def getColorMap(self):
        return self.colorMap

    def showText(self):
        print(self.text)

    def showTempData(self):
        print(self.tempData)

    def showColorMap(self):
        print(self.colorMap)

    def showData(self):
        print(self.data)

    def modify_Text_by_pixelFunction(self, fucName, *args):
        chars = ""
        strgs = ""
        if len(args) > 1:
            strgs = args[1].split("\n")
            #print(args[1])

        for x in range(self.width):
            for y in range(self.height):
                asArray = " ".join(args[0][x][y].__str__().split())
                asArray = asArray.replace(" ", ",").replace("[,", "[")
                if len(args) > 1:
                    strippedText = strgs[x][y]
                    chars += self.evaluatePixelFunction(fucName, 1, strippedText, asArray)
                else:
                    chars += self.evaluatePixelFunction(fucName, 0, asArray)
            if x < self.width - 1:
                chars += "\n"
        self.text = chars

    def modify_TempData_by_pixelFunction(self, fucName, *args):
        TData = ""
        for x in range(self.width):
            for y in range(self.height):
                asArray = " ".join(self.data[x][y].__str__().split())
                asArray = asArray.replace(" ", ",").replace("[,", "[")
                TData += self.evaluatePixelFunction(fucName,0, asArray)
            if x < self.width - 1:
                TData += "\n"
        self.tempData = TData

    def modify_ColorMap_by_pixelFunction(self, fucName, *args):
        for x in range(self.width):
            for y in range(self.height):
                asArray3 = " ".join(self.colorMap[x][y].__str__().split())
                asArray3 = asArray3.replace(" ", ",").replace("[,", "[")
                self.colorMap[x][y] = self.evaluatePixelFunction(fucName, 0, asArray3)

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

    def pixel_color_mapping(self, pixel):
        pixNum = int((pixel[0] + pixel[1] + pixel[2]) // 3)
        pixChar = int(np.interp(pixNum, [0, 255], [0, 16]))

    def bake_color_codes(self, inputChar, *args):
        werte = ast.literal_eval(args[0])
        type = len(args)
        if type == 0:
            return self.color_rst + inputChar[0].__str__()
        elif type == 1:
            #print(werte)
            if werte[0] > 15:
                return self.cmd_color_codes_background[werte[0]] + inputChar[0].__str__() + self.color_rst
            else:
                return self.cmd_color_codes_foreground[werte[0]] + inputChar[0].__str__() + self.color_rst
        elif type == 2:
            return inputChar[0].__str__()
        elif type == 3:
            return inputChar[0].__str__()

    def pixelD_match_cmd_color_foreground(self, pixel):
        paare = []
        bestGuess = (0, 0, 0)
        bestGuessNum = 0
        avgNum = 765
        for i in range(15):
            closeR = self.cmd_colors[i][0] - pixel[0]
            closeG = self.cmd_colors[i][1] - pixel[1]
            closeB = self.cmd_colors[i][2] - pixel[2]
            paare.append([closeR, closeG, closeB])
            avgC = closeR + closeG + closeB
            if avgC < avgNum and avgC >= 0:
                avgNum = avgC
                bestGuess = (closeR, closeG, closeB)
                bestGuessNum = i
        #print(bestGuessNum)
        return bestGuessNum



    def evaluatePixelFunction(self, fucName, indicator, *args):
        out = "self." + fucName + "("
        for i in range(args.__len__()):
            if indicator == 1:
                if type(args[i]) == str:
                    out += "\"" + args[i].__str__() + "\""
                else:
                    out += args[i].__str__()
            else:
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