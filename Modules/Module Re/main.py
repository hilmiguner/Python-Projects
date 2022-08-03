import re

inRe = dir(re)
print(inRe)

print(50*"*")

# "re.findall(string str1, string str2)" takes 2 string parameters and searches the first parameter in second parameter
# and returns the list.
str1 = "Python Kursu: Python Programlama Rehberiniz | 40 saat"
list1 = re.findall("Python", str1)
print(list1)
print("There are", len(list1), '"Python" in the string.')

print(50*"*")

# "re.split(string str1, string str2)" makes a list by splitting the second parameter with the first parameter.
list2 = re.split(" ", str1)
print(list2)

print(50*"*")

# "re.sub(string str1, string str2, string str3)" changes every str1 into str2 in str3.
str2 = re.sub("P", "A", str1)
print(str2)

print(50*"*")

# "re.search(string str1, string str2)" searches str1 in str2 and returns a Match object.
matchObj = re.search("Python", str1)
print(matchObj)
print(matchObj.span())  # Interval of indexes of str1 in str2.
print(matchObj.start())  # Beginning index of the interval.
print(matchObj.end())  # Ending index of the interval.
print(matchObj.group())  # String that you are searching in str2.
print(matchObj.string)  # String that you are searching str1 in it.

print(50*"*")

list3 = re.findall("[abc]", str1)  # Searches for every character between the brackets.
print('All a, b and c characters in "' + str1 + '":', list3)

list1 = re.findall("[sati]", str1)  # Searches for every character between the brackets.
print('All s, a, t and i characters in "' + str1 + '":', list1)

list1 = re.findall("[a-e]", str1)  # Searches for every character in the interval a to e.
print('All characters in the interval a to e in "' + str1 + '":', list1)

list1 = re.findall("[1-5]", str1)  # Searches for every character in the interval 1 to 5.
print('All characters in the interval 1 to 5 in "' + str1 + '":', list1)

list1 = re.findall("[1-30]", str1)  # Searches for 0 and every character in the interval 1 to 3 and.
print('0 and all characters in the interval 1 to 3 in "' + str1 + '":', list1)

list1 = re.findall("[^abc]", str1)  # Searches for every character except a, b and c.
print('Every character except a, b and c in "' + str1 + '":', list1)

list1 = re.findall("[^0-9]", str1)  # Searches for every non-numerical characters.
print('Every non-numerical characters in "' + str1 + '":', list1)

list1 = re.findall("...", str1)  # Searches for every 3 digits strings because the first parameter is "...".
print('Every 3 digits strings in "' + str1 + '":', list1)

list1 = re.findall("Py..on", str1)  # Searches for every 5 digits strings which starts with "Py" and end with "on".
print('Every 5 digits strings which start with "Py" and end with "on" in "' + str1 + '":', list1)

list1 = re.findall("^P", str1)  # Returns a list with the first parameter if the second parameter starts with first parameter.
print(list1)

list1 = re.findall("t$", str1)  # Returns a list with the first parameter if the second parameter ends with first parameter.
print(list1)

list1 = re.findall("saat$", str1)  # Returns a list with the first parameter if the second parameter ends with first parameter.
print(list1)

list1 = re.findall("sa*t", str1)  # Searches strings that start with "s", end with "t" and contain one "a" or multiple "a"'s.
print('Strings that start with "s", end with "t" and contain one "a" or multiple "a"' + "'s", 'in "' + str1 + '":', list1)

# You can use "+" instead of "*".

list1 = re.findall("sa+t", str1)  # Searches strings that start with "s", end with "t" and contain one "a" or multiple "a"'s.
print('Strings that start with "s", end with "t" and contain one "a" or multiple "a"' + "'s", 'in "' + str1 + '":', list1)

list1 = re.findall("sa?t", str1)  # Searches strings that start with "s", end with "t" and contain one or zero "a".
print('Strings that start with "s", end with "t" and contain one or zero "a" in "' + str1 + '":', list1)

list1 = re.findall("a{2}", str1)  # Searches strings that 2 "a"'s are attached to each other.
print('Strings that 2 "a"' + "'s are attached to each other in " + '"' + str1 + '":', list1)

list1 = re.findall("a{2,3}", str1)  # Searches strings that at least 2 or at most 3 "a"'s are attached to each other.
print('Strings at least 2 or at most 3 "a"' + "'s are attached to each other in " + '"' + str1 + '":', list1)

list1 = re.findall("[0-9]{2,4}", str1)  # Searches strings that include at least 2 and at most 4 digits numbers.
print('Strings that include at least 2 and at most 4 digits numbers in "' + str1 + '":', list1)

