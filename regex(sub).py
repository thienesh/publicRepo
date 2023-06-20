import re

with open("task(20-06)", 'r') as f:
    str1 = f.readlines()


for line in str1:
    substr = "too"
    new_str = re.sub("to", substr, line)
    print(f"new string: {new_str}")
