from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

# driver 연결
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')

# 네이버 로그인 접속
driver.get('http://mbam3.com/')

# 아이디와 비밀번호를 입력
id = 'hsmhsm511'
pw = '!ghkdtjdals511'
sleep(0.3)
driver.find_element_by_name('mb_id').send_keys('whang4239')
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys('h57357')

# Xpath 사용해서 onclick 버튼 실행
# 로그인
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()
sleep(0.5)
# 매니저 이름 불러와서 찍어 보자 

# 휴게텔
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside/section/ul/li[4]').click()
sleep(0.5)

# 휴게텔 - 서울
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside/section/ul/li[4]/ul/li[1]/div/div[2]/a').click()
sleep(0.5)

# 매니저 명 가지고 와서 댓글 달기
# 첫번째 리스트 값에 따라 매니저명 변경

for i in range(5,24,1):
    s = str(i)
    check = int(s) 
    address = '//*[@id="list-body"]/li['+s+']/div[2]/a/div/div[2]/span'
    driver.find_element_by_xpath(address).click()
    sleep(0.5)
    # html 에 필요한 값들만 파싱하기 bs4로 사용해서
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    #shop = soup.select_one('.table > tbody > tr > td')
    #manager = soup.select_one('.table > tbody > .bg0 > td')
    # 리스트 형태
    data = soup.select('.table > tbody > tr > td')
    shop = data[0].text
    manager = data[1].text
    if( check % 2 == 0 ):
        message = manager +'언니와 즐달하신 후기 잘보고 가염'
        driver.find_element_by_name('wr_content').send_keys(message)
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
    else:
        message = manager +'언니 저도 보고 싶네영~!'
        driver.find_element_by_name('wr_content').send_keys(message)
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
