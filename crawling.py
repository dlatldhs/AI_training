from msilib import type_binary
from re import T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

# 변수
named =[] # 검색어를 입력받을 list
directory_list = [
    './projectpublic_data/data_set/train',
    './projectpublic_data/data_set/test'
]
SCROLL_PAUSE_TIME = 1
count = 1
# directroy 만들기
#for directory in directory_list:
#    if not os.path.isdir(directory):
#        os.makedirs(directory)

# 사용자에게 검색할 데이터 키워드 입력받기
while True:
    input_data = input('검색어를 입력해주세요(종료:quit) :')
    if input_data == 'quit' :
        break
    named.append(input_data) # list로 안해주면 단어 하나하나 씩 검색함

# directory 만드는 함수
def createDirectory(directory): # create directory function
    try:
        if not os.path.exists(directory): # Use Os
            os.makedirs(directory) # mkdir directory
    except OSError:
        print("Error: Failed to create the directory.")

# 크롤링 하는 함수 
def crawling_img(named):

    ## chrome webdriver 실행 시킴
    driver = webdriver.Chrome("project\public_data\crawling\chromedriver.exe")
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q") # google 검색 창 선택
    elem.send_keys(named) # named 입력
    print(named)
    elem.send_keys(Keys.RETURN)# press Enter
    
    # 스크롤을 끝까지 내리는 동작
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
    # ==========================

    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # 가져올 수 있는 작은 이미지 선택
    # directory 생성
    for directory in directory_list: #directory list 를 directory가 돌면서 다함
        directory += named + '/'# 검색 키워드 넣어서 파일을 만들꺼임
        createDirectory(directory)# 아까 만들어 놓은 함수에다가 넘겨주는거임
    
    # 이미지 받기 start
    for img in imgs: #imgs 가져올 수 있는 작은 이미지 선택된거
        try: # 한번 실행하고 계속하는거
            img.click() # 이미지 클릭
            time.sleep(2)# 2초 기다리고
            
            imgUrl = driver.find_element_by_xpath( #imgurl 찾기
                # 크게 뜬 이미지 선택하여 "src" 속성을 받아옴
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div[1]/a/img').get_attribute("src")
            
            # 다운로드 받을 path
            path = './projectpublic_data/data_set/train'
            
            # url을 다운로드 해주는 함수이다.(라이브러리)
            urllib.request.urlretrieve(imgUrl, path + named + str(count) + ".jpg")
            count += 1

            # 받을 이미지 개수 count가 넘어가면 종료시켜서 내가 원하는 수 만큼 
            if count > 80: # 받을 이미지 개수
                break
    
        except:
            pass
    # 구글 드라이버 닫기
    driver.close()

# 사용자에게 키워드 입력받기
for i in named:
    crawling_img(i)

# 이미지 검색 및 다운로드가 다 끝나면 
print("DONE!")