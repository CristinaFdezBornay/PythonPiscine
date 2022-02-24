from PIL import Image
from numpy import asarray

class ImageProcessor():
    def load(path):
        try:
            img = Image.open(path)
            numpydata = asarray(img)
            x, y, c = numpydata.shape
            print(f"Image from path '{path}' has been successfully loaded => SHAPE ({x}x{y})")
            return numpydata
        except Exception as e:
            print(e)
    
    def display(array):
        try:
            img = Image.fromarray(array)
            img.show()
        except Exception as e:
            print(e)