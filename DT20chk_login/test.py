from time import sleep
from selenium import webdriver

def login(driver):
    driver.find_element_by_xpath('//*[@id="iptUser_id"]').send_keys('dt2003258')
    driver.find_element_by_xpath('//*[@id="iptUser_pass"]').send_keys('naruto881')
    driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

url = 'http://dt20chk.hyosungitx.com/covidCheck'
driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

try:
    login(driver)
    sleep(2)
except:
    driver.find_element_by_xpath('/html/body/div[3]/button').click()
    sleep(2)
    login(driver)
    sleep(2)

driver.get(url)

driver.find_element_by_xpath('//*[@id="js-page-content"]/div/div[1]/div/label').click()
driver.find_element_by_xpath('//*[@id="js-page-content"]/div/div[2]/div/label').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
sleep(2)

if driver.find_element_by_xpath('//*[@id="divSurvey1"]/div/div[3]/label').text == '03. 아니오':
    driver.find_element_by_xpath('//*[@id="divSurvey1"]/div/div[3]/label').click()
sleep(1)

driver.execute_script("window.scroll(0, 300);")
sleep(1)
if driver.find_element_by_xpath('//*[@id="divSurvey2"]/div/div[10]/label').text == '09. 방문하지 않음':
    driver.find_element_by_xpath('//*[@id="divSurvey2"]/div/div[10]/label').click()
sleep(1)

driver.execute_script("window.scroll(0, 600);")
sleep(1)
if driver.find_element_by_xpath('//*[@id="divSurvey3"]/div/div[3]/label').text == '03. 방문한 적 없습니다.':
    driver.find_element_by_xpath('//*[@id="divSurvey3"]/div/div[3]/label').click()
sleep(1)

driver.execute_script("window.scroll(0, 900);")
sleep(1)
if driver.find_element_by_xpath('//*[@id="divSurvey4"]/div/div[2]/label').text == '02. 아니오, 증상이 없습니다.':
    driver.find_element_by_xpath('//*[@id="divSurvey4"]/div/div[2]/label').click()
sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)




sleep(1000)
driver.close()