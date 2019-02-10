'''
Created on 2019. 1. 27.

@author: user
'''
from django.urls import path
from .views import *

app_name = 'cl'
#기본주소 : 127.0.0.1:8000/cl/
urlpatterns = [
    #127.0.0.1:8000/cl/signup/
    path('signup/',signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
    ]