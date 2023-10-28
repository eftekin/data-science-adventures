import json

person = {
    'first_name': 'Mark',
    'last_name': 'abc',
    'age': 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open("person.json", "w") as f:  # writing json object
    json.dump(person, f)

# serializing json
json_object = json.dumps(person, indent=4)

# writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

print(json_object)
