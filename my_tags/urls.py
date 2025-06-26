from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('filters/', views.filter_demo, name="filters"),
    path('blogs/', views.blog_list, name="blogs"),
    path('subscribe/', views.subscribe, name="subscribe"),
    
]
