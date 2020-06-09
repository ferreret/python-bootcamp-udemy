import random

keeps_playing = ""

while keeps_playing != "n":
    random_number = random.randint(1, 10)
    guess_number = ""
    while guess_number != random_number:
        guess_number = input("Guess a number between 1 and 10: ")
        guess_number = int(guess_number)
        if guess_number == random_number:
            print("You guessed it! You won!")
        elif guess_number > random_number:
            print("Too high, try again!")
        else:
            print("Too low, try again!")
    keeps_playing = input("Do you want to keep playing: (y/n)")

print("Thanks for playing. Bye!")
