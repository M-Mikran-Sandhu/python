import matplotlib.pyplot as plt

# Collect data
num_entries = int(input("Enter number of countries: "))
countries = []
death_ratios = []

for i in range(num_entries):
    country = input(f"Enter name of country {i+1}: ")
    ratio = float(input(f"Enter death ratio for {country} (e.g., 2.5 for 2.5%): "))
    countries.append(country)
    death_ratios.append(ratio)

# Plotting the death ratio
plt.figure(figsize=(10, 6))
plt.plot(countries, death_ratios, marker='o', linestyle='-', color='red', label='Death Ratio')
plt.xlabel("Countries")
plt.ylabel("Death Ratio (%)")
plt.title("Death Ratio by Country")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()  # Add this line to display the legend
plt.tight_layout()
plt.show()
