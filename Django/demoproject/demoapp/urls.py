from django.urls import path
from . import views 
""" imports the views file from myapp directory
. represents current directory 'myapp' """

urlpatterns = [
    path('', views.index, name='index'),    
]
""" maps the index function from the views file to the homepage.
The index function generates the content of the page.
    '' represents homepage """