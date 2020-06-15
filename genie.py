from bs4 import BeautifulSoup
from selenium import webdriver

import time as t

base_url = "https://www.genie.co.kr/chart/top200"

meta_data = [] # 다운 받을 데이터 공간

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(base_url)

t.sleep(3)

n = 1

for j in range(4):

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    temp_data = soup.select("td[class=info]")

    for i in temp_data:
        title_data = i.select_one(".title.ellipsis").text.strip()
        artist_data = i.select_one(".artist.ellipsis").text.strip()
        album_data = i.select_one(".albumtitle.ellipsis").text.strip()

        print(n, "등")
        print("제목 : ", title_data)
        print("가수 : ", artist_data)
        print("앨범 : ", album_data)

        n += 1

    if j == 3:
        break

    next_url = "#body-content > div.page-nav.rank-page-nav > a:nth-child(" + str(j+2) + ")"

    driver.find_element_by_css_selector(next_url).click()

    t.sleep(3)

#body-content > div.page-nav.rank-page-nav > a:nth-child(2)