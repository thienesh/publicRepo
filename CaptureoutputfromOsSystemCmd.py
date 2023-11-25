import os

cmd1 = "dir"

result = os.popen(cmd1)
print(f"output : {result}")
print(f"output from popen : {len(result.readlines())}")
