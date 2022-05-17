from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

# variable
name = '서동현'
count = 0

driver = webdriver.Chrome('C:/Users/sionz/Desktop/dlxkw/project\public_data\crawling\chromedriver.exe') # need chrome driver path
driver.get('https://naver.com')

elem = driver.find_element_by_name("q") # google search

elem.send_keys(name)
elem.send_keys(Keys.RETURN) # ENTER 치는거

# img url 가져오기
imgs = driver.find_element_by_css_selector(".rg_i.Q4LuWd")
count = 1
for img in imgs:
    try:
        img.click()
        time.sleep(2)
        img_url = driver.find_element_by_xpath(
            '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
        ).get_attribute("src")
        path = "C:\\Users\\sionz\\Desktop\\dlxkw\\project\\public_data\\crawling\\imgs\\" + name + "\\"
        urllib.request.urlretrieve(img_url, path + name + str(count + ".jpg"))
        count = count + 1
        if count > 260:
            break
    except:
        pass