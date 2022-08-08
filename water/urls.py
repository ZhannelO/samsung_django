

from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('homepage',views.home_screen_view, name='home_screen_view'),
    path('',views.homelogin, name='home_login'),
    path('signup',views.signup, name="signup"), #register
    path('signin',views.signin, name="signin"), #login
    path('signout',views.signout, name="sign-out"), #log out
    path('profile', views.profile, name='profile') # profile
]
