list1 = ["kocaeli","istanbul"]
list2 = [41,34]
print(list2[list1.index("kocaeli")])
print(list2[list1.index("istanbul")])

# We use dictionary for above syntax.

print("------------------------")

# variableName = { key1 : value1 , key2 : value2 , ...}

dictionary = {"kocaeli" : 41 , "istanbul" : 34}
print(dictionary["kocaeli"])
print(dictionary["istanbul"])

print("------------------------")

dictionary["ankara"] = 6
print(dictionary)

print("------------------------")

users = {"hilmi":{"age" : 20 , "roles" : ["worker","student"] , "email" : "hilmi.guner@hotmal.com" , "adress" : "Bursa" , "phone" : 123456} , "efe":{"age" : 14 , "roles" : ["student"] , "email" : "efe.guner@hotmal.com" , "adress" : "Bursa" , "phone" : 654321}}
print(users["hilmi"]["age"])
print(users["hilmi"]["roles"])
print(users["hilmi"]["roles"][0])