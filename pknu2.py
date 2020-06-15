from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd

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

        data_title = tag1.text.strip()
        data_author = tag2.text
        data_date = tag3.text

        data_author = data_author.replace("\xa0","")
        data_date = data_date.replace("\xa0", "")

        meta_data.append([data_title,data_author,data_date])

        if find_data in data_title:
            pass
            # print(data_title,"/", data_author,"/",  data_date)

    if n == limit_num:
        break

    n += 1

    driver.find_element_by_css_selector("#contents > div.contents-inner > div.paginate > a:nth-child(" + str(n+1) + ")").click()

# 판다스 작업

save_data = pd.DataFrame(meta_data)
save_data.columns = ['title','author','time']

print(meta_data)

save_data.to_csv('부경대학교 크롤링 결과.csv',encoding='cp949')

t.sleep(5)
driver.close()


