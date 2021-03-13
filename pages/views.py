from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from pages.models import extUser
from django.conf import settings
import os

# Create your views here.
def about(request):
    return render(request,'pages/about.html')

def contacts(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if len(name)<2 and len(email)<3 and len(message)<3:
            messages.error(request,"Enter the Details Correctly")
        else:
            Contact = contact(name=name, email=email, textfield=message)
            Contact.save()
            messages.success(request, 'Your Message have been Sent Successfully')
    return render(request,'pages/contact.html')

def search(request):
    query = request.GET.get('q')
    searchPostTitle = Post.objects.filter(title__icontains=query)
    searchPostCont = Post.objects.filter(content__icontains=query)
    searchPost = searchPostCont.union(searchPostTitle)
    params = {'searchPost':searchPost, 'query':query}
    return render(request,'pages/search.html',params)

def signup(request):
    username = request.POST['username']
    email = request.POST['email']
    phone = request.POST['phone']
    fname = request.POST['fname']
    lname = request.POST['lname']
    age = request.POST['age']
    password = request.POST['password']
    newuser = User.objects.create_user(username,email,password)
    newuser.first_name = fname
    newuser.last_name = lname
    newuser.save()
    extuser = extUser(phone=phone,user=newuser,age=age)
    extuser.save()
    messages.success(request,"Your Account Has Been Created Successfully")
    return redirect('/')

def userlogin(request):
    username = request.POST['loginusername']
    password = request.POST['loginpassword']

    user = authenticate(username=username,password=password)
    
    if user is not None:
        login(request, user)
        messages.success(request,"You Have been Logged In Successfully")
        return redirect('/')
    else:
        messages.error(request,"Incorrect Username/Password")
        return redirect("/")

def userlogout(request):
    logout(request)
    messages.success(request,"You have Been Logged Out Successfully")
    return redirect('/')

def myaccount(request):
    userprofile = extUser.objects.filter(user=request.user)
    return render(request,'pages/myaccount.html',{'udata':userprofile})

def editprofile(request):
    userprofile = extUser.objects.filter(user=request.user)
    return render(request,'pages/editprofile.html',{'udata':userprofile})

def updateprofile(request):
    userdata = extUser.objects.get(user__id=request.user.id)
    if request.method=="POST":
        print(request.POST)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']

        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()

        userdata.phone = phone
        userdata.age = age
        userdata.save()
        if "profileimg" in request.FILES:
            os.remove(os.path.join(settings.MEDIA_ROOT,str(userdata.profileimg)))
            profileimg = request.FILES['profileimg']
            userdata.profileimg = profileimg
            userdata.save()
        messages.success(request,"Profile Updated Successfully")
    return redirect('/')

def changepass(request):
    if request.method=="POST":
        currentPass = request.POST['curPass']
        newPass = request.POST['newPass']

    user = User.objects.get(id=request.user.id)
    checkPass = user.check_password(currentPass)
    if checkPass == True:
        user.set_password(newPass)
        user.save()
        login(request,user)
        messages.success(request,"Password Changed Successfully")
    else:
        messages.error(request,"Current Password is Wrong! Try Again")
    return render(request,'pages/editprofile.html')