from django import views
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('home/', views.index, name = 'index'),
    path('pricing/', views.pricing, name= 'pricing'),
    path('user_research/', views.user_research, name = 'user_research'),
    path('web_development/', views.web_development, name= 'web_development'),
    
]
