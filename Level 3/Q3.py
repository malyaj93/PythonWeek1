import os

def JtoI(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()

        # Replace all occurrences of 'J' with 'I'
        corrected_content = content.replace('J', 'I')

        # Display the corrected content
        print("Corrected content of the file:")
        print(corrected_content)
    else:
        print(f"File not found at path: {file_path}")

folder_path = './resources/'
file_name = 'words.txt'

file_path = os.path.join(folder_path, file_name)

# Call the JtoI function to replace 'J' with 'I' and display the corrected content
JtoI(file_path)