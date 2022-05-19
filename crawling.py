from msilib import type_binary
from re import T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

named =[] # 검색어를 입력받을 list
while True:
    input_data = input('검색어를 입력해주세요(종료:quit) :')
    if input_data == 'quit' :
        break
    named.append(input_data) # list로 안해주면 단어 하나하나 씩 검색함

def createDirectory(directory): # create directory function
    try:
        if not os.path.exists(directory): # Use Os
            os.makedirs(directory) # mkdir directory
    except OSError:
        print("Error: Failed to create the directory.")

def crawling_img(named):
    driver = webdriver.Chrome("C:\\Users\\sionz\\Desktop\\dlxkw\\project\\public_data\\crawling\\chromedriver.exe")
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q") # google 검색 창 선택
    elem.send_keys(named) # named 입력
    print(named)
    elem.send_keys(Keys.RETURN)# press Enter

    #
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")  # 브라우저의 높이를 자바스크립트로 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 브라우저 끝까지 스크롤을 내림
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # 가져올 수 있는 작은 이미지 선택
    dir = "C:\\Users\\sionz\\Desktop\\dlxkw\\project\\public_data\\crawling\\imgs\\" + named

    createDirectory(dir) #폴더 생성
    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div[1]/a/img').get_attribute("src") # 크게 뜬 이미지 선택하여 "src" 속성을 받아옴
            path = "C:\\Users\\sionz\\Desktop\\dlxkw\\project\\public_data\\crawling\\imgs\\" + named + "\\"
            urllib.request.urlretrieve(imgUrl, path + named + str(count) + ".jpg")
            count = count + 1
            if count >= 5: # 받을 이미지 개수
                break
        except:
            pass
    driver.close()

for i in named:
    crawling_img(i)
print("DONE!")