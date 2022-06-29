from selenium import webdriver
import time

driver = webdriver.Safari() # It's now program's web browser.
# driver = webdriver.Chrome(executable_path="../SELENIUM/chromedriver") # It's for chrome.
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