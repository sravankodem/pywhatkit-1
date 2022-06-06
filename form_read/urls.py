from django.contrib import admin
from django.urls import path
from  . import views


urlpatterns = [
    path('', views.showform, name='showform'),
    path('reply',views.reply, name='reply')
]