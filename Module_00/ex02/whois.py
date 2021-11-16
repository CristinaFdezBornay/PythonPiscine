import sys

def check_args():
    """
    Function to verify arguments number and validity. Only one argument is allowed + program name
    """
    if len(sys.argv) != 2:
        print('ERROR')
        return sys.exit(0)
    try:
        arg = int(sys.argv[1])
    except:
        print('ERROR')
        return sys.exit(0)

def odd_or_even(arg):
    number = int(arg)
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__=="__main__":
    check_args()
    odd_or_even(sys.argv[1])