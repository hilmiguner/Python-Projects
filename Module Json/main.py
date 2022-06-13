import json

person_string = '{"name": "Ali", "languages": ["python", "c#"]}'  # It looks like a dictionary but it is just a string.
# With "json.loads(string str)" we can turn strings into dictionaries.

dict1FromString = json.loads(person_string)
print(type(dict1FromString))  # As we can see it is a dictionary object.
print(dict1FromString)
print("Name:", dict1FromString["name"])
print("Languages:", dict1FromString["languages"])

print(50*"*")

# "json.loads()" turns strings to dictionaries, but "json.load()" reads a json file and turns it to dictionary.
with open("person.json") as file:  # This code block closes the file automatically at the end of itself.
    dict2FromJsonFile = json.load(file)
print(type(dict2FromJsonFile))
print("Name:", dict2FromJsonFile["name"])
print("Languages:", dict2FromJsonFile["languages"])

print(50*"*")

# "json.dumps(dict obj)" turns the dict objects to json strings.
person_dict = {
  "name": "Ali",
  "languages": ["python", "c#"]
}

str1FromDict = json.dumps(person_dict)
print(type(str1FromDict))
print(str1FromDict)

# "json.dump(dict obj, File file)" takes a dictionary and write it to the json file as a json string.
person_dict2 = {
    "name": "Hilmi",
    "age": "21",
    "city": "Istanbul"
}
with open("dictToJson.json", "w") as file:
    json.dump(person_dict2, file)  # If you look at the "dictToJson.json" file, you can see the "person_dict2" as a json string.

