class GotCharacter():
    """A class that allows user to manage characters. Stores name and alive status"""
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        """Prints the house words. Attribute that is unique to each house"""
        print(self.house_words)

    def die(self):
        """Method that will set is_alive status to False and kill the GotCharacter"""
        print(f"\n=> {self.first_name}.die()")
        self.is_alive = False

if __name__ == "__main__":
    empty_GC = GotCharacter()
    print("=> Empty GotCharacter")
    print(empty_GC.__dict__)

    random_GC = GotCharacter("Random", True)
    print("\n=> Random GotCharacter")
    print(random_GC.__dict__)
    print(random_GC.__doc__)

    arya = Stark("Arya")
    print("\n=> Arya.__dict__ :")
    print(arya.__dict__)

    print("\n=> Arya.print_house_words()")
    arya.print_house_words()

    print(f"\n=> Arya.is_alive : {arya.is_alive}")
    arya.die()
    print(f"\n=> Arya.is_alive : {arya.is_alive}")

    print(f"\n=> Arya.__doc__  : {arya.__doc__}")

    lol = Stark("LOL")
    print("\n=> LOL.__dict__ :")
    print(lol.__dict__)