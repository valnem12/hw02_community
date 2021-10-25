from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    """Main page - dispalying the latest ten posts"""

    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Filters by group and displays ten latest posts"""

    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts_by_group = (group
                .relevant_group
                .filter(group=group)[:10])
    context = {
        'group': group,
        'posts_by_group': posts_by_group
    }
    return render(request, template, context)
