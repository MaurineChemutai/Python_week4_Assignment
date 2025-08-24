#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# File Read & Write Challenge with Error Handling

def modify_content(line):
    """
    Example modification function:
    Converts text to uppercase and adds a line number.
    """
    return line.upper()

def main():
    # Ask user for the input filename
    input_file = input("Enter the name of the file to read: ")

    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Modify the content
        modified_lines = []
        for i, line in enumerate(lines, start=1):
            modified_line = f"{i}: {modify_content(line)}"
            modified_lines.append(modified_line)
        
        # Ask for output filename
        output_file = input("Enter the name of the new file to write to: ")

        # Write modified content to new file
        with open(output_file, 'w') as file:
            file.writelines(modified_lines)

        print(f"Modified content has been written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


# In[ ]:




