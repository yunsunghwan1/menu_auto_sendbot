from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
SCROLL_PAUSE_TIME = 1

# 외부파일에서 아이디 비번 가지고 오기 
with open('login.txt', 'r') as f:
    credentials = f.read().split(',')
    id = credentials[0]
    password = credentials[1]

driver = webdriver.Chrome()
elem = driver.get('https://gj.korchamhrd.net/co')
time.sleep(SCROLL_PAUSE_TIME)
# 검색 위치 주소가 name에 q가 있음
driver.find_element(By.ID,'user_id').send_keys(id)
driver.find_element(By.ID,'password').send_keys(password)

log_in_button_path = "#loginForm > div > div > div > div.logBox > div.logIp > div:nth-child(3) > div > a"
driver.find_element(By.CSS_SELECTOR, log_in_button_path).click()
time.sleep(SCROLL_PAUSE_TIME)

menu_button_path = "#container > div.subContent.mb0 > div.campusHome > div.doubleBox01.max > div.box.right01 > div.camList02 > ul > li:nth-child(1) > a"
driver.find_element(By.CSS_SELECTOR, menu_button_path).click()
time.sleep(SCROLL_PAUSE_TIME)

driver.maximize_window()
time.sleep(SCROLL_PAUSE_TIME)
menu_table_path  = "#container > div.subContent.max > div.noticeView02 > div.contText > table"
table = driver.find_element(By.CSS_SELECTOR, menu_table_path)
time.sleep(SCROLL_PAUSE_TIME)
table.screenshot('table.png')
driver.close()