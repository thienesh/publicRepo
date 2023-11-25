import os
import subprocess

cmd = "wmic logicaldisk get deviceid, freespace, size"
f_out = open("c:/output file.txt",'w')

result = subprocess.run(cmd,shell=True,stdout=f_out)
#result = subprocess.run(cmd,shell=True,stdout=True)

f_out.close()

