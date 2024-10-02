# File: file_handling_assignment.py

# File Creation: Writing to a new file
def create_file():
    try:
        # Open the file in write mode ('w')
        with open("my_file.txt", 'w') as file:
            # Write multiple lines to the file
            file.write("Hello, World!\n")
            file.write("This is line number 2.\n")
            file.write("The answer is 42.\n")
        print("File created and text written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

# File Reading and Display
def read_file():
    try:
        # Open the file in read mode ('r')
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print("File not found. Please ensure the file exists before reading.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

# File Appending: Append to the existing file
def append_file():
    try:
        # Open the file in append mode ('a')
        with open("my_file.txt", 'a') as file:
            # Append additional lines to the file
            file.write("Appending this line to the file.\n")
            file.write("Here is another appended line.\n")
            file.write("And one more for good measure.\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

# Error Handling
def main():
    try:
        create_file()      # Create and write to the file
        read_file()        # Read and display the file content
        append_file()      # Append additional content
        read_file()        # Read and display the updated file content
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File operations completed.")

# Run the main function
if __name__ == "__main__":
    main()
