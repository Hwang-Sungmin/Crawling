from django.urls import path
from . import views as views_web

app_name = 'webcrawling'

urlpatterns = [
    path('', views_web.index, name="index"),
    path('nfind/', views_web.nfind, name="nfind"),
    path('wfind/', views_web.wfind, name="wfind"),
    #path('articles/<int:article_id>/delete/', article_views.delete, name="delete"),
    #path('find/<int:data_id>/delete/', views_web.delete, name="delete"),
    path('delete_all/', views_web.delete_all, name="delete_all"),
    path('<int:data_id>/delete_one/', views_web.delete_one, name="delete_one"),
]
