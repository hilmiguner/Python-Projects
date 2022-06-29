from userInfo import username, password
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
import time

class GitHub:
    def __init__(self):
        self.browser = webdriver.Firefox(service=firefoxService(executable_path="../drivers/geckodriver_w10.exe"))
        self.url = ""
        self.count = 1
        self.followersHtml = ""
        self.__followersList = []

    def sign_in(self):
        self.url = "https://github.com/login"
        self.browser.get(self.url)
        time.sleep(1)
        self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.browser.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()
        time.sleep(2)
        self.browser.minimize_window()

    def get_followers_list(self, username):
        self.browser.get(f"https://github.com/{username}?tab=followers")
        time.sleep(2)
        followers = self.browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed')
        for follower in followers:
            self.__followersList.append(follower.find_element(By.CSS_SELECTOR, '.Link--secondary').text)
        self.browser.close()
        self.print_followers_list()

    def print_followers_list(self):
        count = 1
        for follower in self.__followersList:
            print(f"{count}. follower's name:", follower)
            count = count + 1

obj = GitHub()
obj.sign_in()
user = input("Hangi kullanıcının takipçi listesini istiyorsun: ")
obj.get_followers_list(user)

