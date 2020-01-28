from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

id = "whang4239"
pwd = 'h57357'
driver = webdriver.Chrome('C:\Crawling\Selenium\chromedriver.exe')
driver.get('http://mbam4.com/')
driver.find_element_by_name('mb_id').send_keys(id)
sleep(0.3)
driver.find_element_by_name('mb_password').send_keys(pwd)
driver.find_element_by_xpath('//*[@id="miso_sidelogin"]/div/div[1]/button').click()

# Crawlings
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
data = soup.select('.paddingssang')

print(data[3].text)
