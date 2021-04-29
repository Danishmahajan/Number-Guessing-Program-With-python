Number = 18
Chances=1
print("Welcome To Number Guessing Game  ")
print("Number of guesses is limited to only 6 times: ")
while(Chances<=6):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("you enter less number please input greater number.\n")
    elif guess_number > 18:
        print("you enter greater number please input smaller number.\n ")
    else:
        print("you won\n")
        print(Chances, "no.of guesses he took to finish.")
        break
    print(6 - Chances, "no. of guesses left")
    Chances = Chances + 1

    if (Chances > 6):
        print("Game Over,You  are unable to guess")

