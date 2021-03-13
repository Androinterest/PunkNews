from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def blog(request):
    allPosts = Post.objects.all().order_by('-Sno')
    print(allPosts)
    context = {'allPosts':allPosts}
    return render(request,'blog/blog.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogPost.html',context) 

def category(request,cat):
    catPost = Post.objects.filter(category=cat)
    return render(request,'blog/category.html',{'catPost':catPost,'cat':cat})
