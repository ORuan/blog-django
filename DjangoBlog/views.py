from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from .services import post_create_bd
from .forms import *
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home/home.html' )


def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        print(form)
        if form.is_valid():
            print('dentro')
            #post_title = form.cleaned_data['title']
            #post_content = form.cleaned_data['content']
            #new_post = post_create_bd(title=post_title, content=post_content)
            form.save()
            #new_post.save()
            return redirect('/')
        form = CreatePostForm()
        return render(request, 'create-post/create-post.html', {'form':form})

    else: 
        form = CreatePostForm()
        return render(request, 'create-post/create-post.html', {'form':form})
    return HttpResponse('funcionou menozada')

       
   



def login(request):
    return render(request, 'login/login.html' )

    
