from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Database
import requests


# Create your views here.
def index(request):
    return render(request, 'exam/main.html')

def push(request):
    DB = Database()
    DB.a = request.GET["Aaa"]
    DB.b = request.GET["Abb"]
    DB.c = request.GET["Acc"]
    DB.save()

    a = DB.a
    b = DB.b
    c = DB.c

    print(a)
    print(b)
    print(c)
    return render(request, 'exam/call.html')
