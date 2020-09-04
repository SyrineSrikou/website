from django.shortcuts import get_object_or_404, render
import random
from .models import BlogPost

def index(request):
    blogposts = BlogPost.objects.all() 
    context ={
         'blogposts' : blogposts
    }
    return render(request, 'Blog/blog.html', context)

def blogpost(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    context = {
        'blogpost' : blogpost
    }
    return render(request, 'Blog/blogpost.html', context)

