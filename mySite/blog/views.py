"""File for frontend slice of application"""


from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Post, PublishedManager


def post_list(request) -> HttpResponse:
    """Function for parsing post list"""
    posts: PublishedManager = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, id) -> HttpResponse:
    """Function for parsing post detail"""
    post: Post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
