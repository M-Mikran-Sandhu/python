import matplotlib.pyplot as plt

# Collecting expense data
num_items = int(input("Enter the number of expense categories: "))
categories = []
expenses = []

for i in range(num_items):
    category = input(f"Enter category {i+1}: ")
    amount = float(input(f"Enter amount for {category}: "))
    categories.append(category)
    expenses.append(amount)

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title("Expense Distribution")
plt.axis('equal')  # Makes the pie chart a circle
plt.show()
