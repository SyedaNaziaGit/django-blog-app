from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
#auto_now_add date is updated only once when it is created 
#auto_now date is updated everytime it is called 
# here we are using django froala editor as a library add in installed apps
#pip install django-froala-editor
#pip install Pillow - to manage images in python 



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField(default = "Blog Content")
    #null and blank is true - so that it will allow the empty values
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=1000,null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='blog')
    
    def __str__(self):
        return self.title
    
    #override save method
    def save(self, *args,**kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
        
    
    