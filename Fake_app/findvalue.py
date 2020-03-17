from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from django.http.response import HttpResponse
# selenium
from selenium import webdriver
from time import sleep
import random
# Create your views here.
print("숫자를 입력 ")
types = input("종목 : ")
region = input("지역 : ")


id = 'whang4239'
pwd = 'h57357'
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')
driver.get('http://dalbam1.com/')
driver.find_element_by_name('mb_id').send_keys(id)
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()


#//*[@id="MB-main-header"]/aside/section/ul/li[5]/ul/li[1]/div/div[2]/a/img[1]
# 종목, 지역으로 이동
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li['+types+']/a').click()
sleep(0.3)
driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li['+types+']/ul/li['+region+']/div/div[2]/a/img[1]').click()

# 2번째 페이지로 이동
driver.find_element_by_xpath('//*[@id="fboardlist"]/div[3]/ul/li[4]/a').click()                                   
sleep(0.5)

for j in range(4,7,1):
    count = str(j)
    address = '//*[@id="fboardlist"]/div[3]/ul/li['+count+']/a'
    driver.find_element_by_xpath(address).click()                                   
    sleep(0.5)

    for i in range(2,21,1):
        s = str(i)
        driver.find_element_by_xpath('//*[@id="list-body"]/li['+s+']/div[2]/a[3]/div/div[2]/span').click()
        sleep(0.3)
        # //*[@id="list-body"]/li[20]/div[2]/a[5]/div/div/span
        # Crawlings
        req = driver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        #data = soup.select('.paddingssang')
        # 도토리
        #print(data[3].text)

        # 데이터 파싱
        data = soup.select('.mb_reviewer > .review_head_body > div '  )
        # 매니저    
        manager = data[2].text
        if manager :
            manager = manager.replace("매니져 예명","")
            manager = manager.replace(" ","")
            manager = manager.replace("\n","")
            manager = manager.replace("\t","")
        else:
            pass
        # 가게
        shop = data[0].text
        shop = shop.replace("업소명","") 
        shop = shop.replace("출근부","") 
        shop = shop.replace("후기","") 
        shop = shop.replace(" ","") 
        shop = shop.replace("\n","") 
        shop = shop.replace("\t","") 
         
        # 지역을 구분짓기 위해 
        region = ['강남','역삼','선릉','논현','신림','건대','잠실','사당','이수','구로','중랑','서초',
            '강동','강서','노원','마포','송파','수유','신촌','쌍문','은평','창동','홍대','성북',
            '고양','광명','구리','군포','김포','동탄','병점','분당','송파','송탄','수원','시흥','성남','안성',
            '안산','안양','야탑','양주','여주','연천','영통','이천','일산','판교','평촌','평택','포승','포천',
            '하남','화정','향남','계양','구월','부천','부평','인천','주안']
        # for k in range(len(shop)) :

        if shop[0:2] in region:
            shop = shop[0:2] + ' ' + shop[2:]    
        else:
            shop = shop[0:3] + ' ' + shop[3:]    

        print(shop)
        print(manager)
        if manager == '콩지' or manager == '하얀' or manager == '아오이' or manager == '한별' :
            driver.find_element_by_name('wr_content').send_keys('보고 싶은 언냐네요. ')
            print(manager + ' 찾았습니다')
            sleep(5)
            pass
        #bj
        #https://javmovies.mobi/mov/45142/%EC%9D%B8%EB%B0%A9-bj%EC%BD%94%EC%BD%94%EC%96%91.html
        #https://video.fc2.com/a/content/20190219pZ3JH7T3
        #https://video.fc2.com/a/content/201701036JgdTexS
        #https://video.fc2.com/a/content/20170103rrQbuQs4
        #https://video.fc2.com/a/content/20170525tNAbWRCU
        #https://video.fc2.com/ko/a/content/20150331F20psnZ7
        #https://video.fc2.com/a/content/2019102029wKXMfA
        #https://video.fc2.com/a/content/20191015P4qE0ztr
        #https://video.fc2.com/a/content/20191013ugYPf7gE
        #https://video.fc2.com/a/content/20190813vcYH7UQp 사슴
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
        # 같은 아이디 제거
        finds= soup.select('.media-body > .media-heading > b > a > span.member')
        keep = []
        nick = ' 오징어대마왕'        
        
        for j in range(len(finds)):
            keep.append(finds[j].text)
        
        if( nick in keep):
        # 있을땐 수정 후에 댓글 : id 값이 계속 변경되서 불가
            driver.find_element_by_name('wr_content').send_keys('여기는 그냥 지나칠꺼야')
            sleep(3)
            pass
        
        else:
            sleep(0.5)
            driver.find_element_by_name('wr_content').send_keys(random.choice(message))
            sleep(3)
            driver.find_element_by_xpath('//*[@id="btn_submit"]').click()
            sleep(3)
        