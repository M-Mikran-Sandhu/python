# Object-Oriented Programming (OOP) Concepts in Python

# OOP is a programming paradigm based on the concept of "objects",
# which can contain data in the form of fields (often known as attributes or properties)
# and code in the form of procedures (often known as methods).

# -----------------------------------
# 1. CLASSES
# -----------------------------------
# A class is a blueprint for creating objects. It defines a set of attributes and methods
# that the created objects will have.

print("--- 1. Classes and Objects ---")

class Dog:
    # This is a class attribute. It's shared by all instances (objects) of the class.
    species = "Canis familiaris"

    # This is the constructor method, also known as the initializer.
    # It's automatically called when you create a new object (instance) of the class.
    # 'self' refers to the instance being created.
    # 'name' and 'age' are instance attributes, specific to each object.
    def __init__(self, name, age):
        self.name = name  # Attribute specific to each Dog instance
        self.age = age    # Attribute specific to each Dog instance
        self._secret_trick = "Roll over" # Example of a "non-public" attribute convention
        self.__very_secret_mood = "Always happy" # Example of name mangling for "pseudo-private"

    # This is an instance method. It operates on an instance of the class ('self').
    def description(self):
        # f-strings (formatted string literals) are a convenient way to embed expressions inside string literals.
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}!"

    # Method to demonstrate accessing "private" attributes (for illustration)
    def reveal_secret_trick(self):
        return f"{self.name}'s secret trick is to {self._secret_trick}."

    def reveal_mood(self):
        # Accessing name-mangled attribute (Python renames it to _ClassName__attributeName)
        return f"{self.name}'s mood: {self._Dog__very_secret_mood}"


# -----------------------------------
# 2. OBJECTS (Instances)
# -----------------------------------
# An object is an instance of a class. When a class is defined, no memory is allocated
# until an object of that class is created.

# Creating (instantiating) objects of the Dog class
dog1 = Dog("Buddy", 3)  # Calls the __init__ method with name="Buddy", age=3
dog2 = Dog("Lucy", 5)   # Calls the __init__ method with name="Lucy", age=5

# Accessing instance attributes
print(f"{dog1.name} is an instance of Dog.")
print(f"{dog2.name} is also an instance of Dog.")

# Accessing class attributes
# Can be accessed via the class itself or an instance
print(f"All dogs belong to the species: {Dog.species}")
print(f"{dog1.name} is a {dog1.species}.")

# Calling instance methods
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog2.speak("Woof"))  # Output: Lucy says Woof!

# -----------------------------------
# 3. INHERITANCE
# -----------------------------------
# Inheritance allows a new class (child/derived class) to inherit attributes and methods
# from an existing class (parent/base class). This promotes code reuse.

print("\n--- 3. Inheritance ---")

# Parent class (already defined as Dog)

# Child class inheriting from Dog
class GoldenRetriever(Dog):
    # The child class can have its own __init__ method.
    def __init__(self, name, age, favorite_toy):
        # 'super()' calls the __init__ method of the parent class (Dog).
        # This ensures that the parent's initialization logic (like setting name and age) is executed.
        super().__init__(name, age)
        self.favorite_toy = favorite_toy  # Attribute specific to GoldenRetriever

    # Child class can have its own methods
    def fetch(self, item):
        return f"{self.name} fetches the {item}. Their favorite toy is {self.favorite_toy}."

    # Child class can also override methods from the parent class
    def speak(self, sound="Bark"): # Overriding the speak method
        return f"{self.name} (a Golden Retriever) enthusiastically says {sound}!"

# Creating an instance of the child class
golden = GoldenRetriever("Charlie", 2, "tennis ball")

# Accessing attributes and methods from both parent and child class
print(golden.description())  # Inherited from Dog: Charlie is 2 years old.
print(golden.speak())        # Overridden in GoldenRetriever: Charlie (a Golden Retriever) enthusiastically says Bark!
print(golden.speak("Grrr"))  # Overridden in GoldenRetriever: Charlie (a Golden Retriever) enthusiastically says Grrr!
print(golden.fetch("stick")) # Defined in GoldenRetriever: Charlie fetches the stick. Their favorite toy is tennis ball.
print(f"{golden.name} is a {golden.species}") # Accessing class attribute inherited from Dog


