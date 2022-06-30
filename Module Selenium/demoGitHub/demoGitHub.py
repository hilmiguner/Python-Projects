from userInfo import username, password
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
import time

class GitHub:
    def __init__(self):
        self.__browser = None
        self.url = ""
        self.count = 1
        self.followersHtml = ""
        self.__followersList = []
        self.is_logged_in = False

    def sign_in(self):
        self.check_browser()
        self.url = "https://github.com/login"
        self.__browser.get(self.url)
        time.sleep(1)
        self.__browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(username)
        self.__browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.__browser.find_element(By.XPATH, '/html/body/div[3]/main/div/div[4]/form/div/input[12]').click()
        time.sleep(1)
        if self.__browser.current_url != "https://github.com/session":
            self.is_logged_in = True
        self.__browser.minimize_window()

    def sign_out(self):
        self.check_browser()
        self.__browser.maximize_window()
        self.__browser.find_element(By.CSS_SELECTOR, '.Header-item.position-relative.mr-0.d-none.d-md-flex').click()
        time.sleep(1)
        self.__browser.find_element(By.CSS_SELECTOR, '.dropdown-item.dropdown-signout').click()
        time.sleep(1)
        self.__browser.minimize_window()

    def get_followers_list(self, username):
        self.check_browser()
        self.__browser.maximize_window()
        self.__browser.get(f"https://github.com/{username}?tab=followers")
        time.sleep(2)
        will_break = False
        while True:
            followers = self.__browser.find_elements(By.CSS_SELECTOR, '.d-table.table-fixed')
            for follower in followers:
                self.__followersList.append(follower.find_element(By.CSS_SELECTOR, '.Link--secondary').text)
            for i in self.__browser.find_element(By.CSS_SELECTOR, '.paginate-container').find_elements(By.CSS_SELECTOR, 'a'):
                if i.text == "Next":
                    i.click()
                    time.sleep(2)
            if will_break:
                break
            if len(self.__browser.find_element(By.CSS_SELECTOR, '.paginate-container').find_elements(By.CSS_SELECTOR, 'a')) == 1 and self.__browser.find_element(By.CSS_SELECTOR, '.paginate-container').find_elements(By.CSS_SELECTOR, 'a')[0].text == "Previous":
                will_break = True
        time.sleep(2)
        self.__browser.minimize_window()
        self.print_followers_list()

    def print_followers_list(self):
        count = 1
        for follower in self.__followersList:
            print(f"{count}. follower's name:", follower)
            count = count + 1

    def close_browser(self):
        if self.__browser is not None:
            self.__browser.close()

    def check_browser(self):
        if self.__browser is None:
            self.__browser = webdriver.Firefox(service=firefoxService(executable_path="../drivers/geckodriver_w10.exe"))
            self.__browser.maximize_window()

obj = GitHub()
while True:
    secim = int(input("1-Giriş yap\n2-Takipçi listesi al\n3-Çıkış yap\n4-Programı kapat\nSeçim: "))
    if secim == 4:
        obj.close_browser()
        break
    else:
        if secim == 1:
            if not obj.is_logged_in:
                obj.sign_in()
            else:
                print("Zaten bir hesabınız açık.")
        elif secim == 2:
            user = input("Hangi kullanıcının takipçi listesini istiyorsun: ")
            obj.get_followers_list(user)
        elif secim == 3:
            if obj.is_logged_in:
                obj.sign_out()
            else:
                print("Zaten sistemde açık bir hesap yok.")
