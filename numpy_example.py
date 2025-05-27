import numpy as np

def demonstrate_numpy_operations():
    """Demonstrates some basic NumPy operations."""

    print("--- NumPy Demonstration ---")

    # Create a NumPy array from a Python list
    list_a = [1, 2, 3, 4, 5]
    array_a = np.array(list_a)
    print(f"Array 'a' from list: {array_a}")
    print(f"Type of array_a: {type(array_a)}")
    print(f"Shape of array_a: {array_a.shape}")
    print(f"Data type of array_a: {array_a.dtype}")

    # Create an array with a specified data type
    array_b = np.array([1.0, 2.5, 3.3], dtype=np.float32)
    print(f"\nArray 'b' with float32 dtype: {array_b}")

    # Create arrays with initial placeholders
    zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
    print(f"\nZeros array (2x3):\n{zeros_array}")

    ones_array = np.ones((3, 2))  # 3x2 array of ones
    print(f"\nOnes array (3x2):\n{ones_array}")

    range_array = np.arange(0, 10, 2)  # Like Python's range, but returns an ndarray
    print(f"\nArray created with arange(0, 10, 2): {range_array}")

    linspace_array = np.linspace(0, 1, 5) # 5 numbers evenly spaced between 0 and 1
    print(f"\nArray created with linspace(0, 1, 5): {linspace_array}")

    random_array = np.random.rand(2, 2) # 2x2 array of random numbers (0 to 1)
    print(f"\nRandom array (2x2):\n{random_array}")

    # Array Reshaping
    array_c = np.arange(1, 7)
    print(f"\nOriginal array 'c': {array_c}")
    reshaped_array_c = array_c.reshape(2, 3)
    print(f"Reshaped array 'c' (2x3):\n{reshaped_array_c}")
    
    # Array Slicing (similar to Python lists but can be multi-dimensional)
    print(f"\nElement at index 1 of reshaped_array_c[0,1]: {reshaped_array_c[0, 1]}")
    print(f"First row of reshaped_array_c: {reshaped_array_c[0, :]}")
    print(f"First column of reshaped_array_c:\n{reshaped_array_c[:, 0]}")

    # Basic mathematical operations (element-wise)
    array_x = np.array([1, 2, 3])
    array_y = np.array([4, 5, 6])

    print(f"\nArray x: {array_x}")
    print(f"Array y: {array_y}")
    print(f"x + y = {array_x + array_y}")
    print(f"x * 2 = {array_x * 2}")
    print(f"x ** 2 = {array_x ** 2}")
    print(f"np.sqrt(x) = {np.sqrt(array_x)}")
    print(f"np.sin(x) = {np.sin(array_x)}") # Universal functions (ufuncs)

    # Dot product
    dot_product = np.dot(array_x, array_y)
    print(f"\nDot product of x and y: {dot_product}")
    
    # Sum, min, max, mean
    print(f"\nSum of elements in reshaped_array_c: {reshaped_array_c.sum()}")
    print(f"Min of elements in reshaped_array_c: {reshaped_array_c.min()}")
    print(f"Max of elements in reshaped_array_c: {reshaped_array_c.max()}")
    print(f"Mean of elements in reshaped_array_c: {reshaped_array_c.mean()}")
    print(f"Sum of columns in reshaped_array_c: {reshaped_array_c.sum(axis=0)}") # axis 0 = columns
    print(f"Sum of rows in reshaped_array_c: {reshaped_array_c.sum(axis=1)}")    # axis 1 = rows

    print("\n--- NumPy Demonstration End ---")

if __name__ == "__main__":
    demonstrate_numpy_operations()
