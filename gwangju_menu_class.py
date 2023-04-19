import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By 


class menudownload:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.SCROLL_PAUSE_TIME = 1

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        driver = webdriver.Chrome(options=options)
        driver.get('https://gj.korchamhrd.net/co')
        time.sleep(self.SCROLL_PAUSE_TIME)
        driver.find_element(By.ID, 'user_id').send_keys(self.id)
        driver.find_element(By.ID, 'password').send_keys(self.password)

        log_in_button_path = "#loginForm > div > div > div > div.logBox > div.logIp > div:nth-child(3) > div > a"
        driver.find_element(By.CSS_SELECTOR, log_in_button_path).click()
        time.sleep(self.SCROLL_PAUSE_TIME)

        menu_button_path = "#container > div.subContent.mb0 > div.campusHome > div.doubleBox01.max > div.box.right01 > div.camList02 > ul > li:nth-child(1) > a"
        driver.find_element(By.CSS_SELECTOR, menu_button_path).click()
        time.sleep(self.SCROLL_PAUSE_TIME)

        driver.maximize_window()
        time.sleep(self.SCROLL_PAUSE_TIME)
        menu_table_path  = "#container > div.subContent.max > div.noticeView02 > div.contText > table"
        table = driver.find_element(By.CSS_SELECTOR, menu_table_path)
        time.sleep(self.SCROLL_PAUSE_TIME)
        table.screenshot('table.png')
        driver.close()
