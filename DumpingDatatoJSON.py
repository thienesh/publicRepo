import json

data = {"name": "rama", "age": 34}

json_data = json.dumps(data)

with open("data.json", 'w') as f:
    json.dump(data, f)
