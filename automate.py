import os
import shutil

# Define source and destination directories
from_dir = "C:\\Users\\Shubh\\Downloads"
to_dir = "C:\\Users\\Shubh\\Organized_Files"


# List of document file extensions to check
doc_extensions = ['.txt', '.doc', '.docx', '.pdf']

# Get the list of files in the source directory
files = os.listdir(from_dir)

# Iterate over each file in the source directory
for file_name in files:
    # Get the file extension
    file_extension = os.path.splitext(file_name)[1]

    # Check if the extension is blank
    if file_extension == '':
        continue

    # Check if the file extension is one of the document extensions
    if file_extension in doc_extensions:
        # Create the source path
        path1 = os.path.join(from_dir, file_name)
        
        # Create the destination directory path
        path2 = os.path.join(to_dir, "Document_Files")
        
        # Create the full destination path
        path3 = os.path.join(path2, file_name)
        
        # Check if the destination directory exists
        if not os.path.exists(path2):
            # Create the destination directory
            os.makedirs(path2)
            print(f"Creating directory: {path2}")

        # Move the file
        print(f"Moving {file_name} to {path3}")
        shutil.move(path1, path3)
