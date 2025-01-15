import os
import re
import random
import tkinter as tk
from tkinter import filedialog, messagebox

# List of random names to use if the image name is only numbers
random_names = [
    "sunrise", "oceanWave", "mountainView", "forestPath", 
    "desertSky", "cityLights", "riverFlow", "gardenBloom", 
    "cloudMist", "fireSpark", "iceCrystal", "windBreeze"
]

def sanitize_name(name):
    """
    Sanitize the image name to be a valid JavaScript/TypeScript identifier.
    - Replace invalid characters with underscores.
    - Use a random name if the image name is only numbers.
    """
    base_name = os.path.splitext(name)[0]  # Remove the file extension
    
    # Check if the name is entirely numeric
    if base_name.isdigit():
        return random.choice(random_names)
    
    # Replace invalid characters with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9_]', '_', base_name)
    
    # Ensure the name starts with a letter or underscore
    if not sanitized[0].isalpha() and sanitized[0] != '_':
        sanitized = '_' + sanitized
    
    return sanitized

def create_ts_file(folder_path):
    image_extensions = (".png", ".jpg", ".jpeg", ".gif")
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    
    if not image_files:
        messagebox.showinfo("No Images Found", "No image files found in the selected folder.")
        return
    
    export_lines = [
        f"export {{ default as {sanitize_name(image)} }} from './{image}';"
        for image in image_files
    ]
    
    ts_file_path = os.path.join(folder_path, "images.ts")
    with open(ts_file_path, "w") as ts_file:
        ts_file.write("\n".join(export_lines))
    
    messagebox.showinfo("Export Complete", f"'images.ts' created successfully at {folder_path}.")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        create_ts_file(folder_path)

# Tkinter GUI setup
root = tk.Tk()
root.title("Image Exporter")
root.geometry("400x200")

select_button = tk.Button(root, text="Select Folder", command=select_folder, padx=20, pady=10)
select_button.pack(expand=True)

root.mainloop()
