from django.contrib import admin
from .models import Author, Tag, Post, Comment, ContactMessage

# Register your models here.

class postadmin(admin.ModelAdmin):
    list_filter=("author","tag","date")
    list_display=("title","date","author")
    prepopulated_fields={"slug":("title",)}

class commentadmin(admin.ModelAdmin):
    list_display=("user_name", "post")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'sent_at')

admin.site.register(Post,postadmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,commentadmin)