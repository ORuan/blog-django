from django.urls import path
from .views import *
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home-page"),
    path('create-post/', create_post, name="create-post"),
    path('login/', create_post, name="create-post"),


    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)