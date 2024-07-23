from ast import Index
from typing import Literal
from django.conf import settings
from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    
    def get_queryset(self) -> models.QuerySet:
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
            )


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT: tuple[Literal['DF']] = 'DF', 'Draft'
        PUBLISHED: tuple[Literal['DF']] = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )
    objects = models.Manager()
    # Not work yet
    # published = models.PublishedManager()  

    class Meta:
        ordering: list[str] = ['-publish']
        indexes: list[Index] = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self) -> str:
        return self.title
