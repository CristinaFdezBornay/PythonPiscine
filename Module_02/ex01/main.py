import re

class ObjectC(object):
    def __init__(self):
        pass

def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    var = [] 
    for i in range(len(args)):
        var_name = f"var_{i}"
        obj.__setattr__(var_name, args[i])
        var.append(var_name)
    for key, val in kwargs.items():
        if key in var:
            return None
        obj.__setattr__(key, val)
    return obj

def doom_printer(obj):
    if obj is None:
        print("ERROR\n------------------------")
        return
    for attr in dir(obj):
        if attr[0] == '_':
            continue
        value = getattr(obj, attr)
        print("{}: {}".format(attr, value))
    print("------------------------")

if __name__ == "__main__":
    print("\nExample 1: 7")
    obj = what_are_the_vars(7)
    doom_printer(obj)

    print("\nExample 2: None, []")
    obj = what_are_the_vars(None, [])
    doom_printer(obj)

    print("\nExample 3: \"ft_lol\", \"Hi\"")
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)

    print("\nExample 4: None")
    obj = what_are_the_vars(None)
    doom_printer(obj)

    print("\nExample 5: 12, \"Yes\", [0, 0, 0], a=10, hello=\"world\"")
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)

    print("\nExample 6: 42, a=10, var_0=\"world\"")
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

    print("\nExample 7: 42, \"Yes\", a=10, var_21=\"world\"")
    obj = what_are_the_vars(42, "Yes", a=10, var_21="world")
    doom_printer(obj)

    print("\nExample 8: lambda x: x, function=what_are_the_var")
    obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
    doom_printer(obj)
