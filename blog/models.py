from django.db import models
from django.utils.text import slugify
import string
import random
import uuid
from django.db.models.signals import pre_save
from kahini.utils import unique_slug_generator

def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    metatags = models.TextField()
    metadesc = models.TextField()
    category = models.CharField(max_length = 100)
    image = models.URLField()
    date = models.DateTimeField()
    slug = models.SlugField(max_length=255,  null = True , blank = True)
    
    
    def __str__(self):
        return self.title

def slug_generator(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator,sender = Blog)



class Page_seo(models.Model):
    name =  models.CharField(max_length = 100)
    title = models.TextField()
    metatags = models.TextField()
    metadesc = models.TextField()
    def __str__(self):
        return self.name

class report(models.Model):
    email = models.EmailField()
    discription = models.TextField()
    def __str__(self):
        return self.email

class feature(models.Model):
    title = models.CharField(max_length = 100)
    post = models.CharField(max_length = 100)
    image = models.URLField()
    def __str__(self):
        return self.post