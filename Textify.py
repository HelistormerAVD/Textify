from math import trunc
from operator import truediv
from time import sleep
from tkinter import Tk

from PIL import Image
import numpy as np
from tkinter.filedialog import askopenfilename


from functions import ImageText

def load_image_as_array(image_path):
    # Bild öffnen
    img = Image.open(image_path)

    # Bild in RGB konvertieren (falls es Transparenz enthält, wird der Alpha-Kanal ignoriert)
    img = img.convert("RGB")

    # Bild in ein NumPy-Array umwandeln
    pixel_array = np.array(img)

    return pixel_array


if __name__ == "__main__":

    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    while 1:
        image_path = askopenfilename(initialdir="C:\\Users\\kenne\\OneDrive\\Desktop\\Freizeit\\Programme\\python_wii_freez\\SpieleKumpelSWE\\Textify\\testimages\\painting")  # show an "Open" dialog box and return the path to the selected file

        #image_path = "testimages/block/amethyst_cluster.png"  # Pfad zur Bilddatei
        pixel_data = load_image_as_array(image_path)

        print("Bildgröße:", pixel_data.shape)  # Ausgabe der Form des Arrays
        #print("Pixelwerte:", pixel_data)  # Anzeige der RGB-Werte
        #print("\n\n\n\n")
        test = ImageText(pixel_data.shape[0], pixel_data.shape[1])
        #test.showText()
        #print("\n")
        test.setData(pixel_data.copy())  # Ensure a separate copy
        test.setText(pixel_data.copy())  # Ensure a separate copy
        test.setColorMap(pixel_data.copy())  # Ensure a separate copy
        test.modify_Text_by_pixelFunction("pixel_average_brightness_mapping", test.getData())
        test.setTempData(test.text)
        test.showText()
        test.modify_ColorMap_by_pixelFunction("pixelD_match_cmd_color_foreground")
        #test.showData()
        test.modify_Text_by_pixelFunction("bake_color_codes", test.colorMap,test.text)
        test.showText()
        #test.showData()
        sleep(3)