from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email =  models.EmailField( max_length=254)
    issu  =  models.CharField(max_length=300, default='')

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=254)
    content = models.TextField()
    slug= models.SlugField(max_length = 250, null = True, blank = True)
    autho =  models.CharField(max_length=50)
    date = models.DateTimeField(default=now())

    def __str__(self):

        return self.title + ' by '+ self.autho 
    

 
class Blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank = True)
 
    def __str__(self):
        return self.comment
    