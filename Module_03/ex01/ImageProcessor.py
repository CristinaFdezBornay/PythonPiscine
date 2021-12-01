# import matplotlib

class ImageProcessor():
    def load(path):
        try:
            file = open(path, 'r')
            print(file)
        except Exception as e:
            print("Exception: {} -- strerror: {}".format(e.__class__.__name__, e))
    
    def display(array):
        try:
            print(array)
        except Exception as e:
            print("Exception: {} -- strerror: {}".format(e.__class__.__name__, e))