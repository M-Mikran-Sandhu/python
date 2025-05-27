import matplotlib.pyplot as plt
import numpy as np

def demonstrate_matplotlib_plotting():
    """Demonstrates some basic Matplotlib plotting functionalities."""

    print("--- Matplotlib Demonstration ---")

    # --- Line Plot ---
    print("\nGenerating a simple line plot...")
    # Sample data
    x_line = np.array([1, 2, 3, 4, 5])
    y_line = np.array([2, 4, 1, 5, 3]) # Some y-values

    plt.figure(figsize=(8, 5)) # Optional: specify figure size
    plt.plot(x_line, y_line, marker='o', linestyle='-', color='b', label='Sample Data')
    
    # Adding titles and labels
    plt.title('Simple Line Plot')
    plt.xlabel('X-axis Values')
    plt.ylabel('Y-axis Values')
    plt.legend() # Display the label
    plt.grid(True) # Add a grid
    
    # Save the plot to a file
    line_plot_filename = "line_plot_example.png"
    try:
        plt.savefig(line_plot_filename)
        print(f"Line plot saved as {line_plot_filename}")
    except Exception as e:
        print(f"Error saving line plot: {e}")
    # plt.show() # Uncomment to display the plot interactively if desired (blocks execution)
    plt.close() # Close the figure to free up memory

    # --- Bar Chart ---
    print("\nGenerating a simple bar chart...")
    # Sample data
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [10, 24, 15, 30]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
    
    # Adding titles and labels
    plt.title('Simple Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.xticks(rotation=15) # Rotate category labels slightly if long
    
    # Save the plot to a file
    bar_chart_filename = "bar_chart_example.png"
    try:
        plt.savefig(bar_chart_filename)
        print(f"Bar chart saved as {bar_chart_filename}")
    except Exception as e:
        print(f"Error saving bar chart: {e}")
    # plt.show() # Uncomment to display
    plt.close()

    # --- Scatter Plot ---
    print("\nGenerating a simple scatter plot...")
    # Sample data
    x_scatter = np.random.rand(50) # 50 random x values
    y_scatter = np.random.rand(50) # 50 random y values
    colors = np.random.rand(50)    # Random colors for points
    sizes = 100 * np.random.rand(50) # Random sizes for points

    plt.figure(figsize=(8, 5))
    plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.7, cmap='viridis')

    plt.title('Simple Scatter Plot')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.colorbar(label='Color Intensity') # Show color scale

    scatter_plot_filename = "scatter_plot_example.png"
    try:
        plt.savefig(scatter_plot_filename)
        print(f"Scatter plot saved as {scatter_plot_filename}")
    except Exception as e:
        print(f"Error saving scatter plot: {e}")
    # plt.show()
    plt.close()

    print("\n--- Matplotlib Demonstration End ---")
    print("Note: Plot images (line_plot_example.png, bar_chart_example.png, scatter_plot_example.png) have been saved in the root directory.")

if __name__ == "__main__":
    demonstrate_matplotlib_plotting()
