
from bs4 import BeautifulSoup
from selenium import webdriver

from time import sleep

url = "http://dt20chk.hyosungitx.com/main"

driver = webdriver.Chrome(
    executable_path="webdriver/chromedriver.exe"
)
driver.get(url)

def login():


try:
    pass
except:
    driver.find_element_by_xpath('/html/body/div[3]/button').click()

sleep(3)
driver.close()