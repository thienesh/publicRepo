import os

directory = "c:/python files"

if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1,11):
    file_path = os.path.join(directory,f"python program {i}.py")
    with open(file_path,'w') as f:
        f.write(f"This file is created for python program no.{i}")