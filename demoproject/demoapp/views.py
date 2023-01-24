from django.shortcuts import render
from django.http import HttpResponse 


def index(request):
    path = request.path
    method = request.method
    content = '''
        <center>
            <h2>Testing Django Request Response Objects</h2>
            <p>Request path: " {}</p>
            <p>Request method: {}</p>
        </center>
        '''.format(path, method)
    return HttpResponse(content)


def pathview(request, name, id):
    '''URL dispatcher parses name and id parameters and passes them to this function'''
    return HttpResponse("Name: {} UserID: {}".format(name, id))


def qryview(request):
    '''URL dispatcher does not parse name and id parameters. These are fetched from the request object's GET dictionary'''
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} UserID: {}".format(name, id))

def showform(request):
    return render(request, "form.html")

def getform(request):
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
    return HttpResponse("Name: {} UserID: {}".format(name, id))


def menuitems(request, dish):
    items = {'pasta' : 'noddle thingies',
            'falafel': 'deep fried patties',
            'cheesecake' : 'not what it sounds like',
    }

    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)