# Functions are reusable blocks of code that perform a specific task.

# This is a simple function that greets a person.
# 'person' is a parameter - it's a placeholder for the value that will be passed to the function when it's called.
def say_hello_simple(person):
    # This function now returns a greeting string.
    # It uses an f-string (formatted string literal) to include the 'person' variable directly in the string.
    return f"Hello {person}, How are you"

# Calling the say_hello_simple function and printing its returned value.
# An argument is the actual value passed to a function's parameter.
returned_greeting_simple = say_hello_simple("mms")
print(f"Output of say_hello_simple('mms'): {returned_greeting_simple}")

# This function converts a temperature from Fahrenheit to Celsius.
# 'fahr' is the parameter representing the temperature in Fahrenheit.
def fahrtocelsius(fahr):
    # This is the formula to convert Fahrenheit to Celsius.
    # 1. Subtract 32 from the Fahrenheit temperature.
    # 2. Multiply the result by 5.
    # 3. Divide that result by 9.
    celsius = (5 * (fahr - 32)) / 9
    # This line returns the calculated Celsius temperature.
    # The 'return' statement sends a value back to where the function was called.
    return celsius

# Calling the fahrtocelsius function with 100 as the argument.
# The result is rounded to 2 decimal places for better readability.
celsius_temp = fahrtocelsius(100)
print(f"Celsius output for fahrtocelsius(100): {round(celsius_temp, 2)}")

# This is a more advanced greeting function with a default parameter value.
# 'person1' is a required parameter.
# 'person2' is an optional parameter with a default value of "mafia".
# If no value is provided for 'person2' when the function is called, "mafia" will be used.
def say_hello_adv(person1, person2="mafia"):
    # This function now returns a greeting string including both person1 and person2.
    return f"Hello {person1}, How are you? And hello to {person2}!"

# Calling the say_hello_adv function with two arguments and printing its returned value.
returned_greeting_adv1 = say_hello_adv("mms", "ucp")
print(f"Output of say_hello_adv('mms', 'ucp'): {returned_greeting_adv1}")

# Calling the say_hello_adv function with only one argument and printing its returned value.
returned_greeting_adv2 = say_hello_adv("friend")
print(f"Output of say_hello_adv('friend'): {returned_greeting_adv2}")
