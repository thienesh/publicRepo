import os

path_file = "c:/newfiles"

if not os.path.exists(path_file):
    os.mkdir(path_file)

for i in range(1, 11):
    file_path = os.path.join(path_file, f"file no.{i}.txt")

    with open(file_path, 'w') as f:
        f.write(f"File no.{i} for sample text file")
no_of_files_created = len(range(1, 11))
print(f"{no_of_files_created}Files created successfully")
