# Python Advanced Data Structures: Sets, Tuples (In-depth), Dictionaries (In-depth)

import collections # For collections.namedtuple

# -----------------------------------
# 1. SETS
# -----------------------------------
# Sets are unordered collections of unique elements.
# This means an element cannot appear more than once in a set, and the order of elements is not guaranteed.
# Sets are mutable (you can add or remove elements).
# They are very useful for membership testing, removing duplicates from a sequence,
# and performing mathematical set operations like union, intersection, etc.

print("--- 1. Sets ---")

# --- a. Creating Sets ---
print("\n[Sets] Creating Sets:")
# Creating an empty set (must use set(), {} creates an empty dictionary)
empty_set = set()
print(f"Empty set: {empty_set}, type: {type(empty_set)}")

# Creating a set from a list (duplicates are automatically removed)
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
numbers_set = set(numbers_list)
print(f"Set from list {numbers_list}: {numbers_set}") # Output: {1, 2, 3, 4, 5}

# Creating a set directly with elements
fruits_set = {"apple", "banana", "cherry", "apple"} # "apple" appears once
print(f"Set of fruits: {fruits_set}")

# --- b. Adding and Removing Elements ---
print("\n[Sets] Adding and Removing Elements:")
my_set = {1, 3}
print(f"Initial set: {my_set}")

# Add a single element
my_set.add(2) # Adds 2 to the set
print(f"After adding 2: {my_set}")
my_set.add(3) # Adding an existing element does nothing
print(f"After adding 3 again: {my_set}")

# Remove an element
# `remove()` will raise a KeyError if the element is not found.
my_set.remove(3)
print(f"After removing 3: {my_set}")
# my_set.remove(4) # This would cause a KeyError

# `discard()` also removes an element, but does not raise an error if it's not found.
my_set.discard(1)
print(f"After discarding 1: {my_set}")
my_set.discard(4) # No error, element 4 is not in the set
print(f"After discarding 4 (which wasn't there): {my_set}")

# Remove and return an arbitrary element using `pop()`.
# Raises KeyError if the set is empty.
my_set = {'a', 'b', 'c'}
print(f"Set before pop: {my_set}")
popped_element = my_set.pop()
print(f"Popped element: {popped_element}")
print(f"Set after pop: {my_set}")

# Clear all elements from a set
my_set.clear()
print(f"Set after clear: {my_set}")


# --- c. Common Set Operations ---
print("\n[Sets] Common Set Operations:")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union: Elements present in either set_a or set_b (or both). Represented by | operator or .union() method.
union_set = set_a.union(set_b)
# union_set_operator = set_a | set_b # Alternative using operator
print(f"Union (A | B): {union_set}") # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements present in both set_a and set_b. Represented by & operator or .intersection() method.
intersection_set = set_a.intersection(set_b)
# intersection_set_operator = set_a & set_b # Alternative
print(f"Intersection (A & B): {intersection_set}") # Output: {3, 4}

# Difference: Elements present in set_a but not in set_b. Represented by - operator or .difference() method.
difference_set_ab = set_a.difference(set_b) # A - B
# difference_set_ab_operator = set_a - set_b # Alternative
print(f"Difference (A - B): {difference_set_ab}") # Output: {1, 2}

difference_set_ba = set_b.difference(set_a) # B - A
print(f"Difference (B - A): {difference_set_ba}") # Output: {5, 6}

# Symmetric Difference: Elements present in either set_a or set_b, but not in both.
# Represented by ^ operator or .symmetric_difference() method.
symmetric_diff_set = set_a.symmetric_difference(set_b)
# symmetric_diff_set_operator = set_a ^ set_b # Alternative
print(f"Symmetric Difference (A ^ B): {symmetric_diff_set}") # Output: {1, 2, 5, 6}

