from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from time import sleep
import random

# Create your views here.
def index(request):
    return render(request, 'mbam/index.html')

def login(request):
    id = request.POST['id']
    pwd = request.POST['pwd']
    select = request.POST['comment']
    driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')
    driver.get('http://mbam4.com/')
    sleep(0.3)
    driver.find_element_by_name('mb_id').send_keys(id)
    sleep(0.3)
    driver.find_element_by_name('mb_password').send_keys(pwd)
    driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()
    print(id , pwd, select)
    
    # 강남
    if (select == 'opgang'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)  
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[1]/div/div[2]').click()
        sleep(0.5)
    #비강남
    elif(select == 'opbi'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[2]/div/div[2]').click()
        sleep(0.5)
    #경기
    elif(select == 'opkk'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[3]/div/div[2]').click()
        sleep(0.5)
    #인부천
    elif(select == 'opinbu'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[4]/div/div[2]').click()
        sleep(0.5)
    #충청
    elif(select == 'opchung'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[5]/div/div[2]').click()
        sleep(0.5)
    #전라
    elif(select == 'opjun'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[6]/div/div[2]').click()
        sleep(0.5)
    #경상
    elif(select == 'opkyungs'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[7]/div/div[2]').click()
        sleep(0.5)
    #대구
    elif(select == 'opde'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[8]/div/div[2]').click()
        sleep(0.5)
    #제주
    elif(select == 'opje'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[2]/ul/li[9]/div/div[2]').click()
        sleep(0.5)
    
    #휴게텔 서울, 경기, 인천
    elif(select == 'hges'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/ul/li[1]/div/div[2]/a').click()
        sleep(0.5)
    elif(select == 'hgek'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/ul/li[2]/div/div[2]/a').click()
        sleep(0.5)
    elif(select == 'hgei'):
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/a').click()
        sleep(0.5)        
        driver.find_element_by_xpath('//*[@id="MB-main-header"]/aside[1]/section/ul/li[4]/ul/li[3]/div/div[2]/a').click()
        sleep(0.5)

    else:
        return render(request, 'error.html')
       
    driver.find_element_by_xpath('//*[@id="fboardlist"]/div[3]/ul/li[4]/a').click()                                   
    sleep(0.5)

    for i in range(2,22,1):
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
        # 도토리개수
        dotori = soup.select('.paddingssang')
        dotori = dotori[3].text

        finds= soup.select('.media-body > .media-heading > b > a > span.member')
        #finds_all  = soup.select('.media-body > .media-heading > b > a > span.member')
        # keep 이라는 배열은 선언후 크롤링한 결과값을 저장
        nick = ' 오징어대마왕'
        #print(finds.text)
        keep = []
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
            end = '끝냈습니다.' 

    return render(request, 'mbam/index.html', context = {
        'end' : end,
        'dotori' : dotori,
    })


