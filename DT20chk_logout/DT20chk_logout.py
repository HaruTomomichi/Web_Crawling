print("*"*50)
print("공공데이터 청년 인턴십 자동 퇴근 시스템 v0.1")
print("*"*50)

print("업무 중분류 체계는 다음과 같습니다")
print(" - 공공데이터포털 목록등록체계 및 메타정보 점검 : 2") # DR0010
print(" - 공공데이터 보유현황 정리 및 메타데이터 등록 : 3") # DR0011
print(" - 공공데이터 목록 구성 및 개방 : 4") # DR0012
print(" - 기관자체 개방포털 및 개방데이터 정비 : 6") # DR0014
print("현재는 코드 3로 고정되어 있습니다 (테스트 중)")

# id = input('아이디를 입력해주세요 : ')
# password = input('패스워드를 입력해주세요 : ')
# big_div = input('업무 중분류 체계 코드를 입력해주세요 (ex: 2) : )
# small_div = input('업무 소분류 체계 코드를 입력해주세요 (ex: 2) : )
# content = input('오늘 업무 내용을 입력해주세요 (최대 50자) : ')
# 슬라이싱 기능 포함
# name = input('성함을 입력해주세요 : ')

from selenium import webdriver
from time import sleep

url = "http://dt20chk.hyosungitx.com/main"

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

def login():
    driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

try:
    login()
    sleep(2)
except:
    driver.find_element_by_xpath('/html/body/div[3]/button').click()
    sleep(2)
    login()
    sleep(2)

driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
sleep(2)

# 중분류
# //*[@id="selCategory1"]/option[2]
# //*[@id="selCategory1"]/option[3]
# //*[@id="selCategory1"]/option[4]
# //*[@id="selCategory1"]/option[6]

# 소분류
sleep(2)
driver.find_element_by_xpath('//*[@id="selCategory1"]/option['+ big_div +']').click()
driver.find_element_by_xpath('//*[@id="selCategory2"]/option[4]').click()
driver.find_element_by_xpath('//*[@id="taEtcMemo"]').send_keys(content)

driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
sleep(2)

driver.find_element_by_xpath('//*[@id="iptUserName1"]').send_keys(name)
driver.find_element_by_xpath('//*[@id="iptUserName2"]').send_keys(name)
# driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

sleep(3)
driver.close()