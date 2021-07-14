from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="HonvinHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome")
   ]