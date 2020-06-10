from urllib.request import urlopen
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t

meta_id = input("아이디를 입력해 주십시오 :")
meta_password = input("비밀번호를 입력해 주십시오 : ")

base_url = "https://www.instagram.com/explore/tags/"
plus_url = input("검색할 단어를 입력하세요 : ")
limit_num = int(input("저장할 이미지의 수를 입력하세요 : "))

url = base_url + quote_plus(plus_url) # 검색어를 아스키 코드로 변환
meta_data = [] # 다운 받을 이미지 링크 공간

overflow_status = True

#

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

# 로그인 과정

t.sleep(5)
driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button").click()

t.sleep(2)
driver.find_element_by_name("username").send_keys(meta_id)
driver.find_element_by_name("password").send_keys(meta_password)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()

t.sleep(3)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()

# 데이터 전송 기다릴 것 / 특히 한글일 경우

t.sleep(5)
body = driver.find_element_by_css_selector("body")

while 1:
    body.send_keys(Keys.END)
    t.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    insta = soup.select('.v1Nh3.kIKUG._bz0w') # 클래스가 3개일 경우에는 점으로 구분

    for i in insta:
        print('https://www.instagram.com/' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']

        if imgUrl in meta_data: # 중복 링크일 경우 삭제
            continue

        meta_data.append(imgUrl)

        if len(meta_data) == limit_num:
            overflow_status = False
            break

    if not overflow_status:
        break

n = 0 # 증감 연산자
for i in meta_data:
    with urlopen(i) as f:
        with open('./save_image/' + plus_url + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    print(n,"번째 이미지 다운로드 완료\n")
    n += 1

t.sleep(5)
driver.close()


