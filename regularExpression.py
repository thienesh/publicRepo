import re

with open("task(20-06)", 'r') as f:
    str1 = f.readlines()
for line in str1:
    mo = re.match(".*Hello.*", line)

    if mo:
        print(f"Matched string:: {mo.group()}")
        break
else:
    print("Not matching!!")
