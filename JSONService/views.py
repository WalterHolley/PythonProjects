# Create your views here.
from django.http import HttpResponse
from SoccerDataModels.models import *

def index(request):
    return HttpResponse("This is a test")

def GetCountries(request):
    return HttpResponse("Now you haev your countries")