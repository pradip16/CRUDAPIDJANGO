from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("add_data/",views.add_data,name="add_data"),
    path("delete_data/",views.delete_data,name="delete_data"),
    path("update_data/",views.update_data,name="update_data"),
]
