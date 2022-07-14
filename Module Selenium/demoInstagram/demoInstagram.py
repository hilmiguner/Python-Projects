import time
import random
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service as chromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Instagram:
    def __init__(self):
        self.__browser = webdriver.Chrome(service=chromeService(executable_path="Module Selenium/drivers/chromedriver_mac"))
        self.__browser.maximize_window()
        self.__browser.get("https://instagram.com")
        time.sleep(5)
        self.is_logged_in = False

    def getRandomDelay(self, num1, num2):
        return random.uniform(num1, num2)

    def login(self, username="hilmi.guner@hotmail.com", password="baron.951"):
        if not self.is_logged_in:
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

        # Bypassing the saving login informations notification.
        if self.is_logged_in:
            try:
                self.__browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button')
            except NoSuchElementException as err:
                pass
            else:
                self.__browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/div/div/div/button').click()
                time.sleep(self.getRandomDelay(2, 4))

        # Bypassing the notification.
        if self.is_logged_in:
            try:
                self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
            except NoSuchElementException as err:
                pass
            else:
                self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
                time.sleep(self.getRandomDelay(2, 3))

    def logout(self):
        if self.is_logged_in:
            self.__browser.find_element(By.CSS_SELECTOR, '#mount_0_0_O6 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > nav > div._acc1._acc3 > div > div > div._acuq._acur > div > div:nth-child(6) > div._aaav > span').click()
            self.__browser.find_element(By.CSS_SELECTOR, '#mount_0_0_O6 > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div._a3gq._ab-1 > section > nav > div._acc1._acc3 > div > div > div._acuq._acur > div > div:nth-child(6) > div._aa1s > div._aa5u._aa5x._aa5y._aa5z > div._aa61 > div:nth-child(6)').click()
            time.sleep(self.getRandomDelay(2, 4))

    def go_profile(self, *args):
        self.check_browser("https://www.instagram.com")
        if len(args) == 0:
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[1]/span').click()
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
            time.sleep(self.getRandomDelay(2, 4))
        elif len(args) == 1:
            self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(args[0])
            time.sleep(self.getRandomDelay(2, 3))
            self.__browser.find_element(By.CSS_SELECTOR, '.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4 div[class="_aarf"]').click()
            time.sleep(self.getRandomDelay(2, 4))

    def take_followers(self):
        self.__browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(self.getRandomDelay(2, 4))

obj = Instagram()
obj.login()
# obj.logout()
# obj.go_profile()
# obj.take_followers()
