from django.shortcuts import render
from models import BlogPost


def archive(request):
    blogposts = BlogPost.objects.all()
    context = {
        'blogposts': blogposts,
    }

    return render(request, 'archive.html', context)
