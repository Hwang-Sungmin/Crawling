from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create your views here.

def index(request):
    driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')
    driver.get('https://www.youtube.com/')
    time.sleep(2)

    body = driver.find_element_by_tag_name("body")

    num_of_pagedowns = 50

    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        num_of_pagedowns -= 1
        try:
            driver.find_element_by_xpath("""//*[@id="feed-main-what_to_watch"]/button""").click()
        except:
            None

    html = driver.page_source        
    soup = BeautifulSoup(html, "lxml")
    titles = soup.find_all('h3')

    for title in titles:
        print(title)
    return render(request, 'youtube/index.html')