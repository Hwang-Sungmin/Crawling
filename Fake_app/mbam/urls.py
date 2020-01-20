from django.urls import path
from . import views as mbam_views

app_name = 'mbam'
urlpatterns = [
    path('', mbam_views.index, name="index"),
    path('login/', mbam_views.login, name="login"),
]