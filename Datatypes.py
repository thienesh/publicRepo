print(f"Types of Datatypes in dictionary format ::")

dic_datatype = {"Integers": 45, "strings": "datatype string", "floats": 5.6, "dictionary": "{'key':'value'}",
                "sets": "{1, 2, 3, 4}", "tuple": "(1, 2, 3, 4, 5)"}

keys = dic_datatype.keys()
values = dic_datatype.values()

print(dic_datatype)
dic_datatype.update({"lists": "[1, 2, 3, 4]"})

print(F"\nThese are the {keys} in the dictionary")
print(F"\nThese are the {values} in the dictionary")
print(F"\nThose keys and values are from the dictionary of datatypes :{dic_datatype} \naccordingly ")
