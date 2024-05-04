import os
from PIL import Image

class ImageConverter:
    def __init__(self):
        self.input_folder = ""
        self.output_folder = ""

    def set_input_folder(self, input_folder):
        self.input_folder = input_folder

    def set_output_folder(self, output_folder):
        self.output_folder = output_folder

    def convert_images(self):
        if self.input_folder and self.output_folder:
            # Create output subfolder
            output_subfolder = os.path.join(self.output_folder, f"output_{os.path.basename(self.input_folder)}")
            os.makedirs(output_subfolder, exist_ok=True)
            
            # Call the recursive function to convert images in all subfolders
            self.convert_images_in_folder(self.input_folder, output_subfolder)
            print("Conversion complete.")
        else:
            print("Please select input and output folders.")

    def convert_images_in_folder(self, input_folder, output_folder):
        # Loop through all files and subdirectories in the input folder
        for root, dirs, files in os.walk(input_folder):
            # Get the relative path from the input folder to maintain folder structure
            relative_path = os.path.relpath(root, input_folder)
            output_subfolder = os.path.join(output_folder, relative_path)
            os.makedirs(output_subfolder, exist_ok=True)

            for file_name in files:
                input_path = os.path.join(root, file_name)
                
                # Check if the file is an image (JPEG, PNG, JPG)
                if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                    # Open the image
                    with Image.open(input_path) as img:
                        # Convert to WebP format
                        output_path = os.path.join(output_subfolder, file_name.replace('.jpg', '.webp').replace('.jpeg', '.webp').replace('.png', '.webp'))
                        img.save(output_path, 'webp', quality=80)  # Adjust quality as needed
                        print(f"Converted {input_path} to WebP format and saved at {output_path}")
