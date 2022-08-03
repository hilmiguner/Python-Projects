def printText(str1: str, str2: str):
    print(str1.center(50, "*"))
    print(str2)
    print(50*"*")

with open("index.html", "r") as file:
    html_doc = file.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")
result = soup.prettify()  # Makes the html code appropriate for the syntax rules.
title = soup.title
printText(" TITLE ", title)

head = soup.head
printText(" HEAD ", head)

body = soup.body
printText(" BODY ", body)

print(soup.title.name)
print(soup.title.string)

h1 = soup.h1  # There is only 1 h1.
printText(" H1 ", h1)
print(h1.name)
print(h1.string)

h2 = soup.h2  # There are more than 1 h2 so what will happen ?
printText(" H2 ", h2)  # Prints the first h2 label.
print(h2.name)
print(h2.string)

print(50*"*")

listForH2 = soup.find_all("h2")  # Makes a list of all h2 labels in the html.
for i in listForH2:
    print(i)

print(50*"*")

div = soup.div  # Gets the first div.
print(div)

print(50*"*")

listForDiv = soup.find_all("div")
count = 1
for i in listForDiv:
    print(f"{count}. div:\n{i}")
    count += 1

print(50*"*")

secondUl = listForDiv[1].ul
print(secondUl)

print(50*"*")

listForLiFromSecondUl = secondUl.find_all("li")
count = 1
for i in listForLiFromSecondUl:
    print(f"{count}. li: {i}")
    count += 1

print(50*"*")

# ".findChildren()" gets every child label under the parent label.
listForChildrenOfFirstDiv = soup.body.find_all("div")[0].findChildren()  
print(listForChildrenOfFirstDiv)

print(50*"*")

div = soup.body.div  # It is the first div.
printText(" FIRST DIV ", div)
# But we can find next sibling which means next div.
div = div.findNextSibling()
printText(" SECOND DIV ", div)
div = div.findNextSibling()
printText(" THIRD DIV ", div)
# Or we can find the previous sibling.
div = div.findPreviousSibling()
printText(" SECOND DIV ", div)
div = div.findPreviousSibling()  # Back to the first div.
printText(" FIRST DIV ", div)

listOfA = soup.find_all("a")
for link in listOfA:
    print(link)
    print(link.get("href"))
    print(50*"*")