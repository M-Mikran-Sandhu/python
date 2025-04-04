# Initialize an empty list for names
people = []

# Collect 8 names from the user
for x in range(0, 8):
    person = input("Enter a name: ")
    people.append(person)

# Input the name to search for
getnam = input("Enter the name you want to search: ")

# Search for the name in the list
if getnam in people:
    print("Name found")
else:
    print("Name not found")
