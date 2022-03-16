from ColorFilter import ColorFilter
try:
    from ImageProcessor import ImageProcessor
except:
    print("Please import ImageProcessor from ex01")

functions_to_test = [
    ColorFilter.invert,
    ColorFilter.to_blue,
    ColorFilter.to_green,
    ColorFilter.to_red,
    ColorFilter.to_celluloid,
]

if __name__=="__main__":
    try:
        elon_array = ImageProcessor.load("elon_canaGAN.png")
        ImageProcessor.display(elon_array)
        
        for ft in functions_to_test:
            print(f"= Testing function ColorFilter.{ft.__name__}")
            ImageProcessor.display(ft(elon_array))
        
        print(f"= Testing function ColorFilter.to_grayscale ('m')")
        out = ColorFilter.to_grayscale(elon_array, 'm')
        ImageProcessor.display(out)
        
        print(f"= Testing function ColorFilter.to_grayscale ('w', weights=[0.5, 0.1, 0.4])")
        out = ColorFilter.to_grayscale(elon_array, 'w', weights=[0.5, 0.1, 0.4])
        ImageProcessor.display(out)
    
    except Exception as e:
        print(e)
