from django.contrib import admin
from django.urls import path
from . import views
from blog.views import blogpost, blogsec

urlpatterns = [
    path("", views.index, name="HonvinHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path("blogsec/<int:id>", views.blogsec, name="blogsec")
   ]