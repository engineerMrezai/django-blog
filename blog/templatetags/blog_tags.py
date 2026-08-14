from django import template

from blog.models import Category, Post, Tag
from django.db.models import Count, Q
from django.utils import timezone

register = template.Library()

@register.simple_tag()
def get_categories():
    return (
        Category.objects
        .annotate(
            post_count=Count(
                'blog_posts',
                filter=Q(
                    blog_posts__status=True,
                    blog_posts__published_date__lt=timezone.now(),
                )
            )
        ).order_by('-post_count')
    )

@register.simple_tag()
def get_post_pop():
    return Post.objects.filter(status=1, published_date__lt=timezone.now()).order_by('-counted_view')[:10]

@register.simple_tag()
def get_tags():
    return Tag.objects.all()

@register.simple_tag()
def get_last_posts(count=3):
    return Post.objects.filter(status=1, published_date__lt=timezone.now()).order_by('-created_date')[:count]