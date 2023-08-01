from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("country/india", views.india_news, name="india_news"),
    path("country/usa", views.us_news, name="us_news"),
    path("<str:data>", views.detail, name="detail-page"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register")
]
