from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# driver = webdriver.Safari()  # For safari no mac.
driver = webdriver.Firefox(service=firefoxService(executable_path="../drivers/geckodriver_w10.exe"))
url = "https://github.com"
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
repo1 = driver.find_elements(By.CSS_SELECTOR, '.repo-list-item a[class="v-align-middle"]')
for element in repo1:
    print(element.text)

print(50*"*")

# Or we can use BeautifulSoup module to find repositories names.
sourceCode = driver.page_source  # Takes the source code of the page.
driver.close()  # We are done with selenium, so we can close the browser.
soup = BeautifulSoup(sourceCode, "html.parser")
repo2 = soup.find("ul", {"class" : "repo-list"}).find_all("li")
for element in repo2:
    print(element.find("a", {"class" : "v-align-middle"}).text)

