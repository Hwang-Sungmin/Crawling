from selenium import webdriver
from time import sleep
# driver 연결
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')

# 로그인 접속
driver.get('http://kissinfo.co.kr/')
# 아이디와 비밀번호를 입력
sleep(0.3)
driver.find_element_by_name('mb_id').send_keys('hsm511')
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys('h57357')
sleep(0.3)
driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/form/table/tbody/tr/td[2]/input').click()
# 
# /html/body/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/form/table/tbody/tr/td[2]/input