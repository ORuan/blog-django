from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField( max_length=1000)
    #img = models.ImageField(upload_to='static/uploads')
 
