from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
# import boto3



# Create your views here.
def index(request):
    return render (request, 'index.html')

def food(request):
    return render (request, 'food.html')

def travel(request):
    return render (request, 'travel.html')

def create(request):
    return render (request, 'create.html')

def fashion(request):
    return render (request, 'fashion.html')

def login(request):
    return render (request, 'login.html')

def signup(request):
    return render (request, 'signup.html')

def upload(request):
    return render (request, 'upload.html')

def upload2(request):
    return render (request, 'upload2.html')
