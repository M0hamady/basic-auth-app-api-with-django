import os
from tkinter import Tk, filedialog
from PIL import Image

# Function to select folder and minimize image quality
def minimize_images_quality():
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    # Ask the user to select a folder
    folder_path = filedialog.askdirectory(title="Select Images Folder")

    if not folder_path:
        print("No folder selected. Exiting.")
        return

    # Iterate through the folder and process each image
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff')):
            try:
                # Open the image
                with Image.open(file_path) as img:
                    # Set the image quality (lower value = higher compression, worse quality)
                    quality = 10  # You can experiment with this value (from 1 to 100)

                    # Save the image with reduced quality
                    img.save(file_path, quality=quality)
                    print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Run the function
minimize_images_quality()
