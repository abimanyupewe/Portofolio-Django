from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import BlogSection, Category

# Register your models here.
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BlogSectionAdmin(ModelAdmin):
    list_display = ('title', 'author', 'published', 'category', 'thumbnail')
    search_fields = ('title', 'author')
    list_filter = ('published', 'category')
    prepopulated_fields = {'slug': ('title',)}

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;"/>', obj.image.url)
        return 'No Image'
    thumbnail.short_description = 'Image'

admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogSection, BlogSectionAdmin)
