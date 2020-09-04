from django.shortcuts import render
from .models import TeamMember, Partner
from Blog.models import BlogPost
from references.models import Reference

def index(request):
    partners = Partner.objects.all()
    members = TeamMember.objects.all()
    randomblogs = BlogPost.objects.all()[:3]
    randomreferences = Reference.objects.all()[:4]
    context = {
        'partners' : partners, 
        'members' : members,
        'randomblogs' : randomblogs,
        'randomreferences': randomreferences
    }
    return render(request, 'pages/index.html', context)

def about(request):
    members = TeamMember.objects.all()
    context = {
        'members' : members
    }
    return render(request, 'pages/about.html', context)

