import unittest
import sys
import os

# Add the parent directory (project root) to the Python path
# This allows us to import modules from the root directory (e.g., 'functions.py')
# when running tests from the 'tests' subdirectory.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now we can import from functions.py
# If functions.py is not found, it might indicate the script is not being run from the correct context,
# or that functions.py is missing from the root of the project.
try:
    from functions import fahrtocelsius, say_hello_simple, say_hello_adv
except ImportError:
    print("Error: functions.py not found. Ensure it's in the project root and sys.path is correct.")
    # As a fallback for environments where path manipulation might be tricky,
    # one could define dummy functions here, but the goal is to test the actual functions.
    # For now, we'll let the ImportError halt if it occurs, as it's a setup issue.
    raise

class TestFunctions(unittest.TestCase):
    """
    Test cases for the functions defined in functions.py.
    """

    # --- Tests for fahrtocelsius ---
    def test_fahrtocelsius_freezing_point(self):
        """Test fahrtocelsius with the freezing point of water (32 F = 0 C)."""
        self.assertEqual(fahrtocelsius(32), 0)

    def test_fahrtocelsius_boiling_point(self):
        """Test fahrtocelsius with the boiling point of water (212 F = 100 C)."""
        self.assertEqual(fahrtocelsius(212), 100)

    def test_fahrtocelsius_negative_value(self):
        """Test fahrtocelsius with a common negative value (-40 F = -40 C)."""
        self.assertEqual(fahrtocelsius(-40), -40)

    def test_fahrtocelsius_other_value(self):
        """Test fahrtocelsius with another arbitrary value (e.g., 50 F = 10 C)."""
        self.assertEqual(fahrtocelsius(50), 10)

    # --- Tests for say_hello_simple ---
    # These tests assume say_hello_simple has been refactored to RETURN a string.
    def test_say_hello_simple_with_name(self):
        """Test say_hello_simple with a typical name."""
        expected_output = "Hello Alice, How are you"
        self.assertEqual(say_hello_simple("Alice"), expected_output)

    def test_say_hello_simple_empty_string(self):
        """Test say_hello_simple with an empty string as name."""
        expected_output = "Hello , How are you"
        self.assertEqual(say_hello_simple(""), expected_output)

    # --- Tests for say_hello_adv ---
    # These tests assume say_hello_adv has been refactored to RETURN a string.
    def test_say_hello_adv_one_argument(self):
        """Test say_hello_adv with only the first argument (person2 should use default)."""
        expected_output = "Hello Bob, How are you? And hello to mafia!"
        self.assertEqual(say_hello_adv("Bob"), expected_output)

    def test_say_hello_adv_two_arguments(self):
        """Test say_hello_adv with both arguments provided."""
        expected_output = "Hello Charlie, How are you? And hello to friend!"
        self.assertEqual(say_hello_adv("Charlie", "friend"), expected_output)

    def test_say_hello_adv_two_arguments_one_empty(self):
        """Test say_hello_adv with the second argument being an empty string."""
        expected_output = "Hello Dave, How are you? And hello to !"
        self.assertEqual(say_hello_adv("Dave", ""), expected_output)

if __name__ == '__main__':
    """
    This allows the test script to be run directly from the command line.
    `unittest.main()` will discover and run all tests in this file.
    """
    unittest.main()
