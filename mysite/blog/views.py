from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27 , 2018'
    },
    {
        'author': 'dS',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 27 , 2018'
    }
]

# home


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


# about

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)
