people=['Mikran','Imran','Mawaan']
print(people)
new=input("Enter a name you want to add in the list:")
people.append(new)
print(people)
rem=input("Enter a name you want to remove in the list:")        
people.remove(rem)
print(people)
exn=input("Enter a name you want to exchange in the list:")
pos=int(input("Enter a position you want to exchange in the list:"))

people.insert(pos,exn)
print(people)

people.pop()
print(people)
