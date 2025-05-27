import cv2
import numpy as np
import os # To check if the sample image exists

# --- Helper function to ensure sample image exists ---
# (Re-using a simplified version of the image creation from Pillow example if needed,
#  or just checking for the one created by image_processing_example.py)
import matplotlib.pyplot as plt # For creating a sample if it doesn't exist

def ensure_sample_image_exists(filename="sample_generated_image.png"):
    """Checks if the sample image exists, if not, creates it."""
    if os.path.exists(filename):
        print(f"Sample image '{filename}' found.")
        return filename
    else:
        print(f"Sample image '{filename}' not found. Attempting to create a new one...")
        try:
            fig, ax = plt.subplots(figsize=(2, 2))
            square = plt.Rectangle((0,0), 1, 1, color="lightgreen") # Different color for clarity
            ax.add_patch(square)
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            plt.savefig(filename)
            plt.close(fig)
            print(f"New sample image created as '{filename}'.")
            return filename
        except Exception as e:
            print(f"Error creating sample image for OpenCV: {e}")
            return None


def demonstrate_opencv_operations(image_path):
    """Demonstrates some basic OpenCV (cv2) operations."""

    if not image_path:
        print("No image path provided for OpenCV operations.")
        return

    print(f"\n--- OpenCV (cv2) Demonstration on '{image_path}' ---")

    # 1. Read an image
    # cv2.imread() returns a NumPy array.
    # By default, it reads in BGR format (Blue, Green, Red).
    img_bgr = cv2.imread(image_path)

    if img_bgr is None:
        print(f"Error: Could not read image from '{image_path}'. Check the file path and integrity.")
        return

    print(f"Image loaded successfully. Shape: {img_bgr.shape} (Height, Width, Channels)")
    # cv2.imshow("Original BGR Image", img_bgr) # cv2.imshow needs a GUI backend
    # cv2.waitKey(0) # Waits for a key press
    # cv2.destroyAllWindows() # Closes image windows
    # Note: cv2.imshow might not work in all environments (e.g., headless servers, some notebooks).
    # We will focus on processing and saving images.

    # 2. Convert color space (BGR to Grayscale and BGR to HSV)
    print("\nConverting color spaces...")
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    gray_filename = "opencv_grayscale_example.png"
    cv2.imwrite(gray_filename, img_gray)
    print(f"Grayscale image saved as '{gray_filename}'")

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    hsv_filename = "opencv_hsv_example.png"
    cv2.imwrite(hsv_filename, img_hsv)
    print(f"HSV image saved as '{hsv_filename}'")

    # 3. Applying a blur (Gaussian Blur)
    print("\nApplying Gaussian Blur...")
    blurred_img = cv2.GaussianBlur(img_bgr, (5, 5), 0) # Kernel size (5,5), sigmaX=0
    blurred_filename = "opencv_blurred_example.png"
    cv2.imwrite(blurred_filename, blurred_img)
    print(f"Blurred image saved as '{blurred_filename}'")

    # 4. Edge Detection (Canny edge detector)
    # Often applied on a grayscale image for better results.
    print("\nDetecting edges using Canny detector...")
    edges = cv2.Canny(img_gray, threshold1=100, threshold2=200) # Adjust thresholds as needed
    edges_filename = "opencv_edges_example.png"
    cv2.imwrite(edges_filename, edges)
    print(f"Edge-detected image saved as '{edges_filename}'")

    # 5. Drawing on an image (e.g., a rectangle)
    # Let's draw on a copy of the original image
    img_with_rect = img_bgr.copy()
    # Define rectangle parameters: top-left corner (x,y), bottom-right corner (x,y)
    # Let's draw a rectangle in the center
    h, w = img_with_rect.shape[:2]
    pt1 = (w // 4, h // 4)
    pt2 = (w * 3 // 4, h * 3 // 4)
    color = (0, 255, 0) # Green color in BGR
    thickness = 2
    cv2.rectangle(img_with_rect, pt1, pt2, color, thickness)
    rect_filename = "opencv_rectangle_example.png"
    cv2.imwrite(rect_filename, img_with_rect)
    print(f"Image with a rectangle drawn saved as '{rect_filename}'")


    print("\n--- OpenCV (cv2) Demonstration End ---")
    print("Note: Processed images have been saved in the root directory.")
    print("Displaying images with cv2.imshow() is commented out as it requires a GUI environment.")

if __name__ == "__main__":
    # Ensure the sample image (used by Pillow example) exists or create one
    sample_image_file = ensure_sample_image_exists()

    if sample_image_file:
        demonstrate_opencv_operations(sample_image_file)
    else:
        print("Skipping OpenCV demonstration due to error with sample image.")
