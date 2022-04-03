from django.shortcuts import render


def index(request):
    return render(request, 'cad/index.html')


def patent_us_4661747(request):
    return render(request, "cad/cad_patent_us_4661747.html")
