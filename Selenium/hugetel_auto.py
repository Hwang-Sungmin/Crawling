from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

import random
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
sleep(0.5)
# 매니저 이름 불러와서 찍어 보자 

# 건마로 가서 2번째 페이지부터 댓글. 이렇게 달면 다른것도 다 통일 시킬 수 있을듯? 
# 오피
# 안마
# 건마 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[3]/a
# 휴게텔 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/a
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
sleep(0.5)

# 건마 - 서울 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[3]/ul/li[1]/div/div[2]/a
# 휴게텔 - 경기 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/ul/li[2]/div/div[2]/a

# 오피 - 강남 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[1]/div/div[2]/a
# 오피 - 비강남 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[2]/div/div[2]/a
# 오피 - 경기 : //*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[3]/div/div[2]/a

driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[3]/div/div[2]/a').click()                                   
sleep(0.5)


# 페이지가 넘어가는 건 xpath 가 다 동일함
# 건마 - 서울 - 2p : //*[@id="fboardlist"]/div[3]/ul/li[4]/a
# 휴게텔 - 경기 - 2p ://*[@id="fboardlist"]/div[3]/ul/li[4]/a
driver.find_element_by_xpath('//*[@id="fboardlist"]/div[3]/ul/li[4]/a').click()                                   
sleep(0.5)

# 매니저 명 가지고 와서 댓글 달기
# 첫번째 리스트 값에 따라 매니저명 변경

for i in range(2,21,1):
    s = str(i) 
    address = '//*[@id="list-body"]/li['+s+']/div[2]/a/div/div[2]/span'
    driver.find_element_by_xpath(address).click()
    sleep(0.5)
    # html 에 필요한 값들만 파싱하기 bs4로 사용해서
    req = driver.page_source
    soup = BeautifulSoup(req, 'html.parser')
    
    # 같은 닉넴이 있을때는 댓글을 달지 않게 만들기
    #shop = soup.select_one('.table > tbody > tr > td')
    #manager = soup.select_one('.table > tbody > .bg0 > td')
    # 리스트 형태
    data = soup.select('.table > tbody > tr > td')
    shop = data[0].text
    manager = data[1].text
    message = [
        shop+'의 '+manager +'언니와 즐달하신 후기 잘보고 가염',
        shop+'의 '+manager +'언니 저도 보고 싶네영~!',
        manager +'언니 죽여주네염~~~~~!',
        '후기보니 저두 ' + manager + '언니랑 놀구 싶네영~!',
        '당장 ' + shop +'에 예약해 ' + manager + '언니 봐야겠네영',
        manager +'언니가 죽입니당. 한 번 달려야겠네영ㅋㅋㅋ',
        '보장된 ' + shop +'이군요. ' + manager +'언니 후기 잘봤어영~!',
        '저두 달리고 싶네영 ㅠㅠ ' + manager + '언냐 좋네영ㅋㅋㅋㅋ',
        '즐달하신 후기 잘 보고 갑니당~! ' + manager + '언냐 기억해둘께영 ㅋㅋㅋㅋ',
        shop +'의 ' + manager + '언냐 좋네염 ㅋㅋㅋㅋㅋ',
        '후기보니 넘나 달리고 싶어집니당 '+manager+'언냐 후기 잘봤어염',
    ]    
    driver.find_element_by_name('wr_content').send_keys(random.choice(message))
    sleep(0.5)
    
    driver.find_element_by_xpath('//*[@id="btn_submit"]').click() 

    