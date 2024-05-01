import os
from PIL import Image
from pillow_heif import register_heif_opener

def heic_to_jpg(heic_file_path):
    try:
        register_heif_opener()

        # Open the HEIC file
        with Image.open(heic_file_path) as img:
            # Get the base file name without extension
            base_filename = os.path.splitext(heic_file_path)[0]
            # Convert and save as JPEG
            img.convert('RGB').save(base_filename + '.jpeg', 'JPEG')
        print("Image saved successfully ...")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    # Get the current directory
    current_directory = os.getcwd()
    # List all files in the directory
    files = os.listdir(current_directory)
    # Filter HEIC files
    heic_files = [file for file in files if file.lower().endswith('.heic')]
    if not heic_files:
        print("No HEIC files found in the current directory.")
        return

    for heic_file in heic_files:
        heic_to_jpg(heic_file)

if __name__ == "__main__":
    main()
