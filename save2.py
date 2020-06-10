from urllib.request import urlopen
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t

base_url = "https://www.instagram.com/explore/tags/"
plus_url = input("검색할 단어를 입력하세요 : ")

limit_num = int(input("저장할 이미지의 수를 입력하세요 : "))

url = base_url + quote_plus(plus_url) # 검색어를 아스키 코드로 변환

#

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

# 데이터 전송 기다릴 것 / 특히 한글일 경우

t.sleep(5)

body = driver.find_element_by_css_selector("body")

for i in range(30):
    body.send_keys(Keys.END)
    t.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    insta = soup.select('.v1Nh3.kIKUG._bz0w') # 클래스가 3개일 경우에는 점으로 구분

    n = 1 # 반복숫자
    for i in insta:
        print('https://www.instagram.com/' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']

        with urlopen(imgUrl) as f:
            with open('./save_image/' + plus_url + str(n) + '.jpg','wb') as h:
                img = f.read()
                h.write(img)

        n += 1
        print(imgUrl)
        print()

t.sleep(5)
driver.close()


