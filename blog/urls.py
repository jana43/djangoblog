from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings




from django.conf.urls.static import static
urlpatterns = [
    path('',views.home , name = "home"),
    path('about&contact',views.about , name = "about"),
    path('report',views.report_data , name = "report_data"),
    path('all',views.all , name = "all"),
    path('privacy',views.privacy , name = "privacy"),
    path('terms&condition',views.terms , name = "terms"),
    path('search',views.search , name = "search"),
    path('bengali-motivation',views.page_motivation , name = "page_motivation"),
    path('rahasya',views.page_mystery , name = "page_mystry"),
    path('true-bengali-incident',views.page_history , name = "page_history"),
    path('mojadar-information',views.page_fact , name = "page_fact"),
    path('bhoutik-kahini',views.page_horror , name = "page_horror"),
    path('bengali-movie-review',views.page_movie , name = "page_movie"),
    path('<slug:slug_text>',views.viewpost , name = "viewpost"),
    
    
    
]