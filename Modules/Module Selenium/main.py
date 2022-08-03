from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.chrome.service import Service as chromeService
import time

driver = webdriver.Firefox(service=firefoxService(executable_path="../Module Selenium/drivers/geckodriver_w10.exe"))  # It's for firefox on Windows 10.
# driver = webdriver.Chrome(service=chromeService(executable_path="../Module Selenium/drivers/chromedriver_mac")) # It's for chrome on Mac
url = "https://github.com"

driver.get(url)

time.sleep(1)
print("Title:", driver.title)

time.sleep(1)
driver.maximize_window()
driver.save_screenshot("gitHubHomepage.png")

time.sleep(1)
url = "https://github.com/sadikturan"
driver.get(url)
driver.save_screenshot("sadikTuranGitHub.png")

time.sleep(1)
driver.back()

time.sleep(1)
driver.forward()

time.sleep(1)
driver.close()