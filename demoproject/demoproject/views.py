from django.http import  HttpResponse

def handler404(request, exception):
    return HttpResponse("404: Page not Found!")