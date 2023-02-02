from django.urls import path
from . import views 

# define application namespace
app_name = 'demoapp'

urlpatterns = [
    path('home/', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book')
]
