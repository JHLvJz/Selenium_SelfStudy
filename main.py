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


    driver.get('https://workey.codeit.kr/music')
    time.sleep(1)

    popular_artists = []

    for artist in driver.find_elements(By.CSS_SELECTOR, 'ul.popular__order li'):
        popular_artists.append(artist.text.strip())

    print(popular_artists)

Please() 