colors=["red","yellow","purple","grey","pink","blue","black","white"]

import random
while True:
    random_num=random.randint(0,len(colors)-1)

    random_col=colors[random_num]

    #print(random_col)
    while True:
        guess=input("Enter Color:").lower()

        if (random_col==guess):
            break
        else:
            print("Oops try again")

    print("You Guessed it", random_col)

    play_again=input("Play again 'Yes/No' :").lower()

    if play_again=='no':
        break
    elif play_again=='yes':
        continue
print("It was Fun, thanks")
