from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.index,
         name='index'),
    path('patent_us_4661747',
         views.patent_us_4661747,
         name='patent_us_4661747'),
]
