from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
app_name = "res"
urlpatterns = [
    path("upload",views.upload,name ="upload"),
    path("test",views.test,name = "test"),
    path("check",views.check),
    path("detail/<int:id>",views.detail),
    path("download/<int:id>",views.download),


]