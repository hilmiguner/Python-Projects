from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Safari()
url = "https://github.com"
driver.get(url)
driver.maximize_window()

searchInput = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
repo = driver.find_elements(By.CSS_SELECTOR, '.repo-list-item a[class="v-align-middle"]')
for element in repo:
    print(element.text)

# Or we can use BeautifulSoup module to find repositories names.
sourceCode = driver.page_source  # Takes the source code of the page.

driver.close()