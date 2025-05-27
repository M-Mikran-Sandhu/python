# Python Learning Scripts

A curated collection of Python scripts designed for beginners and intermediate learners to grasp various Python concepts. Each script includes detailed comments and explanations.

## How to Use This Repository

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url> # Replace <repository_url> with the actual URL
    cd <repository_directory>
    ```
2.  **Ensure Python is Installed:** Download Python from [python.org](https://www.python.org/downloads/) if you haven't already.
3.  **Install Dependencies:**
    Some scripts require external libraries. The `requirements.txt` file lists all major dependencies for this repository, including those for the HTML index generator, general utility scripts, and the new advanced examples (TensorFlow for AI, SQLAlchemy for database, Requests/BeautifulSoup4 for web tasks, NumPy for numerical computing, Pandas for data manipulation, Matplotlib for plotting, Pillow for image processing).
    Install them using:
    ```bash
    pip install -r requirements.txt 
    ```
    For individual scripts, if you encounter an `ImportError` and haven't run the command above, you might need to install specific libraries (e.g., `pip install tensorflow sqlalchemy requests beautifulsoup4 numpy pandas matplotlib Pillow`).
4.  **Browse Scripts via HTML Index:**
    Open the `index.html` file (located in the root of this repository) in your web browser for a categorized view of all scripts with syntax highlighting. This is often the easiest way to explore the code. If `index.html` is not present or outdated, you can generate it using the instructions in the 'Generating the HTML Index Page' section below.

5.  **Run Individual Scripts:**
    Most scripts are self-contained. Navigate to the repository's root directory and run them using:
    ```bash
    python script_name.py
    ```
    For example, to run the BMI calculator:
    ```bash
    python "BMI conditional.py"
    ```
    (Note: Some filenames contain spaces. Using quotes around the filename is a good practice if so.)

    For the custom module example, navigate into its directory:
    ```bash
    cd custom_module_example
    python main.py
    cd ..
    ```

## Generating the HTML Index Page

This repository includes a script `generate_html_index.py` that creates an `index.html` file, providing a browsable interface with syntax-highlighted code for all Python scripts.

To generate or update `index.html`:

1.  **Install Dependencies for the Generator:**
    The `generate_html_index.py` script requires the `Pygments` library. Ensure it's installed. You can install all necessary dependencies listed in `requirements.txt` by running:
    ```bash
    pip install -r requirements.txt
    ```
    Alternatively, install `Pygments` directly:
    ```bash
    pip install Pygments
    ```
2.  **Run the Generator Script:**
    From the root directory of the repository:
    ```bash
    python generate_html_index.py
    ```
    This will create or overwrite the `index.html` file in the root directory. Open this file in a web browser to view the scripts.

## Topics Covered

### 1. Python Fundamentals
*   `first python.py`: Basic syntax, print statements.
*   `data type str.py`: String operations and methods.
*   `km to miles.py`: Simple numerical conversion.
*   `area of a circle.py`: Using the `math` module.
*   `This program calculates the average of two numbers.py`: Basic arithmetic.
*   `input to give average.py`: User input and calculations.
*   `age using boolean.py`: Boolean logic with age checks.
*   `boolean fucntion.py`: Defining functions that return booleans.
*   `if elif else.py`: Conditional statements.
*   `BMI conditional.py`: Practical example of conditionals (BMI calculation). (Error corrected)
*   `AND OR to get fail and approved.py`: Logical operators in conditionals. (Improved)
*   `for loop.py`: `for` loops.
*   `while.py`: `while` loops.
*   `exercise of loop.py`: Loop-based exercises.
*   `searching using loop.py`: Searching elements in a list using loops.
*   `color game using loop.py`: A simple game using loops.
*   `guess game using while.py`: Guessing game with `while` loop.
*   `functions.py`: Defining and using functions. (Refactored)
*   `Error handling.py`: Basic `try-except` blocks.
*   `exersice using error handling.py`: Exercises on error handling.
*   `data validation.py`: Input validation techniques.

### 2. Data Structures
*   `list add.py`: List operations (adding elements).
*   `Using tuple find month.py`: Basic tuple usage.
*   `dictionares of information.py`: Dictionary basics.
*   `advanced_data_structures.py`: In-depth look at Sets, Tuples (including `namedtuple`), and Dictionaries (comprehensions, `get()`, `setdefault()`).
*   `list_comprehensions.py`: Concise list creation using comprehensions.

### 3. Advanced Python Concepts
*   `oop_concepts.py`: Object-Oriented Programming (Classes, Objects, Inheritance, Encapsulation, Polymorphism).
*   `file_operations.py`: Reading from and writing to files (text, CSV, JSON).
*   `lambda_functions.py`: Creating small, anonymous functions.
*   `custom_module_example/`: Directory demonstrating how to create and use custom modules.
    *   `custom_module_example/my_module.py`: The example module.
    *   `custom_module_example/main.py`: Script importing and using `my_module.py`.
*   `advanced_error_handling.py`: Advanced techniques like specific exceptions, `else`, `finally`, and custom exceptions.

### 4. Libraries & External Modules
*   `json pprint.py`: Pretty-printing JSON data.
*   `exercise json and request exercise.py`: Using `json` and `requests` libraries.
*   `requests.py`: Making HTTP requests (basic example).
*   `matplotlib.py`: Basic plotting with Matplotlib.
*   `plot.py`: More plotting examples.
*   `time.py`: Using the `time` module (e.g., for delays).
*   `time and pyplot exercise.py`: Exercise combining `time` and `matplotlib`.

### 5. Miscellaneous
*   `CHATGPT.py`: (Purpose unclear from name - to be reviewed)
*   `Exercise no 1.py`, `Exercise no 2.py`: General exercises.

## Advanced Library Examples

This section highlights examples using powerful external libraries for specific tasks. Make sure you have installed the necessary dependencies from `requirements.txt` before running these.

### a. AI with TensorFlow (`ai_example.py`)
*   **Library:** [TensorFlow](https://www.tensorflow.org/)
*   **Purpose:** A comprehensive open-source platform for machine learning and artificial intelligence.
*   **Example (`ai_example.py`):** Demonstrates basic TensorFlow setup, tensor creation, a simple arithmetic operation, and a minimal neural network layer using Keras. This script verifies that TensorFlow can be imported and run.
*   **To Run:** `python ai_example.py`

### b. Database Interaction with SQLAlchemy (`database_example.py`)
*   **Library:** [SQLAlchemy](https://www.sqlalchemy.org/)
*   **Purpose:** A SQL toolkit and Object-Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.
*   **Example (`database_example.py`):** Shows how to set up an in-memory SQLite database, define a `User` model, create the corresponding table, and perform basic CRUD (Create, Read, Update, Delete) operations.
*   **To Run:** `python database_example.py`

### c. Web Interaction with Requests and BeautifulSoup (`web_search_example.py`)
*   **Libraries:** 
    *   [Requests](https://requests.readthedocs.io/): An elegant and simple HTTP library for Python.
    *   [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): A library for pulling data out of HTML and XML files.
*   **Purpose:** Used together for fetching web pages (Requests) and parsing their content (BeautifulSoup).
*   **Example (`web_search_example.py`):** Provides a function to perform a Google search for a given term and attempts to extract the title of the search results page. 
    *Note: This example is for illustrative purposes and may be rate-limited or blocked by Google if used excessively. Always respect website terms of service.*
*   **To Run:** `python web_search_example.py`

### d. Numerical Computing with NumPy (`numpy_example.py`)
*   **Library:** [NumPy](https://numpy.org/)
*   **Purpose:** The fundamental package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.
*   **Example (`numpy_example.py`):** Demonstrates creating NumPy arrays, array reshaping, slicing, performing various mathematical operations (element-wise, dot product), and calculating aggregate statistics (sum, min, max, mean).
*   **To Run:** `python numpy_example.py`

### e. Data Manipulation with Pandas (`pandas_example.py`)
*   **Library:** [Pandas](https://pandas.pydata.org/)
*   **Purpose:** A powerful and easy-to-use open-source data analysis and manipulation tool, built on top of Python. It provides data structures like Series (1D) and DataFrame (2D) for handling structured data.
*   **Example (`pandas_example.py`):** Shows how to create DataFrames (from dictionaries and NumPy arrays), inspect data (`head`, `info`, `describe`), select columns and rows (`loc`, `iloc`), filter data based on conditions, add new columns, and perform simple `groupby` operations.
*   **To Run:** `python pandas_example.py`

### f. Data Visualization with Matplotlib (`matplotlib_example.py`)
*   **Library:** [Matplotlib](https://matplotlib.org/)
*   **Purpose:** A comprehensive library for creating static, animated, and interactive visualizations in Python. It can produce plots, histograms, power spectra, bar charts, error charts, scatterplots, etc., with just a few lines of code.
*   **Example (`matplotlib_example.py`):** Demonstrates how to create basic plots: a line plot, a bar chart, and a scatter plot using sample data (generated with NumPy). The script saves these plots as PNG image files (`line_plot_example.png`, `bar_chart_example.png`, `scatter_plot_example.png`) in the repository's root directory.
*   **To Run:** `python matplotlib_example.py` (This will generate image files, not display plots directly unless modified).

### g. Image Processing with Pillow (`image_processing_example.py`)
*   **Library:** [Pillow (PIL Fork)](https://pillow.readthedocs.io/)
*   **Purpose:** A powerful yet easy-to-use library for opening, manipulating, and saving many different image file formats. It is a fork of the Python Imaging Library (PIL).
*   **Example (`image_processing_example.py`):** 
    1.  First, the script generates a simple sample image (`sample_generated_image.png`) using Matplotlib.
    2.  Then, it uses Pillow to open this image and perform several operations: displaying image info, converting to grayscale, resizing, rotating, and applying a blur filter. 
    3.  The modified images are saved with descriptive names (e.g., `grayscale_example.png`, `resized_example.png`).
*   **To Run:** `python image_processing_example.py` (This will generate/overwrite image files in the root directory).

## Contributing
Contributions are welcome! If you have new scripts, improvements, or bug fixes:
1.  Fork the repository.
2.  Create a new branch for your feature or fix.
3.  Make your changes, ensuring code is well-commented for beginners.
4.  If adding a new concept, try to follow the existing style of explanation.
5.  Submit a pull request.

## Roadmap
This repository aims to continuously expand its collection of Python learning scripts. Future additions may include:
*   **More on OOP:** Design patterns, abstract base classes.
*   **Standard Library Deep Dives:** `collections`, `itertools`, `datetime`, `os`, `sys`.
*   **Web Scraping:** Using libraries like Beautiful Soup and Scrapy.
*   **API Interaction:** More complex examples of working with external APIs.
*   **Basic Data Analysis:** Introduction to libraries like NumPy and Pandas.
*   **GUI Development:** Simple GUI applications using Tkinter or PyQt.
*   **Database Interaction:** Using `sqlite3` or ORMs.
*   **Unit Testing:** More comprehensive examples using `unittest` or `pytest`.
*   **Concurrency:** Threads and asynchronous programming.
*   **Best Practices:** More on PEP 8, virtual environments, project structure.
*   **Review and Refactor Existing Scripts:** Standardize file naming (e.g., `snake_case.py`) and further improve comments and clarity across all files.

Feel free to suggest new topics or areas of focus!

Happy coding!
```
