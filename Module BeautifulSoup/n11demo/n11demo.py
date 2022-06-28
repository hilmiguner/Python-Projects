from pickletools import int4
from bs4 import BeautifulSoup
import requests

def roundNum(num1):
    result = num1/28
    if result == int(result):
        return int(result) + 1
    else:
        return int(result) + 2

page = 1
n = int(input("Write number of the product you want to see: "))
listHTML = []

for page in range(1, roundNum(n)):
    url = f"https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg={page}"
    listHTML.append(requests.get(url).content)   

count = 1

for html in listHTML:
    soup = BeautifulSoup(html, "html.parser")

    list1 = []

    flag = False
    if n > 28:
        temp = n
        flag = True
        n %= 28

        list1 = soup.find("ul", {"class" : "list-ul"}).find_all("li")
    else:
        list1 = soup.find("ul", {"class" : "list-ul"}).find_all("li", limit=n)

    if flag:
        n = temp - 28

    for product in list1:
        name = product.find("h3", {"class" : "productName"}).text
        oldPrice = product.find("div", {"class" : "priceContainer"}).div.span.text.strip()
        newPrice = product.find("span", {"class" : "newPrice cPoint priceEventClick"}).text.strip()
        link = product.find("a", {"class" : "plink"})["href"]
        print(f" {count}. COMPUTER INFO ".center(50, "*"))
        print(f"Product Name: {name}")
        print(f"Old Price: {oldPrice}")
        print(f"New Price: {newPrice}")
        print(f"Link: {link}")
        print(50*"*")
        count += 1


