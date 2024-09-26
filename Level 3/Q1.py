import os

# Specify the folder and file name
folder_path = './resources/'
file_name = 'doc.txt'

file_path = os.path.join(folder_path, file_name)

# Check if the file exists
if os.path.exists(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    words = content.split()

    # Filter out words with even length
    even_length_words = [word for word in words if len(word) % 2 == 0]

    result = ' '.join(even_length_words)

    print(result)
else:
    print(f"File '{file_name}' not found in folder '{folder_path}'")