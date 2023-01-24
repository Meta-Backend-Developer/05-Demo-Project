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
    path('showform/', views.showform, name='showform'),
    path('getform/', views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems),
]
""" maps the index function from the views file to the homepage.
The index function generates the content of the page.
    '' represents homepage """