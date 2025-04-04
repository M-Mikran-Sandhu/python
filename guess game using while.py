import random
number=random.randint(0,10)
guess=int(input("'I am thinking about a number  between 1-10' Guess:"))

while True:
    if guess==number:
        print(number,"it is")
        break
    else:
        print("Try again")
        guess=int(input("'I am thinking about a number  between 1-10' Guess:"))
