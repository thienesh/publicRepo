
import subprocess

cmd = "wmic logicaldisk get deviceid, freespace, size"

result = subprocess.run(cmd,shell=True)

if result.returncode == 0:
    print("Executed")
else:
    print("Not executed")

# print(f"output : {result}")
# print(f"output is : {result.returncode}")



# print(f"output : {result}")
# print(f"output from popen : {len(result.readlines())}")
