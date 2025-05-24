# This is a Python module named 'my_module'.
# A module is simply a Python file with a .py extension that contains Python definitions and statements.
# Modules are used to organize code into logical units, making it more manageable, reusable, and shareable.

print("my_module.py is being imported or executed.")

# --- 1. Global Variable ---
# This is a variable defined at the module level.
# It can be imported and accessed by other scripts that import this module.
MODULE_VERSION = "1.0"

# --- 2. Functions ---
# Functions defined in a module can be imported and used in other scripts.

def greet(name):
    """
    A simple function that returns a greeting string.
    Args:
        name (str): The name of the person to greet.
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome from my_module."

def add(a, b):
    """
    A simple function that adds two numbers.
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    Returns:
        int or float: The sum of a and b.
    """
    return a + b

# --- 3. Class ---
# Classes defined in a module can also be imported and used to create objects.

class MyHelperClass:
    """
    A simple example class within the module.
    """
    def __init__(self, owner_name="DefaultOwner"):
        """
        Constructor for MyHelperClass.
        Args:
            owner_name (str): The name of the owner of this helper instance.
        """
        self.owner_name = owner_name
        print(f"MyHelperClass instance created by {self.owner_name}.")

    def get_info(self):
        """
        A method that returns some information about the instance.
        Returns:
            str: Information string.
        """
        return f"This is a MyHelperClass object, owned by {self.owner_name}. Module version: {MODULE_VERSION}"

# --- 4. The `if __name__ == "__main__":` block ---
# This block of code is executed only when the module is run directly as a script
# (e.g., by typing `python my_module.py` in the terminal).
# It is NOT executed when the module is imported into another script.
# This is useful for including test code or a demonstration of the module's capabilities
# that should only run when the module itself is the main program.

if __name__ == "__main__":
    # This code runs ONLY if you execute `python custom_module_example/my_module.py`
    print("\n--- my_module.py executed directly ---")
    print("This part of the script runs because __name__ is currently '__main__'.")

    # Example usage of the module's components when run directly:
    print("\nDirect execution examples:")
    current_version = MODULE_VERSION
    print(f"Module Version (accessed directly): {current_version}")

    greeting_message = greet("Developer")
    print(greeting_message)

    sum_result = add(10, 5)
    print(f"Result of add(10, 5): {sum_result}")

    helper_instance = MyHelperClass("Direct Script User")
    print(helper_instance.get_info())

    print("\n--- End of my_module.py direct execution ---")

# When this file is imported by another script (like main.py):
# - The initial print statement ("my_module.py is being imported...") will run.
# - Definitions (MODULE_VERSION, greet, add, MyHelperClass) will be loaded.
# - The code inside `if __name__ == "__main__":` will NOT run.
#   In that case, __name__ for this file will be "my_module" (the name of the module).
