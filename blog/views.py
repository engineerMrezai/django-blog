from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Count, Q

from blog.models import Post, Category


def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lt=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, id):
    post = get_object_or_404(Post, id=id, status=1, published_date__lt=timezone.now())
    previous_post = Post.objects.filter(status=1, published_date__lt=post.published_date).order_by(
        '-published_date').first()
    next_post = Post.objects.filter(status=1, published_date__gt=post.published_date,
                                    published_date__lt=timezone.now()).first()
    post.counted_view += 1
    post.save()
    content = {'post': post, 'previous_post': previous_post, 'next_post': next_post}
    return render(request, 'blog/blog-single.html', content)
