people=[]
for x in range(0,8):
    person=input("Enter a name:")
    people.append(person)

import random

random_num=random.randint(0,7)

random_person=people[random_num]

print("lucky winner is:",random_person)
