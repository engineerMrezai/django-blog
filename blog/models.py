from django.db import models
from django.conf import settings
from django.db.models import Count
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date', 'updated_date']

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    category = models.ManyToManyField(Category, related_name='blog_posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='blog_posts',null=True)
    tags = models.ManyToManyField('Tag', related_name='blog_posts')
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def excerpt(self):
        return ' '.join(self.content.split()[:30]) + '...'


class Tag(models.Model):
    name = models.CharField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



