# Python Advanced Error Handling Techniques

# Error handling is crucial for writing robust and user-friendly programs.
# Python provides a flexible `try...except` mechanism to manage exceptions.

print("--- Advanced Error Handling ---")

# -------------------------------------------
# 1. Specific Exceptions
# -------------------------------------------
# It's good practice to catch specific exceptions rather than a generic `except Exception:` or `except:`.
# This allows you to handle different types of errors in different ways and prevents
# your program from accidentally catching exceptions you didn't intend to (like SystemExit or KeyboardInterrupt).

print("\n--- 1. Catching Specific Exceptions ---")

def divide_numbers_specific():
    try:
        numerator = int(input("[Specific] Enter numerator: "))
        denominator = int(input("[Specific] Enter denominator: "))
        result = numerator / denominator
        print(f"[Specific] Result of division: {result}")
    except ValueError:
        # Handles errors if input cannot be converted to an integer (e.g., user types "abc")
        print("[Specific] Error: Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        # Handles errors if the denominator is zero
        print("[Specific] Error: Cannot divide by zero.")
    # except Exception as e: # A more general fallback, but try to be specific first
    #     print(f"[Specific] An unexpected error occurred: {e}")

# divide_numbers_specific() # Uncomment to test this section

# -------------------------------------------
# 2. Multiple Exception Blocks
# -------------------------------------------
# You can have multiple `except` blocks to handle different types of exceptions
# that might occur within a single `try` block. Python will execute the first
# `except` block that matches the type of exception raised.

print("\n--- 2. Multiple Exception Blocks (same as above, just emphasizing the structure) ---")
# The `divide_numbers_specific()` function above already demonstrates multiple except blocks.
# Each `except` targets a different potential error: `ValueError` or `ZeroDivisionError`.

def open_and_process_file_multiple():
    file_path = input("[Multiple] Enter file path to open (e.g., 'data.txt' or 'non_existent.txt'): ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Let's imagine we want to convert the first line to an integer
            first_line_value = int(content.splitlines()[0])
            print(f"[Multiple] First line as integer: {first_line_value}")
            print(f"[Multiple] File content:\n{content}")
    except FileNotFoundError:
        print(f"[Multiple] Error: The file '{file_path}' was not found.")
    except ValueError:
        print("[Multiple] Error: The first line of the file could not be converted to an integer.")
    except IndexError:
        print("[Multiple] Error: The file is empty or does not have enough lines.")
    except Exception as e: # Catch-all for other unexpected errors
        print(f"[Multiple] An unexpected error occurred: {e}")

# open_and_process_file_multiple() # Uncomment to test

# -------------------------------------------
# 3. The `else` Clause
# -------------------------------------------
# The `else` block is optional and, if present, is executed only if the `try` block
# completes without raising any exceptions.
# It's useful for code that should run only when the `try` part was successful.

print("\n--- 3. The `else` Clause ---")

def divide_numbers_with_else():
    try:
        numerator = int(input("[Else] Enter numerator: "))
        denominator = int(input("[Else] Enter denominator: "))
        result = numerator / denominator
    except ValueError:
        print("[Else] Error: Invalid input. Please enter numbers only.")
    except ZeroDivisionError:
        print("[Else] Error: Cannot divide by zero.")
    else:
        # This block runs only if no exceptions occurred in the try block.
        print(f"[Else] Division successful! Result: {result}")
        print("[Else] The 'else' block is a good place for code that depends on the try block succeeding.")

# divide_numbers_with_else() # Uncomment to test

# -------------------------------------------
# 4. The `finally` Clause
# -------------------------------------------
# The `finally` block is optional and, if present, is always executed,
# regardless of whether an exception occurred in the `try` block or not.
# It's typically used for cleanup actions, like closing files or releasing resources,
# ensuring these actions happen no matter what.

print("\n--- 4. The `finally` Clause ---")

def example_with_finally():
    file = None # Initialize file variable
    try:
        print("\n[Finally] Attempting to open 'temp_file.txt' for writing.")
        file = open("temp_file.txt", "w")
        user_input = input("[Finally] Enter data to write (or type 'error' to cause one): ")
        if user_input.lower() == 'error':
            # Intentionally cause an error after the file is opened
            result = 10 / 0
        file.write(user_input)
        print("[Finally] Data written to temp_file.txt successfully.")
    except ZeroDivisionError:
        print("[Finally] Error: Oops, a ZeroDivisionError occurred!")
    except Exception as e:
        print(f"[Finally] An unexpected error occurred: {e}")
    finally:
        # This block will always execute.
        print("[Finally] The 'finally' block is executing now.")
        if file: # Check if file was successfully opened
            file.close()
            print("[Finally] File 'temp_file.txt' has been closed.")
        else:
            print("[Finally] File was not opened, so no need to close.")
        # You might also remove the temp file here if it's just for this example
        # import os
        # if os.path.exists("temp_file.txt"):
        #     os.remove("temp_file.txt")
        #     print("[Finally] temp_file.txt removed.")

# example_with_finally() # Uncomment to test

# -------------------------------------------
# 5. Raising Exceptions (`raise`)
# -------------------------------------------
# You can manually trigger (raise) exceptions using the `raise` keyword.
# This is useful when you detect an error condition in your code and want to
# signal that something has gone wrong, often based on custom logic.

print("\n--- 5. Raising Exceptions ---")

def validate_age(age):
    try:
        age_num = int(age)
        if age_num < 0:
            # Raise a ValueError if the age is negative, which is logically incorrect.
            raise ValueError("Age cannot be negative.")
        elif age_num < 18:
            # Raise a custom message or a specific type of error for under-age.
            raise Exception("User is underage for this service.") # Can be more specific
        else:
            print(f"[Raise] Age {age_num} is valid.")
            return True
    except ValueError as ve: # Catch the ValueError we might raise, or from int()
        print(f"[Raise] Value Error: {ve}")
        return False
    except Exception as e: # Catch other exceptions we might raise
        print(f"[Raise] General Error: {e}")
        return False

# print("\n[Raise] Testing age validation:")
# validate_age("25")
# validate_age("-5")
# validate_age("abc")
# validate_age("15")


# -------------------------------------------
# 6. Custom Exceptions
# -------------------------------------------
# You can define your own custom exception classes by inheriting from the base `Exception` class
# (or a more specific built-in exception class).
# Custom exceptions make your error handling more specific and readable.

print("\n--- 6. Custom Exceptions ---")

# Define a custom exception class
class NegativeNumberError(Exception):
    """Custom exception raised when a non-negative number is expected but a negative one is given."""
    def __init__(self, number, message="Negative numbers are not allowed here."):
        self.number = number
        self.message = message
        # Call the base class constructor with the message
        super().__init__(f"{message} (Received: {self.number})")

class ValueTooSmallError(Exception):
    """Custom exception for values that are too small."""
    pass # Can be as simple as this if no extra attributes/methods are needed


def process_positive_number(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError("Input must be a number.")
        if num < 0:
            # Raise our custom exception
            raise NegativeNumberError(num)
        if num < 10:
            raise ValueTooSmallError(f"The number {num} is too small, expected 10 or more.")
        print(f"[CustomExc] Processing number: {num}. Square is {num*num}.")
    except NegativeNumberError as nne:
        # Handle our custom exception specifically
        print(f"[CustomExc] NegativeNumberError Caught: {nne}")
        # print(f"[CustomExc] The problematic number was: {nne.number}") # Access custom attribute
    except ValueTooSmallError as vtse:
        print(f"[CustomExc] ValueTooSmallError Caught: {vtse}")
    except TypeError as te:
        print(f"[CustomExc] TypeError Caught: {te}")


# print("\n[CustomExc] Testing custom exceptions:")
# process_positive_number(25)
# process_positive_number(-5)
# process_positive_number(5) # Will raise ValueTooSmallError
# process_positive_number("text") # Will raise TypeError


print("\n--- Advanced Error Handling Demonstration Complete ---")
print("Uncomment the function calls in the script to test each section interactively.")

# How to test:
# 1. Save this file as advanced_error_handling.py
# 2. Run `python advanced_error_handling.py` in your terminal.
# 3. Uncomment one function call at a time (e.g., `divide_numbers_specific()`)
#    and re-run the script to see that specific error handling technique in action.
#    Follow the prompts to provide input that might cause errors.
