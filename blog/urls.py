from django.contrib import admin
from django.urls import path,include
from . import views
from  .models import Contact,Blog


urlpatterns = [
    path('',views.head ,name ="index"),
    path('contact/',views.contact,name ="contact"),
    path('blog/',views.blog,name ="blog"),
    path('blogpost/',views.blogpost,name ="blogpost" ),
    path('search/',views.Search,name ="Search"),
    path('singup',views.singup,name ="singup"),
    path('login',views.login,name ="login"),
    path('logout',views.userlogout,name ="logout"),
    path('postcomments',views.postcomments,name ="postcomment" ),
    path('userpost',views.userpost,name ="userpost" ),

    path('<str:slug>/',views.blogpost,name ="blogpost" ),

   #api
    
    
    

    
]