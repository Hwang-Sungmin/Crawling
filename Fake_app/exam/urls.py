from django.urls import path
from . import views as ex_views

app_name = 'exam'
urlpatterns = [
    path('', ex_views.index, name="main"),
    path('push', ex_views.push, name="push"),
]