
from django.contrib import admin
from django.urls import path
from domain import views
urlpatterns = [
    path('', views.home),

]
