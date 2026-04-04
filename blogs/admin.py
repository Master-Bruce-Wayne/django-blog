from django.contrib import admin

# models
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    list_filter = ('category', 'author', 'status')
    list_editable = ('is_featured',)
    search_fields = ('id', 'title', 'category__category_name', 'status', 'content')
    # foreign keys -> < key >__< field_name >

    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)