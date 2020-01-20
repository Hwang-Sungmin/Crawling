# 로그인해서 인사말을 자동화

from selenium import webdriver
from time import sleep

# driver 연결
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')

# 네이버 로그인 접속
driver.get('http://mbam3.com/')

# 아이디와 비밀번호를 입력
sleep(0.3)
driver.find_element_by_name('mb_id').send_keys('whang4239')
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys('h57357')

# Xpath 사용해서 onclick 버튼 실행
# 로그인
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()

# 실행

#가입인사
sleep(0.5)
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside/section/ul/li[15]/div/a/div/span').click()
sleep(0.5)
driver.find_element_by_xpath('//*[@id="fboardlist"]/div[3]/ul/li[4]/a').click()
sleep(0.5)
for i in range(2,20):
    # 정수를 문자로 바꾸고 다시 문자로 바꿔야 하나?
    s = str(i)
    check = int(s)
    address = '//*[@id="list-body"]/li['+s+']/div[2]/a'
    driver.find_element_by_xpath(address).click()
    if( check % 2 == 0 ):
        sleep(0.5)
        driver.find_element_by_name('wr_content').send_keys('안녕하세요. 열심히 활동합시다')
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
    else :
        sleep(0.5)
        driver.find_element_by_name('wr_content').send_keys('반갑습니다. 어서오세요')
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
