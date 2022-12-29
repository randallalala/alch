from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="cocktails-home"),
    path('about', views.about, name="cocktails-about"),
]
