"""File for frontend slice of application"""


from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Function for parsing post list"""
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id):
    """Function for parsing post detail"""
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
