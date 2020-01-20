from selenium import webdriver
from time import sleep

# driver 연결
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')

# 네이버 로그인 접속
driver.get('')

# 아이디와 비밀번호를 입력
id = 'hsmhsm511'
pw = '!ghkdtjdals511'
sleep(0.5)
driver.find_element_by_name('mb_id').send_keys('whang4239')
sleep(0.5)
driver.find_element_by_name('mb_password').send_keys('h57357')

# Xpath 사용해서 onclick 버튼 실행
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()

sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div/div[1]/section/div/form/div[1]/ul/li[2]/div[1]/a/div[1]/div/div[2]/b[1]').click()
