from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home/home.html' )

def create_post(request):
    return render(request, 'create-post/create-post.html' )

def login(request):
    return render(request, 'login/login.html' )


def get_form_login(request):
    
