from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.blog,name="blog"),
    path('blog/<str:slug>',views.blogPost,name="blogPost"),
    path('category/<str:cat>',views.category,name="category")
]
