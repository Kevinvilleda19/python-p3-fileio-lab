from pathlib import Path

def write_file(file_name, file_content):
    # Convert file_name to a string if it's a Path object
    file_name = str(file_name)

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Open the file in write mode and write the content
    with open(file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Convert file_name to a string if it's a Path object
    file_name = str(file_name)

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Open the file in append mode and append the content
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Convert file_name to a string if it's a Path object
    file_name = str(file_name)

    # Ensure the file has a .txt extension
    if not file_name.endswith(".txt"):
        file_name += ".txt"

    # Open the file in read mode and return its content
    if Path(file_name).exists():
        with open(file_name, 'r') as file:
            return file.read()
    else:
        return None  # Return None if the file doesn't exist
