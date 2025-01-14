# Play with Computer
import random

num = random.randint(1, 10)
guess = 0

while guess != num:
    guess = int(input("Guess a number"))
    if guess < num:
        print("it is smaller")
    elif guess > num:
        print('it is larger')
    else:
        print("Correct Guess")

# Play with mate
player1 = int(input("Enter a number"))
player2 = 0
while player1 != player2:
    player2 = int(input("Guess the number of first player"))
    if player2 > player1:
        print("No Your number is larger ")
    elif player2 < player1:
        print("No your number is smaller")
    else:
        print("You are Right that is my number")
