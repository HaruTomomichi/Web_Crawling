from urllib.request import urlopen
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t

base_url = "http://www.pknu.ac.kr/usrBoardActn.do?p_bm_idx=5&p_boardcode=PK10000005&p_sbsidx=2"

find_data = input("검색할 단어를 입력하세요 : ")
limit_num = int(input("저장할 페이지의 수를 입력하세요 : "))

url = base_url# 검색어를 아스키 코드로 변환
meta_data = [] # 다운 받을 데이터 공간

#

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

# 로그인 과정

# 데이터 전송 기다릴 것 / 특히 한글일 경우

t.sleep(5)

n = 1

while 1:
    t.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    meta_content = soup.select('td[class=title]')
    meta_author = soup.select('td[class=author]')
    meta_date = soup.select('td[class=date]')

    for tag1,tag2,tag3 in zip(meta_content,meta_author,meta_date):
        if find_data in tag2.text:
            print("title : " + tag1.text.strip())
            print("author : " + tag2.text)
            print("time : " + tag3.text)
            print("-" * (n * 20))

    if n == limit_num:
        break

        # contents > div.contents-inner > div.paginate > a:nth-child(3)
        # contents > div.contents-inner > div.paginate > a:nth-child(4)

    n += 1

    driver.find_element_by_css_selector("#contents > div.contents-inner > div.paginate > a:nth-child(" + str(n+1) + ")").click()

t.sleep(5)
driver.close()


