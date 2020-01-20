from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

# driver 연결
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')

driver.get('http://mbam3.com/')

# 아이디와 비밀번호를 입력
sleep(0.3)
driver.find_element_by_name('mb_id').send_keys('whang4239')
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys('h57357')

# Xpath 사용해서 onclick 버튼 실행
# 로그인
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()
sleep(0.5)
# 매니저 이름 불러와서 찍어 보자 

# 오피스텔 클릭
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
sleep(0.5)

#서울 ~ 제주도 [10]
for i in range(1,10,1):
    s = str(i)
    region = int(s)
    address_region = '//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li['+s+']/div/div[2]/a'
                    #//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[2]/div/div[2]/a/img[1]
    driver.find_element_by_xpath(address_region).click()
    sleep(0.5)

    # 일반 게시글 19개 강남은  14 ~ 33 위쪽은 이벤트   
    if( region == 1 ):
        for j in range(15, 34, 1):
            k = str(j)
            address_comment = '//*[@id="list-body"]/li['+k+']/div[2]/a/div/div[2]/span/b'
            driver.find_element_by_xpath(address_comment).click()
            sleep(0.5)
            req = driver.page_source
            soup = BeautifulSoup(req, 'html.parser')
            data = soup.select('.table > tbody > tr > td')
            shop = data[0].text
            manager = data[1].text

            if( j % 2 == 0 ):
                message = shop+'의 '+manager +'언니와 즐달하신 후기 잘보고 가염'
                driver.find_element_by_name('wr_content').send_keys(message)
                sleep(0.5)
                driver.find_element_by_xpath('//*[@id="btn_submit"]').click() 
            
            else:
                message = shop+'의 '+ manager +'언니 저도 보고 싶네영~!'
                driver.find_element_by_name('wr_content').send_keys(message)
                sleep(0.5)
                driver.find_element_by_xpath('//*[@id="btn_submit"]').click()    

