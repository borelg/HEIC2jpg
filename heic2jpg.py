import os
from wand.image import Image

def convert_heic_to_jpg(heic_path, jpg_path):
    """Convert HEIC file to JPG."""
    with Image(filename=heic_path) as img:
        img.format = 'jpeg'
        img.save(filename=jpg_path)

def main():
    # Create 'jpgs' directory if it doesn't exist
    if not os.path.exists('jpgs'):
        os.makedirs('jpgs')

    # Loop through all files in the current directory
    for filename in os.listdir('.'):
        if filename.lower().endswith('.heic'):
            # Construct the full file path
            heic_path = os.path.join('.', filename)
            jpg_path = os.path.join('jpgs', filename.lower().replace('.heic', '.jpg'))

            # Convert the image
            convert_heic_to_jpg(heic_path, jpg_path)
            print(f"Converted {filename} to JPG.")

if __name__ == "__main__":
    main()
