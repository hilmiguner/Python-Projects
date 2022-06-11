name = "Hilmi"
surname = "Güner"
print("My name is {} {}.".format(name,surname))
print("My name is {0} {1}.".format(name,surname))
print("My name is {1} {0}.".format(name,surname))
# Numbers are format() functions mean indexes.
print("------------------------------------------------------------")
print("My name is {s} {n}.".format(n=name,s=surname))
age = 20
print("My name is {} {} and I'm {} years old.".format(name,surname,age))
print("My name is {} {} and I'm {} years old.".format(name,surname,20))
print("My name is {} {} and I'm {} years old.".format(name,surname,"20"))
# Let's look another syntax.
print("------------------------------------------------------------")
print(f"My name is {name} {surname} and I'm {age} years old.")