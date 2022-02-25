from ColorFilter import ColorFilter
from ImageProcessor import ImageProcessor # Copy file from ex01

functions_to_test = [
    ColorFilter.invert,
    ColorFilter.to_blue,
    ColorFilter.to_green,
    ColorFilter.to_red,
    ColorFilter.to_celluloid,
    ColorFilter.to_grayscale,
]

if __name__=="__main__":
    elon_array = ImageProcessor.load("elon_canaGAN.png")
    ImageProcessor.display(elon_array)
    for ft in functions_to_test:
        print(f"= Testing function ColorFilter.{ft.__name__}:")
        ImageProcessor.display(ft(elon_array))
        input("=>\n")
