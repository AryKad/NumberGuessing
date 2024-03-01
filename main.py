import random
from logo import logo
print(logo)
print("Welcome to the Number Guessing Game!")
ch=input("Choose a difficulty.Type 'easy' or 'hard': ")
def game(count):
    print("I am thinking of a number between 1 to 100")
    num = random.randint(1, 100)
    while(count>0):
        print(f"You have got {count} guesses left")
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}")
            break
        elif guess < num:
            print("too low. Guess again")
            count-=1
        else:
            print("too high.")
            count-=1
            if count == 0:
                print("You've run out of guesses. You lose")
            else:
                print("Guess again")
if ch=="easy":
    game(10)
else:
    game(5)
