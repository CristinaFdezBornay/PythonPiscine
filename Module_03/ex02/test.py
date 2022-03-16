import numpy as np
from ScrapBooker import ScrapBooker

sb = ScrapBooker()
sb_functions = {
    "crop" : sb.crop,
    "thin" : sb.thin,
    "juxtapose" : sb.juxtapose,
    "mosaic" : sb.mosaic
}

def unit_test(ft, array, **kwargs):
    try:
        print(f"\n==> Test {ft} : {kwargs}")
        out = sb_functions[ft](array, **kwargs)
        print("Output :")
        print(out)
        input(">>")
    except Exception as exception:
        print(exception)

if __name__ == '__main__':
    array_ints = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array_ints)
    array_chars =  np.array("A B C D E F G H I J K".split() * 8).reshape(-1, 11)
    print(array_chars)

    print("==== TESTING FUNCTION CROP ===")
    unit_test("crop", array=array_ints, dim=(0,0), position=(0,0))
    unit_test("crop", array=array_ints, dim=(1,1), position=(0,0))
    unit_test("crop", array=array_ints, dim=(2,1), position=(0,0))
    unit_test("crop", array=array_ints, dim=(1,2), position=(0,0))
    unit_test("crop", array=array_ints, dim=(2,2), position=(0,0))
    unit_test("crop", array=array_ints, dim=(2,2), position=(1,0))
    unit_test("crop", array=array_ints, dim=(2,2), position=(0,1))
    unit_test("crop", array=array_ints, dim=(2,2), position=(1,1))
    unit_test("crop", array=array_ints, dim=(2,2), position=(2,2))

    print("==== TESTING FUNCTION THIN ===")
    unit_test("thin", array=array_chars, n=0, axis=1)
    unit_test("thin", array=array_chars, n=1, axis=1)
    unit_test("thin", array=array_chars, n=3, axis=1)
    unit_test("thin", array=array_chars, n=9, axis=1)
    unit_test("thin", array=array_chars, n=0, axis=0)
    unit_test("thin", array=array_chars, n=1, axis=0)
    unit_test("thin", array=array_chars, n=3, axis=0)
    unit_test("thin", array=array_chars, n=9, axis=0)

    print("=== TESTING FUNCTION JUXTAPOSE ===")
    unit_test("juxtapose", array=array_ints, n=0, axis=1)
    unit_test("juxtapose", array=array_ints, n=1, axis=1)
    unit_test("juxtapose", array=array_ints, n=3, axis=1)
    unit_test("juxtapose", array=array_ints, n=8, axis=1)
    unit_test("juxtapose", array=array_ints, n=0, axis=0)
    unit_test("juxtapose", array=array_ints, n=1, axis=0)
    unit_test("juxtapose", array=array_ints, n=3, axis=0)

    print("=== TESTING FUNCTION MOSAIC ===")
    unit_test("mosaic", array=array_ints, dim=(0,0))
    unit_test("mosaic", array=array_ints, dim=(1,1))
    unit_test("mosaic", array=array_ints, dim=(2,2))
    unit_test("mosaic", array=array_ints, dim=(3,5))
    unit_test("mosaic", array=array_ints, dim=(2,9))
