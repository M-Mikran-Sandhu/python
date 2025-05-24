# Get input from the user for two grades.
# `float()` converts the text input into a number with decimal points.
grade1 = float(input("Input first grade (0-10):"))
grade2 = float(input("Input second grade (0-10):"))

# Get input for the number of absences and total classes.
# `int()` converts the text input into a whole number.
absences = int(input("Input number of absences:"))
total_classes = int(input("Input total number of classes:"))

# Calculate the average of the two grades.
avg_grade = (grade1 + grade2) / 2

# Calculate the attendance rate as a percentage.
# 1. Subtract absences from total classes to get attended classes.
# 2. Divide attended classes by total classes.
# 3. Multiply by 100 to get a percentage.
attendance_rate = ((total_classes - absences) / total_classes) * 100

# Print the calculated average grade.
print("Average grade:", round(avg_grade, 2))
# Print the calculated attendance rate, followed by a '%' sign.
print("Attendance rate:", round(attendance_rate, 2), "%")

# Determine if the student is approved or failed based on grade and attendance.
# The student is approved if their average grade is 6 or higher AND their attendance rate is 80% or higher.
if avg_grade >= 6 and attendance_rate >= 80:
    print("Approved")
# If both average grade is less than 6 AND attendance rate is less than 80%, they fail due to both.
elif avg_grade < 6 and attendance_rate < 80:
    print("Failed due to low grade and low attendance.")
# If attendance is sufficient (80% or higher) but the grade is low (less than 6), they fail due to low grade.
elif attendance_rate >= 80: # This implies avg_grade < 6 because the first 'if' condition was not met.
    print("Failed due to low grade.")
# If the grade is sufficient (6 or higher) but attendance is low (less than 80%), they fail due to low attendance.
# This 'else' covers the case where avg_grade >= 6 (because the second 'elif' was not met)
# and attendance_rate < 80 (because the first 'if' and third 'elif' were not met).
else: # This implies avg_grade >=6 and attendance_rate < 80
    print("Failed due to low attendance.")
