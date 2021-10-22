from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = "posts/index.html"
    text = "Это главная страница проекта Yatube"
    posts = Post.objects.all()[:10]
    context = {
        'text': text,
        'posts': posts
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    posts_by_group = (Post
            .objects
            .filter(group=group)
            .all()[:10]
            )
    context = {
        'group': group,
        'posts_by_group': posts_by_group
    }
    return render(request, template, context)
