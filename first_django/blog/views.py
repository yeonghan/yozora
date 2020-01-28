from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {
        'posts': posts,
    })

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/detail.html", {
        'post': post,
    })
