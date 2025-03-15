from PIL import Image
import numpy as np

from functions import ImageText

ESC = ""
def load_image_as_array(image_path):
    # Bild öffnen
    img = Image.open(image_path)

    # Bild in RGB konvertieren (falls es Transparenz enthält, wird der Alpha-Kanal ignoriert)
    img = img.convert("RGB")

    # Bild in ein NumPy-Array umwandeln
    pixel_array = np.array(img)

    return pixel_array


if __name__ == "__main__":
    image_path = "testimages/block/acacia_door_bottom.png"  # Pfad zur Bilddatei
    pixel_data = load_image_as_array(image_path)

    print("Bildgröße:", pixel_data.shape)  # Ausgabe der Form des Arrays
    #print("Pixelwerte:", pixel_data)  # Anzeige der RGB-Werte
    #print("\n\n\n\n")
    test = ImageText(8, 8)
    test.showData()
    print("\n")
    test.setText(pixel_data)
    test.showText()
