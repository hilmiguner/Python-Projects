import requests  # This module needs to be download by pip. ("pip install requests" or "python3 -m pip install requests")
# This module gets the source code of a website as html.

dirOfRequests = dir(requests)
print(dirOfRequests)

print(50*"*")

linkGet = requests.get("https://jsonplaceholder.typicode.com/todos")  
# If the output is "Response [200]", we can successfully access the website.
print(linkGet)

print(50*"*")

# If we look inside of the website, we can see a json text. With .text we can take the json text.
jsonText = linkGet.text
print(jsonText, "\nType of the json text:", type(jsonText))  # As you can see it is a string.

print(50*"*")

# Let's make it a list of dictionaries.
import json
listFromString = json.loads(jsonText)
print(listFromString, "\nType of the variable:", type(listFromString))  # It is a list of dictionaries.
print("Type of the any index in the list:", type(listFromString[0]))

print(50*"*")

# For example let's get the value of "title" at 48. index.
str1 = listFromString[48]["title"]
print("title value of 48. index:", str1)
