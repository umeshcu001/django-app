from django.shortcuts import render
from .models import Blogpost, Blogsec
# Create your views here.
from django.http import HttpResponse

def index(request):
    myposts= Blogpost.objects.all()
    mypost= Blogsec.objects.all()
    return render(request, 'allblog/index.html', {'myposts': myposts, 'mypost': mypost})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request, 'allblog/blogpost.html',
                  {'post':post})

def blogsec(request, id):
    post = Blogsec.objects.filter(post_id1 = id)[0]
    return render(request, 'allblog/blogpost1.html',
                  {'post':post})
