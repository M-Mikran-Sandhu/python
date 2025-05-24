# This is main.py, a script that will use the custom module 'my_module.py'.
# It demonstrates how to import and use components (functions, classes, variables)
# from another Python file in the same directory (or a directory in Python's search path).

# --- What is a Module? ---
# A module is simply a Python file (.py extension) containing Python definitions and statements.
# Modules help you organize your code into logical units, making it:
# - More manageable: Break down large programs into smaller, well-defined pieces.
# - Reusable: Use the same functions or classes in multiple scripts without copying code.
# - Shareable: Distribute your code for others to use.
# 'my_module.py' in this directory is an example of a custom module we've created.

print("--- main.py execution started ---")

# When Python encounters an `import` statement, it looks for the specified module.
# If it's the first time this module is imported in the program, Python will:
# 1. Execute the module file (my_module.py in this case) from top to bottom.
#    This means any statements not inside a function or class, or the `if __name__ == "__main__":`
#    block in the module, will run. (You should see "my_module.py is being imported..." printed).
# 2. Make the module's objects (functions, classes, variables) available to main.py.


# --- 1. Importing the entire module ---
# `import my_module` imports everything from my_module.py under the namespace 'my_module'.
# To access its components, you need to prefix them with `my_module.`.
print("\n--- Method 1: import my_module ---")
import my_module # This executes my_module.py (if not already executed)

# Using the greet function from my_module
message1 = my_module.greet("Alice")
print(f"From my_module.greet: {message1}")

# Using the add function from my_module
sum1 = my_module.add(100, 200)
print(f"From my_module.add(100, 200): {sum1}")

# Accessing the global variable from my_module
print(f"Accessing my_module.MODULE_VERSION: {my_module.MODULE_VERSION}")

# Creating an instance of MyHelperClass from my_module
helper1 = my_module.MyHelperClass("Main Script User 1")
print(helper1.get_info())


# --- 2. Importing specific components using `from ... import ...` ---
# This imports specific names directly into the current script's namespace.
# You don't need to prefix them with the module name.
print("\n--- Method 2: from my_module import greet ---")
from my_module import greet # Only imports the 'greet' function

# Now 'greet' can be called directly
message2 = greet("Bob") # This 'greet' is my_module.greet
print(f"From imported greet: {message2}")

# Note: If main.py had its own 'greet' function, this import would shadow (replace) it
# if 'greet' was defined *before* this import, or be shadowed by it if defined *after*.

# Trying to access 'add' without prefixing or specific import will fail here:
# sum2 = add(5,5) # This would cause a NameError because 'add' is not directly in main.py's namespace yet


# --- 3. Importing a specific component with an alias using `as` ---
# This imports a specific name but gives it a different name (alias) in the current script.
# Useful to avoid naming conflicts or to use a shorter name.
print("\n--- Method 3: from my_module import add as custom_add ---")
from my_module import add as custom_add

sum3 = custom_add(7, 8)
print(f"Result of custom_add(7, 8): {sum3}")
# print(add(7,8)) # This would still cause a NameError as 'add' itself was not directly imported


# --- 4. Importing multiple specific components (including classes and variables) ---
print("\n--- Method 4: from my_module import MyHelperClass, MODULE_VERSION ---")
from my_module import MyHelperClass, MODULE_VERSION

# Now MyHelperClass and MODULE_VERSION can be used directly
helper2 = MyHelperClass("Main Script User 2")
print(helper2.get_info())
print(f"Directly imported MODULE_VERSION: {MODULE_VERSION}")


# --- Understanding `if __name__ == "__main__":` in `my_module.py` ---
# Each Python file has a special built-in variable called `__name__`.
# - When a Python script is run directly (e.g., `python my_module.py`), its `__name__` variable
#   is set to `"__main__"`.
# - When a Python script is imported as a module into another script (like we are doing here
#   with `my_module.py`), its `__name__` variable is set to the name of the module file
#   (i.e., `"my_module"` for `my_module.py`).

# The `if __name__ == "__main__":` block in `my_module.py` contains code that will
# ONLY run if `my_module.py` is executed directly. It will NOT run when `my_module.py`
# is imported by `main.py` (because in that case, `my_module.__name__` is "my_module", not "__main__").

# You should have seen the print statement "my_module.py is being imported or executed."
# from `my_module.py` when this script started (due to the first import).
# However, you should NOT have seen the print statement from inside the
# `if __name__ == "__main__":` block of `my_module.py`.
# To see that, you would need to run `python custom_module_example/my_module.py` from your terminal.

print("\n--- Demonstrating that my_module's __name__ is 'my_module' when imported ---")
# We can even access the __name__ variable of the imported module (though not typical)
if 'my_module' in dir(): # Check if my_module was imported using "import my_module"
    print(f"The __name__ variable of the imported my_module is: {my_module.__name__}")


# --- Best Practices for Importing ---
# - Be specific: `from module import specific_function` is often preferred over `import module`
#   if you only need a few things, as it makes it clearer where names come from.
# - Avoid `from module import *`: This imports all names from the module into the current
#   namespace. It can make it hard to tell where a function or variable came from and
#   can lead to naming conflicts. There are exceptions, but generally, it's discouraged for clarity.
# - Use aliases (`as`) for clarity or to resolve naming conflicts.
# - Place imports at the top of your script (standard convention).

print("\n--- main.py execution finished ---")

# To run this example:
# 1. Make sure both `main.py` and `my_module.py` are in the `custom_module_example` directory.
# 2. Open your terminal.
# 3. Navigate to the `custom_module_example` directory.
# 4. Run this script using the command: `python main.py`
#
# You can also run the module directly to see its `if __name__ == "__main__":` block execute:
# `python my_module.py`
