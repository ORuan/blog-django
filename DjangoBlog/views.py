from django.shortcuts import render, redirect
from django.http import HttpResponse
from .services import post_create_bd
from .forms import *
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'home/home.html' )




def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():

            post_title = form.cleaned_data['title']
            post_content = form.cleaned_data['content']
            post_img = form.cleaned_data['img']

            new_post = create_bd_post(title=post_title, content=post_content, img=post_img)
            new_post.save()
            

        else:
            return redirect('')


            
    else:

        form = CreatePostForm()
        
    return render(request, 'create-post/create-post.html' , {'form': form })



def login(request):
    return render(request, 'login/login.html' )

    
