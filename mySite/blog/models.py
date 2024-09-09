"""File for development database structure"""


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    """Class for management query sets"""
    def get_queryset(self) -> models.QuerySet:
        """Method for parsing query set's"""
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """Class Post for database"""
    class Status(models.TextChoices):
        """Post Status class"""
        DRAFT: tuple[str, str] = 'DF', 'Draft'
        PUBLISHED: tuple[str, str] = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(
        max_length=250,
        unique_for_date='publish'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_post'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """Class for sorting post's"""
        ordering: list[str] = ['-publish']
        indexes: list[models.Index] = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self) -> str:
        """Method for parsing strings.
        Yeah, this method return not string
        """
        return self.title

    def get_absolute_url(self) -> str:
        """Method for parsing absolute url"""
        return reverse(
            'blog:post_detail',
            args=[self.id]
        )
