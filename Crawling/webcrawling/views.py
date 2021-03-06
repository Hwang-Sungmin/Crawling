from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import data
# Create your views here.

def index(request):
   
    return render(request, 'index.html')

def nfind(request):
    # 네이버 검색시 base가 되는 url 
    baseUrl ='https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
    # index의 검색어 받아오기   
    search = request.GET['nname']
    url = baseUrl + search
    html = requests.get(url).text 
    # html을 긁어옴
    soup = BeautifulSoup(html, "html.parser")
    title = soup.find_all(class_="sh_blog_title")
    # print(title)
    # 값이 있을때
    if title:
        for i in title:
            datas = data()
            datas.title = i.attrs['title']
            datas.web = i.attrs['href']
            datas.save()
        alldata = data.objects.all()
        context = {
            'alldata' : alldata,
        }    
        return render(request, 'index.html', context)    
    else :
        return render(request, 'error.html')

def wfind(request):
    baseUrl = 'https://ko.wikipedia.org/wiki/'
    search = request.GET['wname']
    url = baseUrl + search
    html = requests.get(url).text 
    # html을 긁어옴
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    return render(request, 'index.html')


def delete_one(request, data_id):
    datas = data.objects.get(id=data_id)
    datas.delete()

    datas = data.objects.all()
    context = {
        'alldata' : datas,
    }    

    return render(request, 'index.html', context)


def delete_all(request):
    data_all = data.objects.all()
    data_all.delete()
    return render(request, 'index.html')

