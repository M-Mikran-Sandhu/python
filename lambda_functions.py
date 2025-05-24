# Python Lambda Functions (Anonymous Functions)

# A lambda function is a small, anonymous, inline function defined using the `lambda` keyword.
# They are also known as "anonymous functions" because they don't have a formal name
# defined with `def` (unless you assign them to a variable, which is common).

# Syntax:
# lambda arguments: expression
# - `lambda`: The keyword that indicates you are defining a lambda function.
# - `arguments`: One or more arguments, separated by commas (just like regular function arguments).
# - `expression`: A single expression that is evaluated and returned.
#   Lambda functions cannot contain multiple expressions or complex statements. They are limited
#   to a single expression.

print("--- Lambda Functions ---")

# -------------------------------------------
# 1. Basic Lambda Function Syntax
# -------------------------------------------
print("\n--- 1. Basic Lambda Function Syntax ---")

# Example: A lambda function that adds two numbers.
add = lambda x, y: x + y
# - `lambda`: Keyword
# - `x, y`: Arguments
# - `x + y`: Expression (this value will be returned)

# Calling the lambda function (it's assigned to the variable 'add')
result = add(5, 3)
print(f"Result of add(5, 3): {result}") # Output: 8

# You can use lambda functions immediately without assigning them to a variable,
# though this is less common for direct calls and more for passing as arguments.
immediate_result = (lambda a, b: a * b)(4, 5)
print(f"Result of (lambda a, b: a * b)(4, 5): {immediate_result}") # Output: 20

# Comparison with a regular function defined using `def`:
def add_def(x, y):
    return x + y

result_def = add_def(5, 3)
print(f"Result of add_def(5, 3) (using def): {result_def}")
# Lambda functions are more concise for simple, single-expression functions.

# -------------------------------------------
# 2. Use Cases for Lambda Functions
# -------------------------------------------
# Lambda functions are most useful when you need a small, throwaway function for a short period,
# often as an argument to higher-order functions (functions that take other functions as arguments).

print("\n--- 2. Use Cases for Lambda Functions ---")

# --- a. With `sorted()` ---
# The `sorted()` function can take a `key` argument, which is a function that
# returns a value to be used for sorting. Lambdas are perfect for simple keys.
print("\n[Lambda] Using with sorted():")
points = [(1, 5), (3, 2), (5, 8), (2, 0)]
print(f"Original points: {points}")

# Sort points based on the second element (y-coordinate) of each tuple
# Using a lambda function as the key:
# For each item `p` in `points`, `lambda p: p[1]` returns `p[1]` (the y-coordinate).
sorted_by_y = sorted(points, key=lambda p: p[1])
print(f"Points sorted by y-coordinate (using lambda): {sorted_by_y}")

# For comparison, using a regular function:
def get_y_coordinate(point):
    return point[1]
sorted_by_y_def = sorted(points, key=get_y_coordinate)
print(f"Points sorted by y-coordinate (using def):    {sorted_by_y_def}")
# The lambda version is more compact for this simple key.

# Sort a list of dictionaries by a specific key's value
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
print(f"\nOriginal students: {students}")
sorted_students_by_grade = sorted(students, key=lambda student: student['grade'])
print(f"Students sorted by grade (using lambda): {sorted_students_by_grade}")


# --- b. With `map()` ---
# The `map()` function applies a given function to each item of an iterable (e.g., list)
# and returns a map object (which can be converted to a list).
print("\n[Lambda] Using with map():")
numbers = [1, 2, 3, 4, 5]
print(f"Original numbers: {numbers}")

# Goal: Create a new list where each number is squared.
# Using lambda with map:
# `lambda x: x * x` is applied to each element `x` in `numbers`.
squared_numbers_map = map(lambda x: x * x, numbers)
squared_numbers_list = list(squared_numbers_map) # Convert map object to list
print(f"Squared numbers (using lambda with map): {squared_numbers_list}")

# For comparison, using a list comprehension (often preferred over map for this):
squared_numbers_comp = [x * x for x in numbers]
print(f"Squared numbers (using list comprehension): {squared_numbers_comp}")

# For comparison, using a regular function with map:
def square(x):
    return x * x
squared_numbers_map_def = map(square, numbers)
print(f"Squared numbers (using def with map):    {list(squared_numbers_map_def)}")
# Lambda is concise for simple transformations with map.

# --- c. With `filter()` ---
# The `filter()` function constructs an iterator from elements of an iterable
# for which a function returns true.
print("\n[Lambda] Using with filter():")
numbers_for_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers for filter: {numbers_for_filter}")

# Goal: Create a list of only the even numbers.
# Using lambda with filter:
# `lambda x: x % 2 == 0` returns True if x is even, False otherwise.
# filter() will include only those elements for which the lambda returns True.
even_numbers_filter = filter(lambda x: x % 2 == 0, numbers_for_filter)
even_numbers_list = list(even_numbers_filter) # Convert filter object to list
print(f"Even numbers (using lambda with filter): {even_numbers_list}")

# For comparison, using a list comprehension (often preferred over filter for this):
even_numbers_comp = [x for x in numbers_for_filter if x % 2 == 0]
print(f"Even numbers (using list comprehension): {even_numbers_comp}")

# For comparison, using a regular function with filter:
def is_even(x):
    return x % 2 == 0
even_numbers_filter_def = filter(is_even, numbers_for_filter)
print(f"Even numbers (using def with filter):    {list(even_numbers_filter_def)}")
# Lambda is concise for simple filtering conditions.


# -------------------------------------------
# 3. When to Use Lambda Functions
# -------------------------------------------
# - **Short, simple operations:** When the function logic is very simple and can be expressed in a single line.
# - **As arguments to higher-order functions:** This is the most common and idiomatic use (e.g., `map`, `filter`, `sorted`, UI event handlers).
# - **Readability for simple cases:** For simple tasks, a lambda can be more readable than defining a full function, as the logic is right where it's used.

# When NOT to use Lambda Functions:
# - **Complex logic:** If the function requires multiple lines of code, complex logic, or many statements, use a regular `def` function.
# - **When you need docstrings:** Lambda functions cannot have docstrings.
# - **When you need type hints for arguments/return value in a reusable way:** While you can assign a lambda to a variable and type hint that variable, `def` functions offer more standard and readable type hinting.
# - **If it makes the code harder to read:** If a lambda becomes too convoluted, a named `def` function is often clearer.

print("\n--- Lambda Functions Demonstration Complete ---")

# To run this file:
# 1. Save it as lambda_functions.py
# 2. Open a terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python lambda_functions.py
# The script will print the results of various lambda function applications.
