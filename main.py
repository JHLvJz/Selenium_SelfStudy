#/Users/moonjihoo/Downloads/chromedriver_mac_arm64/chromedriver
#웹드라이버 경로
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def Please():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3) #find메소드에 영향 (최대 n초 기다림, 성공하면 바로 넘어감)


    driver.get(' https://workey.codeit.kr/costagram/index')
    time.sleep(1) #단순지연 (로딩되거나 바뀔 때)
    driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
    driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')
    driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()

    while(True):
        pass
Please() 