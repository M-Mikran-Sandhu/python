import pandas as pd
import numpy as np

def demonstrate_pandas_operations():
    """Demonstrates some basic Pandas operations."""

    print("--- Pandas Demonstration ---")

    # Creating a DataFrame from a Python dictionary
    data_dict = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Salary': [70000, 80000, 90000, 75000, 65000]
    }
    df_from_dict = pd.DataFrame(data_dict)
    print("\nDataFrame created from a dictionary:")
    print(df_from_dict)

    # Creating a DataFrame from a NumPy array
    data_np = np.array([
        ['Alice', 25, 'New York', 70000],
        ['Bob', 30, 'Los Angeles', 80000],
        ['Charlie', 35, 'Chicago', 90000]
    ])
    df_from_np = pd.DataFrame(data_np, columns=['Name', 'Age', 'City', 'Salary'])
    # Pandas will infer types, but Age and Salary might be objects. Let's convert.
    df_from_np['Age'] = pd.to_numeric(df_from_np['Age'])
    df_from_np['Salary'] = pd.to_numeric(df_from_np['Salary'])
    print("\nDataFrame created from a NumPy array (with type conversion):")
    print(df_from_np)

    # Basic DataFrame inspection
    print("\n--- DataFrame Inspection (using df_from_dict) ---")
    print(f"Shape of the DataFrame: {df_from_dict.shape}") # (rows, columns)
    print("\nFirst 3 rows (head()):")
    print(df_from_dict.head(3))
    print("\nLast 2 rows (tail()):")
    print(df_from_dict.tail(2))
    print("\nDataFrame info (dtypes, non-null counts):")
    df_from_dict.info()
    print("\nDescriptive statistics for numerical columns (describe()):")
    print(df_from_dict.describe())

    # Column Selection
    print("\n--- Column Selection ---")
    names_series = df_from_dict['Name']
    print("Selected 'Name' column (as a Series):")
    print(names_series)
    print(f"Type of names_series: {type(names_series)}")

    name_and_city_df = df_from_dict[['Name', 'City']]
    print("\nSelected 'Name' and 'City' columns (as a DataFrame):")
    print(name_and_city_df)

    # Row Selection (using .loc and .iloc)
    print("\n--- Row Selection ---")
    # .loc uses labels
    print("Row with index label 1 (Bob):")
    print(df_from_dict.loc[1]) 
    # .iloc uses integer positions
    print("\nRow at integer position 2 (Charlie):")
    print(df_from_dict.iloc[2])
    print("\nRows from index 1 to 3 (inclusive for .loc):")
    print(df_from_dict.loc[1:3])

    # Filtering Data
    print("\n--- Filtering Data ---")
    # People older than 25
    older_than_25 = df_from_dict[df_from_dict['Age'] > 25]
    print("People older than 25:")
    print(older_than_25)

    # People from New York with salary > 60000
    ny_high_earners = df_from_dict[
        (df_from_dict['City'] == 'New York') & (df_from_dict['Salary'] > 60000)
    ]
    print("\nPeople from New York earning > $60000:")
    print(ny_high_earners)

    # Adding a new column
    print("\n--- Adding a New Column ---")
    df_from_dict['Salary_Bonus'] = df_from_dict['Salary'] * 0.10
    print("DataFrame with 'Salary_Bonus' column added:")
    print(df_from_dict.head())

    # GroupBy operations (simple example)
    print("\n--- GroupBy Operations ---")
    avg_salary_by_city = df_from_dict.groupby('City')['Salary'].mean()
    print("Average salary by city:")
    print(avg_salary_by_city)

    print("\n--- Pandas Demonstration End ---")

if __name__ == "__main__":
    demonstrate_pandas_operations()
