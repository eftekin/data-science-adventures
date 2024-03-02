import json

# opening json file
with open("sample.json", "r") as openfile:

    # reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))
