import os


def count_files_in_path(path):
    if not os.path.exists(path):
        return "Path does not exist"

    if not os.path.isdir(path):
        return "Not a directory"

    file_count = 0

    for root, dirs, files in os.walk(path):
        file_count += len(files)

    return file_count


# Replace 'your_path_here' with the path you want to count files in
path_to_count = 'D:\\study'
result = count_files_in_path(path_to_count)

if isinstance(result, str):
    print(result)
else:
    print(f"Number of files in '{path_to_count}': {result}")
