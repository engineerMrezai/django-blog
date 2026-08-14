from django.contrib import admin
from website.models import Contact, Newsletter


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','created_date','updated_date']
    list_filter = ['email']
    search_fields = ['name','email','subject']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email']
    list_filter = ['email']
    search_fields = ['email']