# -----------------------------------
# 4. ENCAPSULATION
# -----------------------------------
# Encapsulation is the bundling of data (attributes) and methods that operate on the data
# into a single unit (a class). It also restricts direct access to some of an object's components.
# Python doesn't have strict private attributes like Java or C++, but uses conventions:
# - _non_public: Treated as a hint that it's for internal use.
# - __pseudo_private: Name mangling is applied (e.g., __mood becomes _Dog__mood).
#   This makes it harder to access accidentally from outside but not truly private.

print("\n--- 4. Encapsulation ---")

# dog1 is an instance of Dog class created earlier
print(f"Dog's name: {dog1.name}") # Public attribute, directly accessible

# Accessing "non-public" attribute (by convention, should be avoided directly from outside)
# print(f"Dog's secret trick (direct access): {dog1._secret_trick}") # Possible, but not recommended
print(dog1.reveal_secret_trick()) # Accessing via a public method is preferred

# Accessing "pseudo-private" attribute (name mangled)
# print(dog1.__very_secret_mood) # This would cause an AttributeError

# Accessing it via its mangled name (demonstrates it's not truly private)
# print(f"Dog's mood (mangled name access): {dog1._Dog__very_secret_mood}") # Possible, but not recommended
print(dog1.reveal_mood()) # Accessing via a public method is preferred

# The idea is to protect attributes from accidental modification and to manage access through methods.

# -----------------------------------
# 5. POLYMORPHISM
# -----------------------------------
# Polymorphism means "many forms". In OOP, it refers to the ability of different classes
# to be treated as objects of a common superclass.
# A common use is "duck typing": "If it walks like a duck and quacks like a duck, then it must be a duck."
# This means Python cares more about whether an object has a certain method or property,
# rather than its specific type.

# More commonly, polymorphism allows different classes to have methods with the same name,
# and these methods can behave differently for each class.

print("\n--- 5. Polymorphism ---")

class Cat(Dog): # Let's make Cat inherit from Dog for this example, though not biologically accurate
    def __init__(self, name, age, color):
        super().__init__(name, age) # Call Dog's init
        self.color = color

    # Cat has its own 'speak' method
    def speak(self, sound="Meow"): # Overriding the speak method
        return f"{self.name} (a cat) purrs: {sound}"

class Parrot: # Parrot does not inherit from Dog
    def __init__(self, name, can_talk=True):
        self.name = name
        self.can_talk = can_talk

    # Parrot also has a 'speak' method
    def speak(self, phrase="Squawk"):
        if self.can_talk:
            return f"{self.name} (a parrot) repeats: '{phrase}'"
        else:
            return f"{self.name} (a parrot) just squawks."

# Create instances of Dog, Cat, and Parrot
dog_poly = Dog("Rex", 4)
cat_poly = Cat("Whiskers", 3, "grey")
parrot_poly = Parrot("Polly")
silent_parrot = Parrot("Silent Bob", can_talk=False)

# Create a list of different animal objects
animals = [dog_poly, cat_poly, parrot_poly, silent_parrot]

# Iterate through the list and call the 'speak' method on each object.
# Even though each object is of a different class (or configured differently),
# they all respond to the 'speak()' call in their own way.
print("\nDemonstrating Polymorphism (common method name):")
for animal in animals:
    # Python doesn't strictly check if 'animal' is of a specific type that 'must' have .speak().
    # It just tries to call .speak(). If the method exists, it works. This is duck typing.
    if hasattr(animal, 'speak'): # Good practice to check if method exists
        print(animal.speak())
    else:
        print(f"{animal.name} can't speak.")

# Another example: a function that uses the .speak() method
def animal_communication(animal_object):
    # This function doesn't care what type of animal_object it is,
    # as long as it has a 'speak' method.
    print(f"Communicating with {animal_object.name}: {animal_object.speak('Hello!')}")

print("\nDemonstrating Polymorphism (duck typing with a function):")
animal_communication(dog_poly)
animal_communication(cat_poly)
animal_communication(parrot_poly)

print("\n--- OOP Concepts Demonstration Complete ---")

# To run this file, save it as oop_concepts.py and run 'python oop_concepts.py' in your terminal.
# You will see the output of the print statements demonstrating each concept.
