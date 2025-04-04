import time as t
import sys
print(sys.path)
import matplotlib.pyplot as plt

# Setting the word for the typing test
word = "pakistan"

# Validating the difficulty level
while True:
    n = int(input("Enter difficulty level (1-10): "))
    if n < 1 or n > 10:
        print("Wrong level!")
        continue
    else:
        break

num = n  # To preserve the original difficulty level
print(f"Write the word '{word}' {n} times.")

times = []  # To store time taken for each attempt
mistake = 0  # To count mistakes

# Typing test loop
while n:
    start = t.time()  # Start the timer
    test = input("Enter: ")
    end = t.time()  # End the timer
    time_taken = end - start
    times.append(time_taken)

    # Decrement the remaining attempts
    n -= 1

    # Count mistakes
    if test != word:
        mistake += 1

# Generating attempt numbers for plotting
y = list(range(1, num + 1))  # Matches the number of attempts

# Plotting the results
plt.plot(y, times, marker='o', linestyle='-', color='b')
plt.xlabel("Attempt Number")
plt.ylabel("Time Taken (seconds)")
plt.title("Typing Test Evaluation")
plt.grid()

# Printing results
print(f"You have made {mistake} mistakes.")
print("Your test evaluation is loading...")

t.sleep(2)  # Adding a slight delay for effect
plt.show()
