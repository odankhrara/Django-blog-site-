from django.http import HttpResponse
from django.shortcuts import render,redirect
from  .models import Contact,Blog,Blogcomment
from django.contrib import messages
from django.contrib.auth import login as logins
 
from django.contrib.auth import authenticate,logout

from django.contrib.auth.models import User



def head(request):
    return render(request,'home/index.html')

def contact(request):
    
    if request.method=='POST':
        name= request.POST['name']
        email= request.POST['email']
        issu= request.POST['issu']
        contact = Contact(name=name, email=email,issu =issu)
        contact.save()
        
        messages.success(request,"Your request are saved in our data")

    
    return render(request,'home/contact.html')


def blog(request):
     allblog = Blog.objects.all()
     context = {'allblog':allblog}
    

     return render(request,'home/blog.html',context)

def Search(request):
    
    query = request.GET['query']
    if len(query)>78:
       allblog = Blog.objects.none()
    allblogtitle = Blog.objects.filter(title__icontains=query  )
    allblogaddcontent = Blog.objects.filter(content__icontains=query  )
    allblog = allblogaddcontent.union(allblogtitle)
    params={'allblog':allblog, 'query':query}

    if allblog.count()==0:
        messages.error(request,"No result avilable")
     
    return render(request,'home/search.html',params)
 
def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    
   
    comments = Blogcomment.objects.filter(post=blog)
    context = {'blog':blog,'comment':comments}
    

    return render(request,'home/blogpost.html',context)

def singup(request):
    if request.method == 'POST':
       uname = request.POST['uname']
       fname = request.POST['fname']
       lname = request.POST['lname']
       email = request.POST['email']
       password = request.POST['password']
       copassword = request.POST['copassword']
       city = request.POST['city']
       
       if len(uname)>10:
           messages.error(request,"Uname must be less then 20 words")
           return redirect('/')

       if password != copassword:
           messages.error(request,"Conform password are not match")
           return redirect('/')

    

       
             

     
       #Create new user 
       user= User.objects.create_user(uname,email,password)
       user.first_name = fname
       user.last_name = lname
       user.user_city = city
       user.save()
       messages.success(request,"Your account has been created")
       return redirect('/')
    else:
        return HttpResponse("Plese submit form ")
    

def login(request):
    if request.method == 'POST':
       loguname = request.POST['loguname']
       logpassword = request.POST['logpassword']

       user = authenticate(username=loguname,password=logpassword)
       if user is not None:
           logins(request,user)
           messages.success(request,"sucessfully login ")
           return redirect('/')
       else:
            
            messages.error(request,"Please check uname or password ")
            return redirect('/')

    
    return HttpResponse('not found')


def userlogout(request):
    
   logout(request)
   messages.success(request,"logout successfully ")
   return redirect('/')
        
def postcomments(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('blogsno')
        post= Blog.objects.get(sno=postSno)
        comment = Blogcomment(comment= comment, user=user, post=post)
        comment.save()

        messages.success(request, "Your comment has been posted successfully")
        
        
    return redirect(f"/{post.slug}")

    
def userpost(request):
    if request.method == "POST":
        title= request.POST['title']
        content= request.POST['content']
        
        autho =  request.user
        upost = Blog(title=title,content=contact,autho=autho)
        upost.save()
        
        messages.success(request,"Your request are saved in our data")
       
   


    return render(request,'home/userpost.html')