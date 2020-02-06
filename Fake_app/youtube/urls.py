from django.urls import path
from . import views as u_views

app_name = 'youtube'
urlpatterns = [
    path('', u_views.index, name="index"),
]