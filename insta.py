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

    t.sleep(3)
    driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
except:
    driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/div/div[1]/div/form/div[4]/button").click()
    driver.get(url)

# 데이터 전송 기다릴 것 / 특히 한글일 경우

t.sleep(5)
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a").click()

while 1:
    t.sleep(2)

    if len(like_meta_data) == limit_num:
        break

    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")

    # 좋아요 추출

    temp = soup.select(".Igw0E.IwRSH.eGOV_.ybXk5.vwCYk")

    if not temp:
        like_meta_data.append(0)
        driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
        continue

    temp = temp[0].select('span')

    if len(temp) == 2:
        like_meta_data.append(int(temp[1].text))
    else:
        like_meta_data.append(int(temp[0].text))

    # 이미지 추출

    print(meta_data,"\n",like_meta_data)
    driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()

driver.find_element_by_xpath("/html/body/div[4]/div[3]/button").click()

t.sleep(5)
body = driver.find_element_by_css_selector("body")

while 1:
    print(meta_data, "\n", like_meta_data)

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

    body.send_keys(Keys.END)
    t.sleep(1)

for i in range(len(like_meta_data)):
    for j in range(len(like_meta_data)):
        if like_meta_data[i] < like_meta_data[j] and i < j:
            like_meta_data[i],like_meta_data[j] = like_meta_data[j],like_meta_data[i]
            meta_data[i],meta_data[j] = meta_data[j],meta_data[i]

n = 0 # 증감 연산자
for i in meta_data:
    with urlopen(i) as f:
        with open('./save_image/' + plus_url + "_" + str(n+1) + "_" + str(like_meta_data[n]) + "의 좋아요" + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    print(n+1,"번째 이미지 다운로드 완료\n")
    n += 1

t.sleep(5)
driver.close()


