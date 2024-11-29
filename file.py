
def read_file(filename):
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        print("File read successfully!")
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return None

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Modified content written to '{filename}' successfully!")
    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")
def modify_content(content):
    # Example modification: convert text to uppercase
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")
    
    # Read the file content
    content = read_file(filename)
    
    if content is not None:
        # Modify the content
        modified_content = modify_content(content)
        
        # Write the modified content to a new file
        new_filename = "modified_" + filename
        write_file(new_filename, modified_content)

if __name__ == "__main__":
    main()
