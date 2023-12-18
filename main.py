import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

load_dotenv()

TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
USERNAME = os.getenv("USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.PROMISED_DOWN = 150
        self.PROMISED_UP = 10
        self.get_download_speed = 0
        self.get_upload_speed = 0
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.options)

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        self.driver.maximize_window()

        time.sleep(2)
        accept_cookie = self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button')
        accept_cookie.click()

        time.sleep(2)
        start_test = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                        '1]/a')
        start_test.click()

        time.sleep(45)
        self.get_download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.get_upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(self.get_download_speed)
        print(self.get_upload_speed)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        self.driver.maximize_window()

        time.sleep(5)
        input_mail = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div["
                                                        "2]/div[2]/div/div/div[2]/div[2]/div/div/div/div["
                                                        "5]/label/div/div[2]/div/input")
        input_mail.click()
        input_mail.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div["
                                                         "2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()

        time.sleep(2)
        confirmation = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div["
                                                          "2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div["
                                                          "2]/label/div/div[2]/div/input")
        confirmation.send_keys(USERNAME)
        confirmation_submit = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div["
                                                                 "1]/div/div/div/div/div/div/div[2]/div["
                                                                 "2]/div/div/div[2]/div[2]/div[2]/div/div/div/div")
        confirmation_submit.click()

        time.sleep(2)
        input_password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div["
                                                            "1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                                            "2]/div[2]/div[1]/div/div/div[3]/div/label/div/div["
                                                            "2]/div[1]/input")
        input_password.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div["
                                                          "2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div["
                                                          "1]/div/div/div")
        login_button.click()

        time.sleep(5)
        post = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div["
                                                  "3]/div/div[2]/div[1]/div/div/div/div[2]/div["
                                                  "1]/div/div/div/div/div/div/div/div/div/div/label/div["
                                                  "1]/div/div/div/div/div/div[2]/div")
        post.click()
        post.send_keys(f"Hey Internet Provider, why is my internet speed "
                       f"{self.get_download_speed}down/{self.get_upload_speed} up when I pay for"
                       f" {self.PROMISED_DOWN}down/{self.PROMISED_UP}up?")
        send_post = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div["
                                                       "2]/main/div/div/div/div/div/div[3]/div/div[2]/div["
                                                       "1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]")
        send_post.click()


twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
