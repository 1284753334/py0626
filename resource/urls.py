from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("upload",views.upload),
    path("test",views.test),
    path("check",views.check),


]