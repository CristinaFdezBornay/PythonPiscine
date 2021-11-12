from random import randint

def print_info( ) -> None:
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

def get_guess( ) -> int:
    in_text = input("What's your guess?\n")
    if in_text == "exit":
        print("Goodbye!")
        exit()
    try:
        guess = int(in_text)
        return guess
    except:
        print("That's not a number.")
        return get_guess()

def print_result(secret_number: int, trials: int) -> None:
    if secret_number == 42 and trials == 1:
        print("The answer to the ultimate question of life, the universe and everything is 42.\nCongratulations! You got it on your first try!")
        exit()
    print("Congratulations, you've got it!")
    print("You won in {} attempts!".format(trials))

if __name__ == "__main__":
    print_info()
    secret_number: int = randint(1, 99)
    trials: int = 0
    guess: int = -1
    print(secret_number)
    while guess != secret_number:
        guess = get_guess()
        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        trials += 1
    print_result(secret_number, trials)
