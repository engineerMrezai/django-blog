from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1,published_date__lt=timezone.now())
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,id):
    post = get_object_or_404(Post,id=id,status=1, published_date__lt=timezone.now())
    post.counted_view += 1
    post.save()
    content = {'post':post}
    return render(request, 'blog/blog-single.html',content)
