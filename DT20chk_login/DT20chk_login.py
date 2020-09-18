from pandas import read_csv,DataFrame
from sys import exit
from time import sleep
from selenium import webdriver

class WEBSYSTEM:
    def __init__(self):
        self.ID = "기본"
        self.password = "기본"
        self.name = "홍길동"

    def ready_for_act(self):
        self.one_more_chk()
        self.third_more_chk()

    def one_more_chk(self):
        try:
            read_data = read_csv('./Login_data.csv',index_col=0)
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
            save_data = DataFrame(save_data,index=[0])
            save_data.to_csv('Login_data.csv',encoding='utf-8-sig')
            print('\n로그인 정보를 저장하는 데에 성공하였습니다!')

    def third_more_chk(self):
        print("*" * 50 + "\nID : ", self.ID)
        print("\npassword : ", self.password)
        print("\n성함 : ", self.name)

        answer = input("\n입력하신 내용이 다음과 같습니까? (y/n) : ")

        if answer == 'y':
            print("*" * 50 + '\n확인을 완료하였습니다! 출근 작업을 시작합니다...')
        else:
            print("*" * 50 + "\n프로그램을 종료합니다 다시 실행시켜 주십시오")
            sleep(2)
            exit()

    def total_on_work(self):
        print("\n가상 페이지를 생성합니다...")
        sleep(2)

        url = 'http://dt20chk.hyosungitx.com/main'
        driver = webdriver.Chrome(
            executable_path="webdriver/chromedriver.exe"
        )
        driver.get(url)

        # zero_on_work

        try:
            self.login(driver)
            sleep(2)
        except:
            driver.find_element_by_xpath('/html/body/div[3]/button').click()
            sleep(2)
            self.login(driver)
            sleep(2)

        # first_on_work

        driver.find_element_by_xpath('//*[@id="iptUserName1"]').send_keys(self.name)
        driver.find_element_by_xpath('//*[@id="iptUserName2"]').send_keys(self.name)
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # second_on_work

        driver.find_element_by_xpath('//*[@id="chkAgree1"]').click()
        driver.find_element_by_xpath('//*[@id="chkAgree2"]').click()
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # third_on_work

        driver.find_element_by_xpath('//*[@id="rdSurvey13"]').click()
        driver.find_element_by_xpath('//*[@id="chkSurvey10"]').click()
        driver.find_element_by_xpath('//*[@id="rdSurvey33"]').click()
        driver.find_element_by_xpath('//*[@id="rdSurvey42"]').click()
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
        sleep(2)

        # end_off_work

        driver.close()
        print("*" * 50 + "\n성공적으로 작업이 완료되었습니다")
        print("\n2초 뒤에 프로그램을 종료합니다")
        sleep(2)

        exit()

    def login(self,driver):
        driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys(self.ID)
        driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys(self.password)
        driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

if __name__ == '__main__':
    print("*" * 50 + "\n공공데이터 청년 인턴십 자동 출근 시스템 v0.4\n" + "*" * 50)
    print(" - 만든이 : 부산 남구청\n")
    print(" - Special Thanks to : 창원 성산구청")
    print("*" * 50)

    person = WEBSYSTEM()
    person.ready_for_act()
    person.total_on_work()
