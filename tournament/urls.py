from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
path('', views.mainpage, name='mainpage'),
path('signup', views.signup, name='signup'),
path('login', views.login_user, name='login_user'),
path('home', views.home, name='home'),
path('tournament', views.tournament, name='tournament'),
path('gallery', views.gallery, name='gallery'),
path('contact', views.contact, name='contact'),
path('logout', views.logout, name='logout'),

]
