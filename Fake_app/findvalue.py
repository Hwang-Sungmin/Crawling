from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

import random

id = "whang4239"
pwd = 'h57357'
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')
driver.get('http://mbam5.com/')
driver.find_element_by_name('mb_id').send_keys(id)
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()

# 오피스텔 -> 강남
#driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
#sleep(0.3)
#driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[1]/div/div[2]/a/img[1]').click()

# 건마 -> 서울
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[3]/a').click()
sleep(0.3)
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[3]/ul/li[1]/div/div[2]/a/img[1]').click()

# 2번째 페이지로 이동
driver.find_element_by_xpath('//*[@id="fboardlist"]/div[3]/ul/li[4]/a').click()                                   
sleep(0.5)


# 첫번째 후기
# 첫번째는 공지 이기때문에 형식상 2번째 후기 li[2] <== 여기가 후기
driver.find_element_by_xpath('//*[@id="list-body"]/li[2]/div[2]/a[3]/div/div[2]/span').click()
sleep(0.3)
# Crawlings
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
#data = soup.select('.paddingssang')
# 도토리
#print(data[3].text)
#.review_head_body

# 데이터 파싱
data = soup.select('.mb_reviewer > .review_head_body > div '  )
# 매니저
manager = data[2].text
manager = manager.replace("매니져 예명","")
manager = manager.replace(" ","")
manager = manager.replace("\n","")
manager = manager.replace("\t","")
# 가게
shop = data[0].text
shop = shop.replace("업소명","") 
shop = shop.replace("출근부","") 
shop = shop.replace("후기","") 
shop = shop.replace(" ","") 
shop = shop.replace("\n","") 
shop = shop.replace("\t","") 

message = [
    shop+'의 '+manager +'언니와 즐달하신 후기 잘보고 가염',
    shop+'의 '+manager +'언니 저도 보고 싶네영~!',
    manager +'언니 죽여주네염~~~~~!',
    manager +'언니랑 즐달했네여~!',
    '후기보니 저두 ' + manager + '언니랑 놀구 싶네영~!',
    '당장 ' + shop +'에 예약해 ' + manager + '언니 봐야겠네영',
    manager +'언니가 죽입니당. 한 번 달려야겠네영ㅋㅋㅋ',
    '보장된 ' + shop +'이군요. ' + manager +'언니 후기 잘봤어영~!',
    '저두 달리고 싶네영 ㅠㅠ ' + manager + '언냐 좋네영ㅋㅋㅋㅋ',
    '즐달하신 후기 잘 보고 갑니당~! ' + manager + '언냐 기억해둘께영 ㅋㅋㅋㅋ',
    shop +'의 ' + manager + '언냐 좋네염 ㅋㅋㅋㅋㅋ',
    '후기보니 넘나 달리고 싶어집니당 '+manager+'언냐 후기 잘봤어염',
    '부럽습니당 '+manager+'언냐 후기 잘봤어염',
    manager + '언냐 후기 잘봤어염',
    '즐달하신 후기 잘 보고 갑니당~!',
]

keep = []
nick = ' 오징어대마왕'        
finds= soup.select('.media-body > .media-heading > b > a > span.member')
for j in range(len(finds)):
    keep.append(finds[j].text)

if( nick in keep):
    # 있을땐 수정 후에 댓글 : id 값이 계속 변경되서 불가
    driver.find_element_by_name('wr_content').send_keys('여기는 그냥 지나칠꺼야')
    sleep(3)
    pass 
else:
    driver.find_element_by_name('wr_content').send_keys(random.choice(message))
    sleep(3)
    driver.find_element_by_xpath('//*[@id="btn_submit"]').click()

sleep(3)    
driver.find_element_by_xpath('//*[@id="at-main"]/div[2]/div[6]/div[1]/a[2]').click()
#     print(keep)    