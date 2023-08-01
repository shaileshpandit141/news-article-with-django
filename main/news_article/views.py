import requests
from django.shortcuts import render
from django.http import Http404

api_key = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=3553f00c26ac42c9aba89b3adc42d59a"
only_india_api_key = "https://newsapi.org/v2/top-headlines?country=in&apiKey=3553f00c26ac42c9aba89b3adc42d59a"
only_us_api_key = "https://newsapi.org/v2/top-headlines?country=us&apiKey=3553f00c26ac42c9aba89b3adc42d59a"

# Create your views here.
def home(request):
    try:
        response = requests.get(api_key).json()["articles"]
        return render(request, "news_article/home.html", {
            "response": response
        })
    except:
        raise Http404()

def india_news(request):
    try:
        response = requests.get(only_india_api_key).json()["articles"]
        return render(request, "news_article/home.html", {
            "response": response
        })
    except:
        raise Http404()

def us_news(request):
    try:
        response = requests.get(only_us_api_key).json()["articles"]
        return render(request, "news_article/home.html", {
            "response": response
        })
    except:
        raise Http404()

def detail(request, data):
    detail_data = requests.get(api_key).json()["articles"]
    for detail_data in detail_data:
        if data == detail_data["publishedAt"]:
            return render(request, "news_article/detail_page.html", {
                "detail_data": detail_data,
            })
    else:
        raise Http404
        
def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")