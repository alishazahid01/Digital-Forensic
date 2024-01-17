Digital Forensic Toolkit
Introduction

This toolkit provides a set of Python functions for conducting digital forensic analysis on disk images. It leverages the pytsk3 library, which is a Python binding for The Sleuth Kit (TSK), a popular open-source library for forensic analysis. The toolkit includes functions for opening an image, traversing the file system, examining files, and closing the image.
Getting Started

To use this toolkit, follow these steps:

    Ensure you have Python installed on your system.
    Install the pytsk3 library using the following command:

    pip install pytsk3

    Clone or download this repository to your local machine.

Code Structure

The toolkit consists of the following components:
1. Opening an Image


# Function for opening image and creating a file system
@print_message
def review_image(image_path):
    # Open image
    image = pytsk3.Img_Info(image_path)

    # TSK (The Sleuth Kit) file system for digital forensic analysis
    file_system = pytsk3.FS_Info(image)

    checking_dir(image, file_system)

This function opens a disk image and creates a file system object for analysis.
2. Traversing the File System


# Function for performing digital forensic
@print_message
def checking_dir(image, file_system):
    # Traverse the file system
    for directory in file_system.open_dir(path="/"):
        print(f"Directory: {directory.info.name.name.decode()}")

        # List files in the current directory
        for f in directory:
            # Skip "."(Current), ".."(Parent), and deleted files
            try:
                if f.info.name.name.decode() not in [".", ".."] and not f.info.meta.is_allocated():
                    print(f"File: {f.info.name.name.decode()}")
                    print(f"File size: {f.info.meta.size}")

                    # Extract file content
                    file_content = f.read_random(0, f.info.meta.size)
                    print(f"File content: {file_content.decode()}")
                    print("--------------")

            except Exception as e:
                print(f"Error occurred while opening the file: {str(e)}")

This function iterates through the file system, listing directories and examining files. It also extracts and prints the content of non-deleted files.
3. Closing the Image


# Function for closing the image
@print_message
def close_image(image):
    # Close the image
    image.close()

This function is responsible for closing the opened disk image when analysis is completed.
4. Decorator for Logging



# Decorator for logging function calls
def print_message(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper

A decorator function is used to log the entry and exit of each function call in the toolkit.
Usage

To run the digital forensic toolkit, execute the following steps:

    Run the main script by executing it in your terminal or code editor:


    python forensic_toolkit.py

    Enter the path to the disk image you want to analyze when prompted.

    The toolkit will open the image, traverse the file system, and provide information about directories and files within the image.

Conclusion

This documentation provides an overview of the Digital Forensic Toolkit, which enables the analysis of disk images for forensic purposes. It includes functions for opening an image, navigating the file system, and examining file content. Users can customize and extend this toolkit for specific forensic analysis needs.
