import unittest
import sys
import os

# Add the parent directory (project root) to the Python path
# This allows us to import modules from the root directory (e.g., 'oop_concepts.py')
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now we can import from oop_concepts.py
# We will test the Dog class and its related functionalities.
try:
    from oop_concepts import Dog, GoldenRetriever # Assuming these classes exist
except ImportError:
    print("Error: oop_concepts.py not found or classes missing. Ensure it's in the project root.")
    # Define dummy classes if the import fails, to allow test structure to be checked,
    # but ideally, the import should work.
    class Dog:
        species = "Canis familiaris"
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def description(self): return ""
        def speak(self, sound): return ""
    class GoldenRetriever(Dog):
        def __init__(self, name, age, favorite_toy):
            super().__init__(name,age)
            self.favorite_toy = favorite_toy
        def fetch(self, item): return ""
    # In a real scenario, we would want the test to fail if the import fails.
    raise

class TestOopConcepts(unittest.TestCase):
    """
    Test cases for classes defined in oop_concepts.py.
    Focusing on the Dog and GoldenRetriever classes.
    """

    # --- Tests for Dog Class ---
    def test_dog_creation(self):
        """Test if a Dog object can be created successfully."""
        dog = Dog("Buddy", 3)
        self.assertIsNotNone(dog, "Dog object should not be None")
        self.assertIsInstance(dog, Dog, "Object should be an instance of Dog")

    def test_dog_attributes(self):
        """Test if the Dog object has the correct attributes after creation."""
        dog_name = "Rex"
        dog_age = 5
        dog = Dog(dog_name, dog_age)
        self.assertEqual(dog.name, dog_name, f"Dog name should be {dog_name}")
        self.assertEqual(dog.age, dog_age, f"Dog age should be {dog_age}")
        self.assertEqual(dog.species, "Canis familiaris", "Dog species class attribute should be 'Canis familiaris'")

    def test_dog_description_method(self):
        """Test the description method of the Dog class."""
        dog = Dog("Lucy", 4)
        expected_description = "Lucy is 4 years old."
        self.assertEqual(dog.description(), expected_description)

    def test_dog_speak_method(self):
        """Test the speak method of the Dog class."""
        dog = Dog("Max", 2)
        sound_to_make = "Woof"
        expected_output = f"Max says {sound_to_make}!"
        self.assertEqual(dog.speak(sound_to_make), expected_output)

    # --- Tests for GoldenRetriever Class (Inheritance) ---
    def test_goldenretriever_creation(self):
        """Test if a GoldenRetriever object can be created."""
        gr = GoldenRetriever("Charlie", 2, "ball")
        self.assertIsNotNone(gr, "GoldenRetriever object should not be None")
        self.assertIsInstance(gr, GoldenRetriever, "Object should be an instance of GoldenRetriever")
        self.assertIsInstance(gr, Dog, "GoldenRetriever object should also be an instance of Dog (inheritance)")

    def test_goldenretriever_attributes(self):
        """Test attributes of GoldenRetriever, including inherited ones."""
        gr_name = "Goldie"
        gr_age = 1
        gr_toy = "Frisbee"
        gr = GoldenRetriever(gr_name, gr_age, gr_toy)
        self.assertEqual(gr.name, gr_name)
        self.assertEqual(gr.age, gr_age)
        self.assertEqual(gr.favorite_toy, gr_toy, f"Favorite toy should be {gr_toy}")
        self.assertEqual(gr.species, "Canis familiaris", "Species should be inherited from Dog")

    def test_goldenretriever_fetch_method(self):
        """Test the fetch method specific to GoldenRetriever."""
        gr = GoldenRetriever("Sunny", 3, "squeaky toy")
        item_to_fetch = "stick"
        expected_output = f"Sunny fetches the {item_to_fetch}. Their favorite toy is squeaky toy."
        self.assertEqual(gr.fetch(item_to_fetch), expected_output)

    def test_goldenretriever_speak_method_overridden(self):
        """Test the overridden speak method in GoldenRetriever."""
        gr = GoldenRetriever("Rocky", 4, "rope")
        # Default sound for GoldenRetriever's overridden speak method
        expected_output_default = "Rocky (a Golden Retriever) enthusiastically says Bark!"
        self.assertEqual(gr.speak(), expected_output_default)
        # Specific sound
        sound_to_make = "Awooo"
        expected_output_specific = f"Rocky (a Golden Retriever) enthusiastically says {sound_to_make}!"
        self.assertEqual(gr.speak(sound_to_make), expected_output_specific)


if __name__ == '__main__':
    """
    Allows running the tests directly from the command line.
    """
    unittest.main()
