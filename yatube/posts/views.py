from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.http import HttpResponse


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts
    }
    template = 'posts/group_list.html'
    return render(request, template, context)
