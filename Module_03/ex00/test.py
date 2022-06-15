from NumPyCreator import NumPyCreator as npc
import numpy as np
import warnings
warnings.filterwarnings("error")

functions_tests = [
    {
        "ft_name": "npc.from_list",
        "ft_ours": npc.from_list,
        "ft_real": np.array,
        "test": [
            [1,2,3,6,3,4],
            [[1,2,3], [6,3,4]],
            [['1','2','3'],['a','b','c'],['5.0', '6.1', '7.8']],
            [[],[]],
            None,
            4,
            [[1,2,3],[6,4]],
            ((1,2),(3,4))
        ]
    },
    {
        "ft_name": "npc.from_tuple",
        "ft_ours": npc.from_tuple,
        "ft_real": np.array,
        "test": [
            (0, 10),
            ("a","b","c"),
            (1, 4, 6),
            ((1,2),(3,4)),
            None,
            4,
            [[1,2,3],[6,3,4]]
        ]
    },
    {
        "ft_name": "npc.from_iterable",
        "ft_ours": npc.from_iterable,
        "ft_real": np.array,
        "test": [
            range(5),
            range(23, 28),
            None,
            4,
            [[1,2,3],[6,3,4]]
        ]
    },
    {
        "ft_name": "npc.from_shape",
        "ft_ours": npc.from_shape,
        "ft_real": np.zeros,
        "test": [
            (3,5),
            (0,0),
            None,
            4,
            [[1,2,3],[6,3,4]]
        ]
    },
    {
        "ft_name": "npc.random",
        "ft_ours": npc.random,
        "ft_real": None,
        "test": [
            (3,5),
            None,
            4,
            [[1,2,3],[6,3,4]]
        ]
    },
    {
        "ft_name": "npc.identity",
        "ft_ours": npc.identity,
        "ft_real": np.identity,
        "test": [
            0,
            4,
            None,
            [[1,2,3],[6,3,4]]
        ]
    },
]

if __name__=="__main__":
    for ft_test in functions_tests:
        print(f"\n==== TESTING ===> {ft_test['ft_name']}")
        for test in ft_test['test']:
            print(f"=== Test {ft_test['ft_name']} : {str(test)}")
            try:
                if ft_test['ft_real']:
                    print(f"= Numpy output :\n{ft_test['ft_real'](test)}")
            except:
                print(f"= Numpy crashed when testing {str(ft_test['ft_real'])}({str(test)})")
                pass
            print(f"= Our output :\n{ft_test['ft_ours'](test)}")
            input("====>\n")