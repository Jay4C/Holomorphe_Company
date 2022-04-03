from django.shortcuts import render


def index(request):
    return render(request, "index/index.html")


def ads_text(request):
    return render(request, "index/ads.txt")
