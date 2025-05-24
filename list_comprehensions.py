# Python List Comprehensions

# List comprehensions provide a concise and readable way to create lists.
# They are often more compact and faster than using traditional `for` loops
# and `append()` calls to build a list.

# The basic syntax is:
# new_list = [expression for item in iterable if condition]
# - expression: The expression to compute for each item (e.g., item * 2).
# - item: The variable representing each element from the iterable.
# - iterable: A sequence or collection to iterate over (e.g., a list, range, tuple).
# - condition (optional): A filter that includes the item in the new list only if the condition is True.

print("--- List Comprehensions ---")

# -------------------------------------------
# 1. Basic List Comprehension (from a range)
# -------------------------------------------
print("\n--- 1. Basic List Comprehension (from a range) ---")

# Goal: Create a list of squares from 0 to 9.

# Using a traditional for loop:
squares_loop = []
for x in range(10): # range(10) produces numbers 0, 1, ..., 9
    squares_loop.append(x * x)
print(f"Squares (using for loop):   {squares_loop}")

# Using a list comprehension:
# expression: x * x
# item: x
# iterable: range(10)
squares_comp = [x * x for x in range(10)]
print(f"Squares (using comprehension): {squares_comp}")
# Notice how the list comprehension is more compact.

# -------------------------------------------------
# 2. List Comprehension with Transformation
# -------------------------------------------------
print("\n--- 2. List Comprehension with Transformation ---")

# Goal: Create a list of uppercase words from a list of lowercase words.
words = ["hello", "world", "python", "is", "fun"]
print(f"Original words: {words}")

# Using a traditional for loop:
uppercase_words_loop = []
for word in words:
    uppercase_words_loop.append(word.upper()) # .upper() converts a string to uppercase
print(f"Uppercase (using for loop):   {uppercase_words_loop}")

# Using a list comprehension:
# expression: word.upper()
# item: word
# iterable: words
uppercase_words_comp = [word.upper() for word in words]
print(f"Uppercase (using comprehension): {uppercase_words_comp}")

# -------------------------------------------------
# 3. List Comprehension with a Conditional Clause (if)
# -------------------------------------------------
print("\n--- 3. List Comprehension with a Conditional Clause (if) ---")

# Goal: Create a list of even numbers from 0 to 19.
numbers = range(20) # Numbers from 0 to 19
print(f"Original numbers: {list(numbers)}") # Convert range to list for printing

# Using a traditional for loop:
even_numbers_loop = []
for num in numbers:
    if num % 2 == 0: # The condition: num is even if num modulo 2 is 0
        even_numbers_loop.append(num)
print(f"Even numbers (using for loop):   {even_numbers_loop}")

# Using a list comprehension with an if condition:
# expression: num
# item: num
# iterable: numbers
# condition: num % 2 == 0
even_numbers_comp = [num for num in numbers if num % 2 == 0]
print(f"Even numbers (using comprehension): {even_numbers_comp}")

# Goal: Get words longer than 3 characters from the 'words' list.
print(f"\nOriginal words: {words}")
long_words_comp = [word for word in words if len(word) > 3]
print(f"Long words (using comprehension): {long_words_comp}")


# -------------------------------------------------
# 4. List Comprehension with 'if-else' (Conditional Expression)
# -------------------------------------------------
print("\n--- 4. List Comprehension with 'if-else' ---")
# Note: The syntax for if-else within a list comprehension is different from the filtering 'if'.
# It's `expression_if_true if condition else expression_if_false` and comes *before* the `for` loop.

# Goal: Create a list where numbers are labeled 'even' or 'odd'.
numbers_to_label = range(1, 6) # 1, 2, 3, 4, 5
print(f"Numbers to label: {list(numbers_to_label)}")

# Using a traditional for loop:
labels_loop = []
for num in numbers_to_label:
    if num % 2 == 0:
        labels_loop.append(f"{num} is even")
    else:
        labels_loop.append(f"{num} is odd")
print(f"Labels (using for loop):   {labels_loop}")

# Using a list comprehension with an if-else expression:
# expression: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
# item: num
# iterable: numbers_to_label
labels_comp = [f"{num} is even" if num % 2 == 0 else f"{num} is odd" for num in numbers_to_label]
print(f"Labels (using comprehension): {labels_comp}")


# -------------------------------------------------
# 5. Nested List Comprehensions (Use with caution, can be hard to read)
# -------------------------------------------------
print("\n--- 5. Nested List Comprehensions ---")

# Goal: Create a flattened list from a list of lists (a matrix).
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Original matrix: {matrix}")

# Using traditional nested for loops:
flattened_loop = []
for row in matrix:
    for item in row:
        flattened_loop.append(item)
print(f"Flattened (using for loops):   {flattened_loop}")

# Using a nested list comprehension:
# The 'for' clauses are in the same order as in the traditional loop.
# expression: item
# outer loop: for row in matrix
# inner loop: for item in row
flattened_comp = [item for row in matrix for item in row]
print(f"Flattened (using comprehension): {flattened_comp}")

# Another example: Create pairs from two lists
list1 = ['A', 'B']
list2 = [1, 2]
print(f"\nList 1: {list1}, List 2: {list2}")

pairs_comp = [(l1, l2) for l1 in list1 for l2 in list2] # (l1, l2) creates a tuple for each pair
print(f"Pairs (using comprehension): {pairs_comp}")
# Output: [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# While powerful, deeply nested comprehensions can become difficult to understand.
# If it's too complex, a traditional for loop might be more readable.

# -------------------------------------------------
# Benefits of List Comprehensions:
# -------------------------------------------------
# 1. Conciseness and Readability: Often more compact and easier to read than equivalent loops,
#    once you are familiar with the syntax.
# 2. Performance: Can be faster than using `append()` in a loop, as they are optimized in CPython.
#    (Though for very complex expressions, this might not always hold true).
# 3. Expressiveness: They are a very Pythonic way to create lists.

print("\n--- List Comprehensions Demonstration Complete ---")

# To run this file:
# 1. Save it as list_comprehensions.py
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python list_comprehensions.py
# The script will print the lists created using both traditional loops and comprehensions.
