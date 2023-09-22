from django.contrib import admin
from .models import Contact,Blog,Blogcomment



# Register your models here.
admin.site.register(Contact)
admin.site.register((Blog,Blogcomment))
