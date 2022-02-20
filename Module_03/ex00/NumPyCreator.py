import numpy as np
from typing import List, Iterable, Tuple

class NumPyCreator():
    def from_list(lst:list=[]):
        try:
            if type(lst) != list:
                return None
            for l in lst:
                if len(l) != len(lst[0]):
                    return None
            return np.array(lst)
        except:
            return None
    
    def from_tuple(tpl:tuple):
        try:
            if type(tpl) != tuple:
                return None
            return np.array(tpl)
        except:
            return None

    def from_iterable(itr:iter):
        try:
            lst:list = []
            for it in itr:
                lst.append(it)
            return np.array(lst)
        except:
            return None

    def from_shape(shape:tuple, value:int=0):
        try:
            if type(shape) != tuple:
                return None
            if type(value) != int:
                return None
            output = np.ones(shape)
            output *= value
            return output
        except:
            return None
    
    def random(shape:tuple):
        try:
            if type(shape) != tuple:
                return None
            return np.random.randint(0, 100, shape)
        except:
            return None

    def identity(n:int):
        try:
            if type(n) != int:
                return None
            return np.identity(n)
        except:
            return None