from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {
        'posts': posts,
    })

def detail(request, post_id):
    comment_form = CommentForm()

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        comment = Comment(post=post)
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            return redirect('blog_detail', post.id)

        #comment = post.comment_set.create(
        #        author=request.POST.get('author'),
        #        content=request.POST.get('content'),
        #        )
        # 아래는 필요없음.
        #comment = Comment()
        #comment.post = post
        #comment.author = request.POST['author']
        #comment.author = request.POST.get('author', "babo")
        #comment.content = request.POST['content']
        #comment.content = request.POST.get('content', "cococo")
        #comment.save()
    else:
        comment_form = CommentForm()
        post = Post.objects.get(id=post_id)
    
    return render(request, "post/detail.html", {
        'post': post,
        'comment_form': comment_form,
    })


