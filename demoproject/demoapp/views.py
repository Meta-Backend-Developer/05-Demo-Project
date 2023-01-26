from django.shortcuts import render
from django.http import HttpResponse 
from .forms import ApplicationForm, LogForm


def index(request):
    # form = ApplicationForm()
    # return render(request, 'form.html', {'form':form})

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        # check whether for is valid
        if form.is_valid():
            # process the data
            # ...
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            post = form.cleaned_data['posts']
            return HttpResponse('Form successfully submitted')


def pathview(request, name, id):
    '''URL dispatcher parses name and id parameters and passes them to this function'''
    return HttpResponse("Name: {} UserID: {}".format(name, id))


def qryview(request):
    '''URL dispatcher does not parse name and id parameters. These are fetched from the request object's GET dictionary'''
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {} UserID: {}".format(name, id))

def showform(request):
    return render(request, "form")

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request, "home.html", context)
    
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