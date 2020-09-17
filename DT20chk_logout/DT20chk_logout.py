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

        print("*" * 50 + '\n업무 중분류 체계는 다음과 같습니다')
        print("\n - 공공데이터포털 목록등록체계 및 메타정보 점검 : 2") # DR0010
        print("\n - 공공데이터 보유현황 정리 및 메타데이터 등록 : 3") # DR0011
        print("\n - 공공데이터 목록 구성 및 개방 : 4") # DR0012
        print("\n - 기관자체 개방포털 및 개방데이터 정비 : 6") # DR0014
        self.big_div = str(input('\n업무 중분류 체계 코드를 입력해주세요 (ex: 2) : '))

        if self.big_div != '2' and self.big_div != '3' and self.big_div != '4' and self.big_div != '6':
            print("*" * 50 + '\n업무 중분류 코드 입력 오류입니다! 기본값으로 진행하겠습니다...')
            print('\n - 업무 중분류 체계 : 공공데이터 보유현황 정리 및 메타데이터 등록')
            print('\n - 업무 소분류 체계 : 기타')

        self.content = input("*" * 50 + '\n오늘 업무 내용을 입력해주세요 (최대 50자) : ')

    def third_more_chk(self):
        print("*" * 50 + "\nID : ", self.ID)
        print("\npassword : ", self.password)
        print("\n성함 : ", self.name)
        WEBSYSTEM.print_work_code(self)
        print("\n업무 내용 : ", self.content)

        answer = input("\n입력하신 내용이 다음과 같습니까? (y/n) : ")

        if answer == 'y':
            print("*" * 50 + '\n확인을 완료하였습니다! 오후 6시에 작업을 시작합니다...')
        else:
            print("*" * 50 + "\n프로그램을 종료합니다 다시 실행시켜 주십시오")
            sleep(2)
            sys.exit()

    def print_work_code(self):
        if self.big_div == '2':
            print("\n업무 중분류 코드 : 공공데이터포털 목록등록체계 및 메타정보 점검") # DR0010
        elif self.big_div == '4':
            print("\n업무 중분류 코드 : 공공데이터 목록 구성 및 개방") # DR0012
        elif self.big_div == '6':
            print("\n업무 중분류 코드 : 기관자체 개방포털 및 개방데이터 정비") # DR0014
        else:
            print("\n업무 중분류 코드 : 공공데이터 보유현황 정리 및 메타데이터 등록")  # DR0011

        print("\n업무 소분류 코드 : 기타")

    def total_off_work(self):
        print("\n가상 페이지를 생성합니다...")
        sleep(2)
        self.url = 'http://dt20chk.hyosungitx.com/main'
        self.driver = webdriver.Chrome(
            executable_path="webdriver/chromedriver.exe"
        )
        self.driver.get(self.url)

        # zero_off_work

        self.driver.get(self.url)

        try:
            self.driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(self.ID)
            self.driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
            sleep(2)
        except:
            self.driver.find_element_by_xpath('/html/body/div[3]/button').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(self.ID)
            self.driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(self.password)
            self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
            sleep(2)

        # first_off_work

        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # second_off_work

        self.driver.find_element_by_xpath('//*[@id="selCategory1"]/option[' + self.big_div + ']').click()
        self.driver.find_element_by_xpath('//*[@id="selCategory2"]/option[' + self.small_div + ']').click()

        try:
            self.driver.find_element_by_xpath('//*[@id="taEtcMemo"]').send_keys(self.content)
        except:
            pass
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # third_off_work

        self.driver.find_element_by_xpath('//*[@id="iptUserName1"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="iptUserName2"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # end_off_work

        self.driver.close()
        print("*" * 50 + "\n성공적으로 작업이 완료되었습니다")
        print("\n2초 뒤에 프로그램을 종료합니다")
        sleep(2)

        sys.exit()

if __name__ == '__main__':
    print("*" * 50 + "\n공공데이터 청년 인턴십 자동 퇴근 시스템 v0.4 (0.2 → 0.3 → 0.4)\n" + "*" * 50)
    person = WEBSYSTEM()
    person.ready_for_act()
    schedule.every().day.at('18:00').do(person.total_off_work)

    while 1:
        print("\n시간을 체크하고 있습니다... 현재 시간 : ", datetime.now())
        schedule.run_pending()
        sleep(1)

# 향후 해야할 일
# 분류 체계 접근 및 이용
# 실측 체계 할 수 있도록 구현

        # if self.big_div == '2':
        #     print("*" * 50 + '\n해당 업무 소분류 체계는 다음과 같습니다')
        # elif self.big_div == '3':
        #     print("*" * 50 + '\n해당 업무 소분류 체계는 다음과 같습니다')
        # elif self.big_div == '4':
        #     print("*" * 50 + '\n해당 업무 소분류 체계는 다음과 같습니다')
        # elif self.big_div == '6':
        #     print("*" * 50 + '\n해당 업무 소분류 체계는 다음과 같습니다')
