from generator import *



def main():
    text = "Le Lorem Ipsum est simplement du faux texte."

    # Example 1:
    try:
        print("==> text is None")
        for word in generator(None):
            print(word)
    except:
        pass

    # Example 2:
    try:
        print("\n==> text is not a str")
        for word in generator(12):
            print(word)
    except:
        pass

    # Example 3:
    try:
        print("\n==> option is not a str")
        for word in generator(text, option=22):
            print(word)
    except:
        pass

    # Example 4:
    try:
        print("\n==> option is not one of the predertermined options")
        for word in generator(text, option="lol"):
            print(word)
    except:
        pass

    # Example 5:
    print("\n==> sep = default (' ') and option default")
    for word in generator(text):
        print(word)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 6:
    print("\n==> sep = 'est' and option default")
    for word in generator(text, sep='est'):
        print(word)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 7:
    print("\n==> sep = default (' ') and option unique")
    for word in generator(text, option="unique"):
        print(word)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 8:
    print("\n==> sep = default (' ') and option shuffle")
    for word in generator(text, option="shuffle"):
        print(word)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 9:
    print("\n==> sep = default (' ') and option ordered")
    for word in generator(text, option="ordered"):
        print(word)

if __name__=="__main__":
    main()