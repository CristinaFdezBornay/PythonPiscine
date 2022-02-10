from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce

iterable = [1, 2, 3, 4, 5]
functions = {
    "map": ft_map,
    "filter": ft_filter,
    "reduce": ft_reduce,
}

def unit_test(message, function_to_test, function_to_apply, iterable):
    try:
        print("\n=> ", message)
        print(list(functions[function_to_test](function_to_apply, iterable)))
    except TypeError as e:
        print(e)

def test_errors(function_to_test, function_to_apply):
    print(f"=============  ft_{function_to_test}  =============")
    unit_test("Passing None as function_to_apply", function_to_test, None, iterable)
    unit_test("Passing None as iterator", function_to_test, function_to_apply, None)
    unit_test("Passing not iterable object", function_to_test, function_to_apply, 2)
    unit_test("Passing a non valid function_to_apply", function_to_test, "LOL", iterable)
    input("\n============= Press ENTER to continue ==>\n")

if __name__=="__main__":
    test_errors("map", lambda dum: dum + 1)
    test_errors("filter", lambda dum: not (dum % 2))
    test_errors("reduce", lambda u, v: u + v)

    unit_test("Valid test map 1", "map", lambda x: x + 2, [])
    unit_test("Valid test map 2", "map", lambda x: x + 2, [1])
    unit_test("Valid test map 3", "map", lambda x: x + 2, iterable)
    unit_test("Valid test map 4", "map", lambda x: x ** 2, iterable)
    input("\n============= Press ENTER to continue ==>\n")

    unit_test("Valid test filter 1", "filter", lambda x: x <= 1, [])
    unit_test("Valid test filter 2", "filter", lambda x: x <= 1, [2])
    unit_test("Valid test filter 3", "filter", lambda x: x <= 1, [0])
    unit_test("Valid test filter 4", "filter", lambda x: x <= 2, iterable)
    input("\n============= Press ENTER to continue ==>\n")

    unit_test("Valid test reduce 1", "reduce", lambda x, y: x + y, [])
    unit_test("Valid test reduce 2", "reduce", lambda x, y: x + y, [1])
    unit_test("Valid test reduce 3", "reduce", lambda x, y: x + y, ['H', 'o', 'l', 'a', ' ', 'l', 'o', 'k', 'i'])
    unit_test("Valid test reduce 4", "reduce", lambda x, y: x * y, iterable)
    input("\n============= Press ENTER to continue ==>\n")

