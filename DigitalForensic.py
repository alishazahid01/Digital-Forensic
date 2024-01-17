# Digital Forensic
import pytsk3

# Decorator 
def print_message(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"{func.__name__} completed.")
        return result
    return wrapper

# Function for opening image and creating file system
@print_message
def review_image(image_path):
    # open image
    image = pytsk3.Img_Info(image_path)

    # TSK (The Sleuth Kit) file system for digital forensic analysis
    file_system = pytsk3.FS_Info(image)

    checking_dir(image, file_system)

# Function for performing digital Forensic 
@print_message
def checking_dir(image, file_system):
    # Traverse the file system
    for directory in file_system.open_dir(path="/"):
        print(f"Directory: {directory.info.name.name.decode()}")

        # List files in the current directory
        for f in directory:
            # Skip "."(Current), ".."(Parent) and deleted files
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

    close_image(image)

# Function for closing image
@print_message
def close_image(image):
    # Close the image
    image.close()

# Main
if __name__ == "__main__":
    # Prompt user to enter the image file path
    image_path = input("Enter the image path: ")
    review_image(image_path)
