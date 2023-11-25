'''
Creating a directory if it does not exist.

Creating 1000 text files in the directory with names "File 1.txt", "File 2.txt", etc.

Renaming each file to "Modifiedfile 1.txt", "Modifiedfile 2.txt", etc.

Removing all files in the directory.

Prints a message to confirm that the files have been removed successfully.
'''

import os

directory = "c:/files"

if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1, 1001):
    file_path = os.path.join(directory, f"File {i}.txt")
    with open(file_path, 'w') as f:
        f.write(f"This file is \ncreated for \nfile no.{i}")

# Renaming the file
for i in range(1, 1001):
    old_file_path = os.path.join(directory, f"File {i}.txt")
    new_file_path = os.path.join(directory, f"Modifiedfile {i}.txt")
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)

# Remove all files in the directory
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    os.remove(file_path)

print("Files removed successfully!")
