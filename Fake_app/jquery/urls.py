from django.urls import path
from . import views as jq_views

app_name = 'jq'
urlpatterns = [
    path('', jq_views.index, name="index"),
    path('find/', jq_views.find, name="find"),
]