from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"), #127.0.0.:8000
    path('about/', views.about, name="about"), #127.0.0.:8000/about
    path('items/', views.items, name="items"), #127.0.0.:8000/items
    path('item/<int:id>', views.item_page, name="item"), #127.0.0.:8000/item/int:id
]
