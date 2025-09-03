# Robust File Read & Write with Error Handling

def modify_content(content):
    """
    Example modification function.
    You can change this to anything (e.g., lowercase, add line numbers, etc.)
    """
    return content.upper()  # Converts text to uppercase

def main():
    # Ask the user for the filename
    filename = input("Enter the filename to read: ")

    try:
        # Read the original file
        with open(filename, "r") as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Create a new filename for the modified file
        new_filename = "modified_" + filename

        # Write the modified content to the new file
        with open(new_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Success! Modified content saved to '{new_filename}' ✅")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist! ❌")
    except PermissionError:
        print(f"Error: You do not have permission to read/write '{filename}'! 🚫")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
