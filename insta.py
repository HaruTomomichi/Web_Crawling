from urllib.request import urlopen
from urllib.parse import quote_plus

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t

meta_id = "01041560286"
meta_password = "asrock6601"

base_url = "https://www.instagram.com/"
plus_url = input("검색할 아이디를 입력하세요 : ")
limit_num = int(input("저장할 이미지의 수를 입력하세요 : "))

url = base_url + quote_plus(plus_url) # 검색어를 아스키 코드로 변환

meta_data = [] # 다운 받을 이미지 링크 공간
like_meta_data = [] # 좋아요 숫자 공간
comment_meta_data = [] # 이 데이터는 사용하지 않음

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

try:
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
except:
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/div/div[1]/div/form/div[4]/button").click()

t.sleep(2)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()

# 데이터 전송 기다릴 것 / 특히 한글일 경우

t.sleep(5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()

while 1:
    t.sleep(1)

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    # 좋아요 추출

    like_num = soup.select(".sqdOP.yWX7d._8A5w5")

    if like_num == []:
        driver.find_element_by_class_name("coreSpriteRightChevron").click()

    print(like_num[1].select('span'))
    like_num = like_num[1].select('span')

    like_meta_data.append(int(like_num[0].text))
    print(like_meta_data)


    # 이미지 추출

    imgUrl = soup.select_one('.KL4Bh').img['src']

    print(imgUrl)

    if imgUrl in meta_data:
        continue

    meta_data.append(imgUrl)

    #



    if len(meta_data) == limit_num:
        overflow_status = False
        break

    driver.find_element_by_class_name("coreSpriteRightChevron").click()





n = 1 # 증감 연산자
for i in meta_data:
    with urlopen(i) as f:
        with open('./save_image/' + plus_url + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    print(n,"번째 이미지 다운로드 완료\n")
    n += 1

t.sleep(5)
driver.close()


