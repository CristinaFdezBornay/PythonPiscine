import sys

def usage():
    return '''Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3'''

def parse_arguments():
    """
    Parse arguments from command line
    """
    if len(sys.argv) == 1:
        print(usage())
        return sys.exit(0)
    elif len(sys.argv) > 3:
        print("InputError: too many arguments\n")
        print(usage())
        return sys.exit(0)
    try:
        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])
        return (number1, number2)
    except:
        print("InputError: only numbers\n")
        print(usage())
        return sys.exit(0)

def compute_operations(numbers):
    operations = {}
    operations['Sum'] = numbers[0] + numbers[1]
    operations['Difference'] = numbers[0] - numbers[1]
    operations['Product'] = numbers[0] * numbers[1]
    if numbers[1] != 0:
        operations['Quotient'] = numbers[0] / numbers[1]
        operations['Remainder'] = numbers[0] % numbers[1]
    else:
        operations['Quotient'] = 'ERROR (div by zero)'
        operations['Remainder'] = 'ERROR (modulo by zero)'
    return operations

def display_operations(operations):
    print("{0: <12}{1}".format('Sum:', operations['Sum']))
    print("{0: <12}{1}".format('Difference:', operations['Difference']))
    print("{0: <12}{1}".format('Product:', operations['Product']))
    print("{0: <12}{1}".format('Quotient:', operations['Quotient']))
    print("{0: <12}{1}".format('Remainder:', operations['Remainder']))

if __name__=='__main__':
    numbers = parse_arguments()
    operations = compute_operations(numbers)
    display_operations(operations)