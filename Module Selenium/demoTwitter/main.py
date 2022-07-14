import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self):
        self.__browser = None
        self.email = "hilmi.guner@hotmail.com"
        self.password = "spiderman2001"

    def check_browser(self, *args):
        if self.__browser is None:
            self.__browser = webdriver.Chrome(service=chromeService(executable_path="Module Selenium/drivers/chromedriver_mac"))
            if len(args) == 1:
                self.__browser.get(args[0])
            self.__browser.maximize_window()
            time.sleep(self.getRandomDelay(3, 5))
        else:
            if self.__browser.current_url != args[0]:
                self.__browser.get(args[0])
                time.sleep(self.getRandomDelay(3, 5))

    def getRandomDelay(self, num1, num2):
        return random.uniform(num1, num2)

    def signIn(self):
        self.check_browser("https://twitter.com/i/flow/login")        
        self.__browser.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input').send_keys(self.email)
        self.__browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(self.getRandomDelay(3, 5))
        self.__browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(self.password)
        self.__browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()

obj = Twitter()
obj.signIn()

    