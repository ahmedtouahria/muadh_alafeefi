from django.urls import path

from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('get_person/',get_person,name="get_person"),
    path('send_message/',send_message,name="send_message"),

    
]
