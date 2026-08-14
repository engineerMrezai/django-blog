from django.contrib import admin
from blog.models import Post, Category, Tag


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['title','author','get_category','counted_view','status','published_date','created_date', 'updated_date']
    list_filter = ['status','created_date','author','category']
    # ordering = ['-created_date']
    search_fields = ['title','content']

    @staticmethod
    def get_category(obj):
        return ', '.join([category.name for category in obj.category.all()])

# admin.site.register(Post,PostAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name','created_date','updated_date']
    list_filter = ['created_date']
    search_fields = ['name']
    fields = ["name"]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ['name','created_date','updated_date']
    list_filter = ['created_date']
    search_fields = ['name']
    fields = ["name"]
