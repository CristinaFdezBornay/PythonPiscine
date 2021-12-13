
class GotCharacter():
    def __init__(self, first_name: str = None, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self) -> None:
        print(self.house_words)

    def die(self) -> None:
        print(f"\n=> {self.first_name}.die()")
        self.is_alive = False

if __name__ == "__main__":
    Arya = Stark("Arya")
    print("=> Arya.__dict__ :")
    print(Arya.__dict__)
    print("\n=> Arya.print_house_words()")
    Arya.print_house_words()
    print(f"\n=> Arya.is_alive : {Arya.is_alive}")
    Arya.die()
    print(f"\n=> Arya.is_alive : {Arya.is_alive}")
    print(f"\n=> Arya.__doc__  : {Arya.__doc__}")
