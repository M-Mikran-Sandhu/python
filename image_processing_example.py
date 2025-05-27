import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter, UnidentifiedImageError

def create_sample_image(filename="sample_generated_image.png"):
    """Creates a simple image using Matplotlib and saves it."""
    try:
        fig, ax = plt.subplots(figsize=(2, 2)) # Small figure
        square = plt.Rectangle((0,0), 1, 1, color="skyblue")
        ax.add_patch(square)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off') # Turn off axis numbers and ticks
        plt.savefig(filename)
        plt.close(fig)
        print(f"Sample image saved as {filename}")
        return filename
    except Exception as e:
        print(f"Error creating sample image: {e}")
        return None

def demonstrate_pillow_operations(image_path):
    """Demonstrates some basic Pillow (PIL) operations on the given image path."""

    if not image_path:
        print("No image path provided for Pillow operations.")
        return

    print(f"\n--- Pillow Image Processing Demonstration on '{image_path}' ---")
    try:
        # Open the image
        img = Image.open(image_path)
        print(f"Opened image: {image_path}")

        # 1. Display basic image information
        print(f"Format: {img.format}, Size: {img.size}, Mode: {img.mode}")

        # 2a. Convert to grayscale
        grayscale_img = img.convert("L")
        grayscale_filename = "grayscale_example.png"
        grayscale_img.save(grayscale_filename)
        print(f"Grayscale version saved as {grayscale_filename}")

        # 2b. Resize the image
        resized_img = img.resize((img.width // 2, img.height // 2)) # Half size
        resized_filename = "resized_example.png"
        resized_img.save(resized_filename)
        print(f"Resized version (half size) saved as {resized_filename}")

        # 2c. Rotate the image
        rotated_img = img.rotate(45) # Rotate 45 degrees
        rotated_filename = "rotated_example.png"
        rotated_img.save(rotated_filename)
        print(f"Rotated version (45 degrees) saved as {rotated_filename}")
        
        # Example of a simple filter
        blurred_img = img.filter(ImageFilter.BLUR)
        blurred_filename = "blurred_example.png"
        blurred_img.save(blurred_filename)
        print(f"Blurred version saved as {blurred_filename}")

        img.close() # Close the original image

    except FileNotFoundError:
        print(f"Error: The image file '{image_path}' was not found.")
    except UnidentifiedImageError:
        print(f"Error: Pillow cannot identify or open the image file '{image_path}'.")
    except Exception as e:
        print(f"An error occurred during Pillow operations: {e}")

    print("\n--- Pillow Demonstration End ---")
    print("Note: Processed images have been saved in the root directory.")


if __name__ == "__main__":
    # First, create the sample image
    sample_image_file = create_sample_image()
    
    # Then, process it with Pillow
    if sample_image_file:
        demonstrate_pillow_operations(sample_image_file)
    else:
        print("Skipping Pillow demonstration due to error in sample image creation.")
