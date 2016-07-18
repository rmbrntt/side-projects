from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime
# Create your views here.



def index(request):
    t = loader.get_template('index.html')
    c = Context({'current_time': datetime.now(), })
    return HttpResponse(t.render(c))



def tasks(request):
    return HttpResponse('<html><body>Tasks page</body></html>')

def projects(request):

    return HttpResponse('<html><body>Query github projects into a table</body></html>')

def notes(request):
    return HttpResponse('<html><body>Create a running notes</body></html>')

def home(request):
    t = loader.get_template('home.html')
    c = Context({'current_time': datetime.now(), })
    return HttpResponse(t.render(c))

