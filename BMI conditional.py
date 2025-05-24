# Get input from the user for their weight and height.
# The `float()` function is used to convert the input (which is initially text) into a number with decimal points.
weight = float(input("Enter Weight (in kilograms):"))
height = float(input("Enter Height (in meters):"))

# Calculate BMI using the formula: weight / (height squared)
# BMI (Body Mass Index) is a measure of body fat based on height and weight.
bmi = weight / (height**2)

# Print the calculated BMI, rounded to two decimal places for readability.
print("Your Body Mass Index =", round(bmi, 2))

# Check the BMI value and print the corresponding category.
# These categories are based on common BMI classifications.

# If BMI is less than 18.5, the person is considered Underweight.
if bmi < 18.5:
    print("You Are Under Weight")
# If BMI is between 18.5 (inclusive) and 24.9 (inclusive), the person is considered Normal Weight.
elif bmi >= 18.5 and bmi <= 24.9:
    print("You Are Normal Weight")
# If BMI is between 24.9 (exclusive, so greater than 24.9) and 29.9 (exclusive, so less than 29.9),
# the person is considered Overweight.
elif bmi > 24.9 and bmi < 29.9:
    print("You Are Over Weight")
# If BMI is 29.9 or greater, the person is considered to have Obesity.
# This 'else' covers all cases where BMI is not in the ranges above (i.e., >= 29.9).
else:
    print("You Are Obesity")
