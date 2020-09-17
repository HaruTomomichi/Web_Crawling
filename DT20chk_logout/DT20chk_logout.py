import sys
import schedule
import pandas as pd

from time import sleep
from selenium import webdriver
from datetime import datetime

class WEBSYSTEM:

    def __init__(self):
        self.ID = "기본"
        self.password = "기본"
        self.name = "홍길동"
        self.content = "기본"
        self.big_div, self.small_div = ['3', '2']
        self.url = 'http://dt20chk.hyosungitx.com/main'
        self.driver = webdriver.Chrome(
            executable_path="webdriver/chromedriver.exe"
        )

    def ready_for_act(self):
        self.one_more_chk()
        self.two_more_chk()
        self.third_more_chk()

    def one_more_chk(self):

        try:
            read_data = pd.read_csv('./Login_data.csv',index_col=0)
            self.ID = read_data['ID'].iloc[0]
            self.password = read_data['PASSWORD'].iloc[0]
            self.name = read_data['NAME'].iloc[0]
            print("로그인 정보를 확인하는데 성공하였습니다!")

        except FileNotFoundError:
            print("로그인 정보를 확인하는데 실패하였습니다...\n\n로그인 정보를 저장하겠습니다...\n")
            self.ID = input('아이디를 입력해주세요 : ')
            self.password = input('\n패스워드를 입력해주세요 : ')
            self.name = input('\n본인 성함을 입력해주세요 : ')

            save_data = {'ID':self.ID,'PASSWORD':self.password,'NAME':self.name}
            save_data = pd.DataFrame(save_data,index=[0])
            save_data.to_csv('Login_data.csv',encoding='utf-8-sig')
            print('\n로그인 정보를 저장하는 데에 성공하였습니다!')

    def two_more_chk(self):
        self.content = input("*" * 50 + '\n오늘 업무 내용을 입력해주세요 (최대 50자) : ')

    def third_more_chk(self):
        print("*" * 50 + "\nID = ", self.ID)
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

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(self.ID)
        self.driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

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
    print("*" * 50 + "\n공공데이터 청년 인턴십 세무과 자동 퇴근 시스템 v0.4 (0.2 → 0.3 → 0.4)\n" + "*" * 50)
    person = WEBSYSTEM()
    person.ready_for_act()
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
