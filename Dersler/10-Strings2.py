message = "Hello there. My name is Hilmi Güner"
print(message)
message = message.upper()
print(message)
message = message.lower()
print(message)
message = message.title()
print(message)
message = message.capitalize()
print(message)

print("---------------")

message = "   Hello there. My name is Hilmi Güner"  # Difference is there are spaces at the beginning of sentence.
print(message)
message = message.strip()
print(message)

print("---------------")

message = "Hello there. My name is Hilmi Güner."
print(type(message))
print(message)
message = message.split()  # message isn't string anymore, is an list now.
print(type(message))
print(message)
print(message[5])
message = "Hello there. My name is Hilmi Güner."
message = message.split(".")
print(message)

message = "Hello there. My name is Hilmi Güner."
message = message.split()
print(message)
message = "---".join(message)
print(message)

print("---------------")

message = "Hello there. My name is Hilmi Güner."
index = message.find("Hilmi")
print(index)  # On the screen there will be 24. It means "Hilmi" starts from index 24.
index = message.find("Apple")
print(index)  # This time you are going to see -1. That means the word that you are searching in the sentence doesn't exist.

print("---------------")

message = "Hello there. My name is Hilmi Güner."
isFound = message.startswith("H")  # It's bool.
print(isFound)
isFound = message.startswith("J")  # It's bool.
print(isFound)

print("---------------")

message = "Hello there. My name is Hilmi Güner."
isFound = message.endswith(".")  # It's bool.
print(isFound)
isFound = message.endswith("5")  # It's bool.
print(isFound)

print("---------------")

message = "Hello there. My name is Hilmi Güner."
message = message.center(100)
print(message)
message = "Hello there. My name is Hilmi Güner."
message = message.center(50)
print(message)
message = "Hello there. My name is Hilmi Güner."
message = message.center(50,"*")
print(message)