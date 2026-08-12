from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_date'
    list_display = ['title','author','counted_view','status','published_date','created_date', 'updated_date']
    list_filter = ['status','created_date','author']
    # ordering = ['-created_date']
    search_fields = ['title','content']

# admin.site.register(Post,PostAdmin)
