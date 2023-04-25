import os
cmd = "ping google.com"
result = os.system(cmd)
print(f"Result: {result}")

import subprocess
cmd1 = "ipconfig /all"
result1 = subprocess.run(cmd1,capture_output=True, text=True)
print(f"My cmdline output for '{cmd1}' is {result1.stdout}")
