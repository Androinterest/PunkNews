from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('about',views.about,name="about"),
    path('contact',views.contacts,name="contacts"),
    path('search',views.search,name="search"),
    path('signup',views.signup,name="signup"),
    path('login',views.userlogin,name="userlogin"),
    path('logout',views.userlogout,name="userlogout"),
    path('account',views.myaccount,name="myaccount"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('updateprofile',views.updateprofile,name="updateprofile"),
    path('change_pass',views.changepass,name="changepass"),
]
