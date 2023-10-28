from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('salam',salam),
    path('',index_page)
]
