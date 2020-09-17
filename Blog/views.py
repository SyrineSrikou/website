from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
import random
from .models import BlogPost, Comment

def index(request):
    blogposts = BlogPost.objects.order_by('-date') 
    context ={
         'blogposts' : blogposts
    }
    return render(request, 'Blog/blog.html', context)

def blogpost(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    comments = Comment.objects.order_by('-date')
    randomblogs = BlogPost.objects.all()[:4]
    context = {
        'blogpost' : blogpost,
        'randomblogs' : randomblogs,
        'comments' : comments
    }
    return render(request, 'Blog/blogpost.html', context)

def comment(request, blogpost_id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
        comment = Comment(name=name, email=email, message=message, blogpost= blogpost)
        comment.save()
    return redirect('/blog/')