# --- d. Set Use Cases ---
print("\n[Sets] Use Cases:")
# Membership testing (very efficient for sets)
my_data = {"apple", "banana", "cherry"}
print(f"Is 'apple' in my_data? {'apple' in my_data}")   # True
print(f"Is 'grape' in my_data? {'grape' in my_data}") # False

# Removing duplicates from a list
my_list_with_duplicates = [10, 20, 30, 20, 10, 40, 50, 10]
unique_items_list = list(set(my_list_with_duplicates))
print(f"Original list: {my_list_with_duplicates}")
print(f"List after removing duplicates using set: {unique_items_list}")


# -----------------------------------
# 2. TUPLES (IN-DEPTH)
# -----------------------------------
# Tuples are ordered, immutable sequences. Immutable means once a tuple is created,
# its elements cannot be changed, added, or removed.
# They are often used to store collections of heterogeneous data (i.e., items of different types)
# or when you want to ensure that the data cannot be changed.

print("\n\n--- 2. Tuples (In-depth) ---")

# --- a. Revisiting Immutability ---
print("\n[Tuples] Immutability:")
my_tuple = (1, "hello", 3.14)
print(f"My tuple: {my_tuple}")
# my_tuple[0] = 2 # This would raise a TypeError: 'tuple' object does not support item assignment
# my_tuple.append("world") # This would raise an AttributeError: 'tuple' object has no attribute 'append'

# However, if a tuple contains mutable objects (like a list), the mutable object itself can be changed.
mutable_tuple = ([1, 2], "a_string")
print(f"Mutable tuple: {mutable_tuple}")
mutable_tuple[0].append(3) # The list inside the tuple is changed
print(f"Mutable tuple after modification: {mutable_tuple}") # Output: ([1, 2, 3], 'a_string')

# --- b. Packing and Unpacking ---
print("\n[Tuples] Packing and Unpacking:")
# Packing: When you assign a sequence of values to a single variable, Python packs them into a tuple.
packed_tuple = 10, 20, "packed" # No parentheses needed, but often used for clarity: (10, 20, "packed")
print(f"Packed tuple: {packed_tuple}, type: {type(packed_tuple)}")

# Unpacking: Assigning elements of a tuple to multiple variables.
# The number of variables must match the number of elements in the tuple.
a, b, c = packed_tuple
print(f"Unpacked: a={a}, b={b}, c={c}")

# Unpacking can be useful for swapping variables
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x # y (10) is assigned to x, x (5) is assigned to y
print(f"After swap: x={x}, y={y}")

# Extended unpacking (Python 3) using *
numbers_tuple = (1, 2, 3, 4, 5)
first, second, *rest = numbers_tuple
print(f"Extended unpacking: first={first}, second={second}, rest={rest} (type: {type(rest)})")
first, *middle, last = numbers_tuple
print(f"Extended unpacking: first={first}, middle={middle}, last={last}")

# --- c. Named Tuples (collections.namedtuple) ---
# Named tuples provide a way to create tuple subclasses with named fields.
# This makes your code more readable as you can access elements by name instead of index.
print("\n[Tuples] Named Tuples:")

# Define a named tuple 'Point' with fields 'x' and 'y'
Point = collections.namedtuple('Point', ['x', 'y'])
# Point = collections.namedtuple('Point', 'x y') # Alternative string syntax for fields

# Create instances of the Point named tuple
p1 = Point(10, 20)
p2 = Point(x=30, y=40) # Can also use keyword arguments

print(f"Point p1: {p1}")
print(f"Point p2: {p2}")

# Access elements by name
print(f"p1.x = {p1.x}, p1.y = {p1.y}")

# Access elements by index (still possible, like regular tuples)
print(f"p2[0] = {p2[0]}, p2[1] = {p2[1]}")

# Named tuples are still immutable
# p1.x = 15 # This would raise an AttributeError

# You can convert a named tuple to a dictionary
print(f"p1 as dictionary: {p1._asdict()}")


