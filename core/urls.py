from django.urls import path 
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('about/<int:pk>', views.about, name='about'),
    path('investment/<int:pk>', views.investment, name='investment'),
    path('news/<int:pk>', views.news, name='news'),
]