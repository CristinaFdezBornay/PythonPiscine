from PIL import Image
import numpy as np

class ImageProcessor():
    def load(path):
        try:
            img = Image.open(path)
            numpydata = np.asarray(img)
            x, y, c = numpydata.shape
            print(f"Image from path '{path}' has been successfully loaded => SHAPE ({x}x{y})")
            return numpydata
        except Exception as e:
            print(e)
    
    def display(array):
        try:
            img = Image.fromarray((array).astype(np.uint8))
            img.show()
        except Exception as e:
            print(e)