import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

response = requests.get(url)
if response.status_code != 200:
    print("Response Failure")
else:
    html_doc = response.content
    soup = BeautifulSoup(html_doc, "html.parser")

    tbody = soup.find("tbody", {"class" : "lister-list"})
    listOfTr = tbody.find_all("tr", limit=5)  # limit attribute limits the len of the list.
    count = 1
    for tr in listOfTr:
        title = tr.find("td", {"class" : "titleColumn"}).find("a").text
        year = tr.find("td", {"class" : "titleColumn"}).find("span", {"class" : "secondaryInfo"}).text.strip("()")
        imdb_rating = tr.find("td", {"class" : "ratingColumn imdbRating"}).find("strong").text
        print((f" {count}. MOVIE INFO ").center(50, "*"))
        print(f"Title: {title}")
        print(f"Year: {year}")
        print(f"IMDB Rating: {imdb_rating}")
        print(50*"*")
        count += 1