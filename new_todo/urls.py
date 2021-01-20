from django.contrib import admin
from django.urls import include, path
from new_todo.views import index

urlpatterns = [
    path('',index ,name='index')
]
