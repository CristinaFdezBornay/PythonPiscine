import numpy as np
from typing import List, Iterable, Tuple

class NumPyCreator():
    def from_list(lst:list=[]):
        if type(lst) != list:
            return None
        for l in lst:
            if len(l) != len(lst[0]):
                return None
        try:
            return np.array(lst, dtype='<U21')
        except:
            return None
    
    def from_tuple(tpl:tuple=(42,42)):
        if type(tpl) != tuple:
            return None
        return np.array(tpl)

    def from_iterable(itr:iter):
        lst:list = []
        for it in itr:
            lst.append(it)
        return np.array(lst)

    def from_shape(shape:Tuple=(4, 2), value:int=0):
        output = np.ones(shape)
        output *= value
        return output
    
    def random(shape:Tuple=(4, 2)):
        return np.random.randint(0, 100, shape)

    def identity(n:int=3):
        return np.identity(n)