import sys
import schedule

from time import sleep
from selenium import webdriver
from datetime import datetime

class WEBSYSTEM:

    def __init__(self):
        self.ID = input('아이디를 입력해주세요 : ')
        self.password = input('\n패스워드를 입력해주세요 : ')
        self.content = input('\n오늘 업무 내용을 입력해주세요 (최대 50자) : ')[:50]
        self.name = input('\n성함을 입력해주세요 : ')
        self.big_div, self.small_div = ['3', '2']

        WEBSYSTEM.one_more_chk(self)
        self.url = 'http://dt20chk.hyosungitx.com/main'
        self.driver = webdriver.Chrome(
            executable_path="webdriver/chromedriver.exe"
        )

    def one_more_chk(self):
        print("*" * 50 + "\nid = ", self.ID)
        print("\npassword = ", self.password)
        print("\n업무 내용 = ", self.content)
        print("\n성함 = ", self.name)
        answer = input("\n입력하신 내용이 다음과 같습니까? (y/n) : ")

        if answer == 'y':
            print("*" * 50 + "\n업무 중분류 체계 - 공공데이터 보유현황 정리 및 메타데이터 등록")
            print("\n업무 소분류 체계 - 기타")
            print("\n가상 페이지를 생성합니다...")
            sleep(2)
        else:
            print("*" * 50 + "\n프로그램을 종료합니다 다시 실행시켜 주십시오")
            sleep(2)
            sys.exit()

    def total_off_work(self):
        self.zero_off_work()
        self.first_off_work()
        self.second_off_work()
        self.end_off_work()

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(self.ID)
        self.driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

    def zero_off_work(self):
        self.driver.get(self.url)

        try:
            WEBSYSTEM.login(self)
            sleep(2)
        except:
            self.driver.find_element_by_xpath('/html/body/div[3]/button').click()
            sleep(2)
            WEBSYSTEM.login(self)
            sleep(2)

    def first_off_work(self):
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

    def second_off_work(self):
        self.driver.find_element_by_xpath('//*[@id="selCategory1"]/option[' + self.big_div + ']').click()
        self.driver.find_element_by_xpath('//*[@id="selCategory2"]/option[4]').click()
        self.driver.find_element_by_xpath('//*[@id="taEtcMemo"]').send_keys(self.content)
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

    def third_off_work(self):
        self.driver.find_element_by_xpath('//*[@id="iptUserName1"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="iptUserName2"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

    def end_off_work(self):
        self.driver.close()

        print("*" * 50 + "\n성공적으로 작업이 완료되었습니다")
        print("\n2초 뒤에 프로그램을 종료합니다")
        sleep(2)
        sys.exit()


if __name__ == '__main__':
    print("*" * 50 + "\n공공데이터 청년 인턴십 세무과 자동 퇴근 시스템 v0.3 (0.2 → 0.3)\n" + "*" * 50)
    person = WEBSYSTEM()
    schedule.every().day.at('18:00').do(person.total_off_work)

    while True:
        print("\n시간을 체크하고 있습니다... 현재 시간 : ", datetime.now())
        schedule.run_pending()
        sleep(1)

# 향후 해야할 일
# 로그인 시스템 구현
# 분류 체계 접근 및 이용
# 실측 체계 할 수 있도록 구현

# big_div = input('업무 중분류 체계 코드를 입력해주세요 (ex: 2) : ')
# small_div = input('업무 소분류 체계 코드를 입력해주세요 (ex: 2) : ')
# print("업무 중분류 체계는 다음과 같습니다")
# print(" - 공공데이터포털 목록등록체계 및 메타정보 점검 : 2") # DR0010
# print(" - 공공데이터 보유현황 정리 및 메타데이터 등록 : 3") # DR0011
# print(" - 공공데이터 목록 구성 및 개방 : 4") # DR0012
# print(" - 기관자체 개방포털 및 개방데이터 정비 : 6") # DR0014
# print("현재는 코드 3로 고정되어 있습니다 (테스트 중)")
