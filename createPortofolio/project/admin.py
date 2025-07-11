from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Framework, Status, Stack, Category, LanguageProgramming, ProjectSection
from django.utils.html import format_html

class LanguageProgrammingAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FrameworkAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StatusAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class StackAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProjectSectionAdmin(ModelAdmin):
    list_display = ('title', 'description', 'textBtn', 'link', 'stack', 'category', 'language', 'framework', 'status', 'thumbnail')
    search_fields = ('title','description')
    list_filter = ('language', 'framework', 'stack', 'category', 'status')
    list_per_page = 4

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;"/>'.format(obj.image.url))
        else:
            return 'No Image'
    thumbnail.short_description = 'Image'

admin.site.register(ProjectSection, ProjectSectionAdmin)
admin.site.register(Stack, StackAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(LanguageProgramming, LanguageProgrammingAdmin)
admin.site.register(Framework, FrameworkAdmin)
admin.site.register(Status, StatusAdmin)