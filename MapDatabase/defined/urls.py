from django.urls import path
from . import views

urlpatterns = [
    path('', views.define_home, name="home"),
]
