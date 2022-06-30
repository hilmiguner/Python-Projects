import time
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self):
        self.__browser = None
        self.is_logged_in = False

    def check_browser(self, *args):
        if self.__browser is None:
            self.__browser = webdriver.Firefox(service=Service(executable_path="../drivers/geckodriver_w10.exe"))
            if len(args) == 1:
                self.__browser.get(args[0])
            self.__browser.maximize_window()
            time.sleep(3)
        else:
            if self.__browser.current_url != args[0]:
                self.__browser.get(args[0])
                time.sleep(2)

    def login(self, username="giomikerlyne@outlook.com", password="baron951"):
        if not self.is_logged_in:
            self.check_browser("https://www.instagram.com/")
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input').send_keys(username)
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input').send_keys(password)
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
            time.sleep(7)

            # Login failure handling.
            try:
                self.__browser.find_element(By.CSS_SELECTOR, '#slfErrorAlert')
            except NoSuchElementException as err:
                self.is_logged_in = True
            else:
                print("Login failure.")

        # AFTER_SUCCESSFUL_LOGIN

        # Bypassing the notification.
        if self.is_logged_in:
            try:
                self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
            except NoSuchElementException as err:
                pass
            else:
                self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
                time.sleep(2)

    def logout(self):
        if self.is_logged_in:
            self.check_browser("https://www.instagram.com/")
            time.sleep(2)
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span').click()
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]').click()
            time.sleep(2)

    def go_profile(self, *args):
        self.check_browser("https://www.instagram.com/")
        time.sleep(2)
        if len(args) == 0:
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span').click()
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
            time.sleep(2)
        elif len(args) == 1:
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(args[0])
            time.sleep(1)
            self.__browser.find_element(By.CSS_SELECTOR, '.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 div[class="_aarf"]').click()
            time.sleep(2)

    def take_followers(self):
        self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)



obj = Instagram()
obj.login()
# obj.logout()
obj.go_profile()
obj.take_followers()

