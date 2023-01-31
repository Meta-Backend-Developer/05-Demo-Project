from django.urls import path
from . import views 
""" imports the views file from myapp directory
. represents current directory 'myapp' """

# define application namespace
app_name = 'demoapp'

urlpatterns = [
    path('', views.index, name='index'),  
    path('getuser/<name>/<id>', views.pathview, name='pathview'),  
    path('getuser/', views.qryview, name='qryview'),
    path('getform/', views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems),
    path('form/', views.showform, name='form'),
    path('formview/', views.form_view, name='formview'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
]
""" maps the index function from the views file to the homepage.
The index function generates the content of the page.
    '' represents homepage """