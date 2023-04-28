import json


with open("Instance launch code (AWS).json", 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
# pyth_data = json.loads(data)