# -----------------------------------
# 3. DICTIONARIES (IN-DEPTH)
# -----------------------------------
# Dictionaries are unordered (in Python versions before 3.7, ordered in 3.7+) collections of
# key-value pairs. Each key must be unique and immutable (e.g., string, number, or tuple).
# Values can be of any type and can be duplicated.
# Dictionaries are mutable.

print("\n\n--- 3. Dictionaries (In-depth) ---")
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Initial dictionary: {my_dict}")

# --- a. Iterating Through Dictionaries ---
print("\n[Dicts] Iterating:")
# Iterating through keys (this is the default iteration behavior)
print("Keys:")
for key in my_dict:
    print(f"  {key} (value: {my_dict[key]})")

# Iterating through values using .values()
print("\nValues:")
for value in my_dict.values():
    print(f"  {value}")

# Iterating through key-value pairs (items) using .items()
print("\nItems (key-value pairs):")
for key, value in my_dict.items():
    print(f"  Key: {key}, Value: {value}")

# --- b. Dictionary Comprehensions ---
# A concise way to create dictionaries.
print("\n[Dicts] Dictionary Comprehensions:")

# Example 1: Create a dictionary of squares
squares_dict = {x: x*x for x in range(1, 6)}
# Equivalent for loop:
# squares_dict_loop = {}
# for x in range(1, 6):
#   squares_dict_loop[x] = x*x
print(f"Squares dictionary: {squares_dict}") # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 2: From two lists
keys_list = ["a", "b", "c"]
values_list = [10, 20, 30]
dict_from_lists = {keys_list[i]: values_list[i] for i in range(len(keys_list))}
# A more Pythonic way for the above using zip:
# dict_from_lists_zip = {k: v for k, v in zip(keys_list, values_list)}
print(f"Dictionary from lists {keys_list} and {values_list}: {dict_from_lists}")

# Example 3: With a condition
original_prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75, "grape": 2.0}
expensive_items = {item: price for item, price in original_prices.items() if price > 0.8}
print(f"Expensive items from {original_prices}: {expensive_items}")

# --- c. Safe Access with .get() and .setdefault() ---
print("\n[Dicts] Safe Access:")
student_grades = {"Alice": 85, "Bob": 92}
print(f"Grades: {student_grades}")

# Accessing a key that exists
print(f"Alice's grade: {student_grades['Alice']}")

# Accessing a key that does NOT exist using [] will raise a KeyError
# print(student_grades['Charlie']) # This would cause a KeyError

# Using .get(key, default_value) for safe access
# If the key exists, its value is returned.
# If the key does not exist, the default_value is returned (None if not specified).
charlie_grade = student_grades.get("Charlie")
print(f"Charlie's grade (using get()): {charlie_grade}") # Output: None

charlie_grade_default = student_grades.get("Charlie", "Not found") # Providing a default
print(f"Charlie's grade (using get() with default): {charlie_grade_default}") # Output: Not found

bob_grade = student_grades.get("Bob", "Not found")
print(f"Bob's grade (using get() with default): {bob_grade}") # Output: 92 (key exists)

# Using .setdefault(key, default_value)
# If the key exists, its value is returned.
# If the key does not exist, it is inserted into the dictionary with the default_value,
# and then default_value is returned.
print(f"\nUsing setdefault():")
print(f"Grades before setdefault for David: {student_grades}")
david_grade = student_grades.setdefault("David", 70) # David is not in dict, so he's added with grade 70
print(f"David's grade (using setdefault()): {david_grade}")
print(f"Grades after setdefault for David: {student_grades}")

alice_grade_setdefault = student_grades.setdefault("Alice", 90) # Alice exists, her grade is returned, dict not changed
print(f"Alice's grade (using setdefault()): {alice_grade_setdefault}")
print(f"Grades after setdefault for Alice: {student_grades}")


print("\n\n--- Advanced Data Structures Demonstration Complete ---")

# To run this file:
# 1. Save it as advanced_data_structures.py
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python advanced_data_structures.py
# The script will print its actions to the console, demonstrating each concept.
