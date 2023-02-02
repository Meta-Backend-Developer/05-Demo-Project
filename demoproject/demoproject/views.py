from django.http import  HttpResponse
from demoapp.views import *

def handler404(request, exception):
    return HttpResponse("404: Page not Found!")
